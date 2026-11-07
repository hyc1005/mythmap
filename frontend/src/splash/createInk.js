/*
MIT License

Copyright (c) 2017 Pavel Dobryakov

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
*/

/*
 * 山海寻踪 · 水墨流体层
 *
 * 基于 PavelDoGreat/WebGL-Fluid-Simulation 的 script.js 改造：
 *   - 保留：速度场求解（curl / vorticity / pressure / advection）与 FBO 封装
 *   - 删除：GUI、统计、推广弹窗、bloom、sunrays、shading、截图、随机彩色、全局事件
 *   - 新增：颜料通道显示（减色、预乘 alpha 透明输出）、程序化纤维纹理、
 *           工厂函数 + destroy、程序化滴墨 / 笔触 API、帧率探测、降级回调
 *
 * 坐标约定（对外 API）：CSS 坐标，(0,0) 左上，(1,1) 右下，y 向下。
 * 速度约定：dx / dy 与原版同量级（约 50–500），方向同 CSS（y 向下为正）。
 * 颜料：dye 的 R/G/B 通道依次为 墨 / 朱红 / 淡彩，各自独立。
 */

const DEFAULT_PALETTE = {
    ink:   '#100704',   // 九尾狐图勾线
    red:   '#E01E07',   // 九尾狐图主红（站内砖红备选：#A4321B）
    cream: '#F8CF8C',   // 九尾狐图毛色
};

const PIGMENT_CHANNEL = { ink: 'r', red: 'g', cream: 'b' };

function getWebGLContext (canvas) {
    const params = { alpha: true, depth: false, stencil: false, antialias: false, preserveDrawingBuffer: false };

    let gl = canvas.getContext('webgl2', params);
    const isWebGL2 = !!gl;
    if (!isWebGL2)
        gl = canvas.getContext('webgl', params) || canvas.getContext('experimental-webgl', params);

    if (!gl) return null;

    let halfFloat;
    let supportLinearFiltering;
    if (isWebGL2) {
        gl.getExtension('EXT_color_buffer_float');
        supportLinearFiltering = gl.getExtension('OES_texture_float_linear');
    } else {
        halfFloat = gl.getExtension('OES_texture_half_float');
        supportLinearFiltering = gl.getExtension('OES_texture_half_float_linear');
    }

    gl.clearColor(0.0, 0.0, 0.0, 1.0);

    const halfFloatTexType = isWebGL2 ? gl.HALF_FLOAT : halfFloat.HALF_FLOAT_OES;
    let formatRGBA;
    let formatRG;
    let formatR;

    if (isWebGL2)
    {
        formatRGBA = getSupportedFormat(gl, gl.RGBA16F, gl.RGBA, halfFloatTexType);
        formatRG = getSupportedFormat(gl, gl.RG16F, gl.RG, halfFloatTexType);
        formatR = getSupportedFormat(gl, gl.R16F, gl.RED, halfFloatTexType);
    }
    else
    {
        formatRGBA = getSupportedFormat(gl, gl.RGBA, gl.RGBA, halfFloatTexType);
        formatRG = getSupportedFormat(gl, gl.RGBA, gl.RGBA, halfFloatTexType);
        formatR = getSupportedFormat(gl, gl.RGBA, gl.RGBA, halfFloatTexType);
    }


    return {
        gl,
        ext: {
            formatRGBA,
            formatRG,
            formatR,
            halfFloatTexType,
            supportLinearFiltering
        }
    };
}

function getSupportedFormat (gl, internalFormat, format, type)
{
    if (!supportRenderTextureFormat(gl, internalFormat, format, type))
    {
        switch (internalFormat)
        {
            case gl.R16F:
                return getSupportedFormat(gl, gl.RG16F, gl.RG, type);
            case gl.RG16F:
                return getSupportedFormat(gl, gl.RGBA16F, gl.RGBA, type);
            default:
                return null;
        }
    }

    return {
        internalFormat,
        format
    }
}

function supportRenderTextureFormat (gl, internalFormat, format, type) {
    let texture = gl.createTexture();
    gl.bindTexture(gl.TEXTURE_2D, texture);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.NEAREST);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.NEAREST);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);
    gl.texImage2D(gl.TEXTURE_2D, 0, internalFormat, 4, 4, 0, format, type, null);

    let fbo = gl.createFramebuffer();
    gl.bindFramebuffer(gl.FRAMEBUFFER, fbo);
    gl.framebufferTexture2D(gl.FRAMEBUFFER, gl.COLOR_ATTACHMENT0, gl.TEXTURE_2D, texture, 0);

    let status = gl.checkFramebufferStatus(gl.FRAMEBUFFER);
    return status == gl.FRAMEBUFFER_COMPLETE;
}

function isMobile () {
    return /Mobi|Android/i.test(navigator.userAgent);
}

function hexToRgb (hex) {
    let h = String(hex).replace('#', '');
    if (h.length === 3) h = h.split('').map(c => c + c).join('');
    const n = parseInt(h, 16);
    return [((n >> 16) & 255) / 255, ((n >> 8) & 255) / 255, (n & 255) / 255];
}

function clamp01 (v) {
    return Math.min(1, Math.max(0, v));
}

// 显示 shader：dye 通道 → 颜料覆盖度 → 预乘 alpha 输出（无墨处完全透明）
const DISPLAY_SHADER = `
    precision highp float;
    precision highp sampler2D;

    varying vec2 vUv;
    uniform sampler2D uTexture;    // dye: r=墨 g=朱红 b=淡彩
    uniform sampler2D uPaperTex;   // 纤维噪声，只用来扰动边缘
    uniform sampler2D uStrokeTex;
    uniform vec4 uStrokeBox;
    uniform float uStrokeEnabled;
    uniform vec2  uPaperScale;
    uniform float uSoft;           // >= 0.02
    uniform float uGrain;
    uniform float uHalo;
    uniform vec3 uInk;
    uniform vec3 uRed;
    uniform vec3 uCream;

    void over (inout vec3 rgb, inout float a, vec3 c, float m) {
        rgb = c * m + rgb * (1.0 - m);
        a   = m + a * (1.0 - m);
    }

    void main () {
        vec3 d = max(texture2D(uTexture, vUv).rgb, vec3(0.0));
        float n = texture2D(uPaperTex, vUv * uPaperScale).r;

        vec3 raw = 1.0 - exp(-d * 1.8);

        float th = 0.5 + (n - 0.5) * uGrain;
        vec3 k = smoothstep(vec3(th - uSoft), vec3(th + uSoft), raw);
        k *= smoothstep(vec3(0.02), vec3(0.10), raw);   // 去掉软边时低浓度处的"鬼影"

        vec3 rgb = vec3(0.0);
        float a = 0.0;
        over(rgb, a, uInk,   smoothstep(0.12, 0.45, raw.r) * uHalo);
        over(rgb, a, uRed,   k.g);
        over(rgb, a, uInk,   k.r);
        over(rgb, a, uCream, k.b);

        if (uStrokeEnabled > 0.5) {
            vec2 at = (vec2(vUv.x, 1.0 - vUv.y) - uStrokeBox.xy) / uStrokeBox.zw;
            rgb *= 0.33;
            a *= 0.33;
            if (all(greaterThanEqual(at, vec2(0.0))) && all(lessThanEqual(at, vec2(1.0)))) {
                vec4 stroke = texture2D(uStrokeTex, at);
                over(rgb, a, stroke.rgb, stroke.a);
            }
        }
        gl_FragColor = vec4(rgb, a);
    }
`;

// 程序化纤维纹理（512×512，必须是 2 的幂以便 WebGL1 使用 REPEAT）
function makeFiberTexture (gl, url) {
    const N = 512;
    let seed = 0x9e3779b9;
    const rand = () => {              // mulberry32，保证每次生成一致
        seed = (seed + 0x6D2B79F5) | 0;
        let t = Math.imul(seed ^ (seed >>> 15), 1 | seed);
        t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
        return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };

    // 白噪声 + 5×5 箱式模糊（可平铺）→ 兼有颗粒与低频起伏
    const W = new Float32Array(N * N);
    for (let i = 0; i < W.length; i++) W[i] = rand();
    const tmp = new Float32Array(N * N);
    const B = new Float32Array(N * N);
    for (let y = 0; y < N; y++)
        for (let x = 0; x < N; x++) {
            let s = 0;
            for (let k = -2; k <= 2; k++) s += W[y * N + ((x + k + N) % N)];
            tmp[y * N + x] = s / 5;
        }
    for (let y = 0; y < N; y++)
        for (let x = 0; x < N; x++) {
            let s = 0;
            for (let k = -2; k <= 2; k++) s += tmp[((y + k + N) % N) * N + x];
            B[y * N + x] = s / 5;
        }

    const c = document.createElement('canvas');
    c.width = c.height = N;
    const g = c.getContext('2d');
    const img = g.createImageData(N, N);
    for (let i = 0; i < N * N; i++) {
        const v = clamp01(0.5 + (W[i] - 0.5) * 0.5 + (B[i] - 0.5) * 2.0);
        const b = Math.round(v * 255);
        img.data[i * 4] = img.data[i * 4 + 1] = img.data[i * 4 + 2] = b;
        img.data[i * 4 + 3] = 255;
    }
    g.putImageData(img, 0, 0);

    // 纤维：短线，8 个偏移副本保证平铺无缝
    g.lineCap = 'round';
    for (let i = 0; i < 1500; i++) {
        const x = rand() * N, y = rand() * N;
        const len = 3 + rand() * 9, ang = rand() * Math.PI;
        const dx = Math.cos(ang) * len, dy = Math.sin(ang) * len;
        const alpha = 0.04 + rand() * 0.04;
        g.strokeStyle = rand() < 0.5 ? `rgba(255,255,255,${alpha})` : `rgba(0,0,0,${alpha})`;
        g.lineWidth = 0.6 + rand() * 0.8;
        for (let ox = -N; ox <= N; ox += N)
            for (let oy = -N; oy <= N; oy += N) {
                g.beginPath();
                g.moveTo(x + ox, y + oy);
                g.lineTo(x + ox + dx, y + oy + dy);
                g.stroke();
            }
    }

    const texture = gl.createTexture();
    gl.bindTexture(gl.TEXTURE_2D, texture);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.REPEAT);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.REPEAT);
    gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA, gl.RGBA, gl.UNSIGNED_BYTE, c);

    const obj = {
        texture,
        width: N,
        height: N,
        attach (id) {
            gl.activeTexture(gl.TEXTURE0 + id);
            gl.bindTexture(gl.TEXTURE_2D, texture);
            return id;
        }
    };

    if (url) {   // 可选：换成自己的纸纹素材（尺寸需为 2 的幂）
        const image = new Image();
        image.onload = () => {
            obj.width = image.width;
            obj.height = image.height;
            gl.bindTexture(gl.TEXTURE_2D, texture);
            gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA, gl.RGBA, gl.UNSIGNED_BYTE, image);
        };
        image.src = url;
    }
    return obj;
}

/**
 * 创建水墨流体层。
 * @param {HTMLCanvasElement} canvas  必须由 CSS 指定尺寸
 * @param {object} [opts]
 * @returns {object|null}  WebGL 不可用 / 用户要求减少动态效果时返回 null，调用方走降级
 */
export function createInk (canvas, opts = {}) {
    if (opts.respectReducedMotion !== false &&
        typeof matchMedia === 'function' &&
        matchMedia('(prefers-reduced-motion: reduce)').matches)
        return null;

    let ctx = null;
    try { ctx = getWebGLContext(canvas); } catch (e) { ctx = null; }
    if (!ctx || !ctx.ext.formatRGBA || !ctx.ext.formatRG || !ctx.ext.formatR) return null;
    const { gl, ext } = ctx;

    const maxDpr = opts.maxDpr != null ? opts.maxDpr : 2;
    const low = opts.quality === 'low' || (opts.quality !== 'high' && isMobile());

    const config = {
        SIM_RESOLUTION: low ? 64 : 128,
        DYE_RESOLUTION: low ? 512 : 1024,
        DENSITY_DISSIPATION: 0.15,    // 实测：0.4 时细线 6 秒后只剩约 27%，0.15 时仍保留约 95%
        VELOCITY_DISSIPATION: 3.0,
        PRESSURE: 0.8,
        PRESSURE_ITERATIONS: low ? 14 : 20,
        CURL: 10,
        SPLAT_RADIUS: 0.08,
        SOFT: opts.soft != null ? opts.soft : 0.06,
        GRAIN: opts.grain != null ? opts.grain : 0.4,
        HALO: opts.halo != null ? opts.halo : 0.0,
    };
    if (!ext.supportLinearFiltering) config.DYE_RESOLUTION = 512;
    config.SOFT = Math.max(0.02, config.SOFT);

    const palette = Object.assign({}, DEFAULT_PALETTE, opts.palette || {});
    const paletteRgb = {};
    const refreshPalette = () => {
        for (const k of ['ink', 'red', 'cream']) paletteRgb[k] = hexToRgb(palette[k]);
    };
    refreshPalette();

    let destroyed = false;
    let running = false;
    let raf = 0;

    resizeCanvas();

    class Material {
        constructor (vertexShader, fragmentShaderSource) {
            this.vertexShader = vertexShader;
            this.fragmentShaderSource = fragmentShaderSource;
            this.programs = [];
            this.activeProgram = null;
            this.uniforms = [];
        }

        setKeywords (keywords) {
            let hash = 0;
            for (let i = 0; i < keywords.length; i++)
                hash += hashCode(keywords[i]);

            let program = this.programs[hash];
            if (program == null)
            {
                let fragmentShader = compileShader(gl.FRAGMENT_SHADER, this.fragmentShaderSource, keywords);
                program = createProgram(this.vertexShader, fragmentShader);
                this.programs[hash] = program;
            }

            if (program == this.activeProgram) return;

            this.uniforms = getUniforms(program);
            this.activeProgram = program;
        }

        bind () {
            gl.useProgram(this.activeProgram);
        }
    }

    class Program {
        constructor (vertexShader, fragmentShader) {
            this.uniforms = {};
            this.program = createProgram(vertexShader, fragmentShader);
            this.uniforms = getUniforms(this.program);
        }

        bind () {
            gl.useProgram(this.program);
        }
    }

    function createProgram (vertexShader, fragmentShader) {
        let program = gl.createProgram();
        gl.attachShader(program, vertexShader);
        gl.attachShader(program, fragmentShader);
        gl.linkProgram(program);

        if (!gl.getProgramParameter(program, gl.LINK_STATUS))
            console.trace(gl.getProgramInfoLog(program));

        return program;
    }

    function getUniforms (program) {
        let uniforms = [];
        let uniformCount = gl.getProgramParameter(program, gl.ACTIVE_UNIFORMS);
        for (let i = 0; i < uniformCount; i++) {
            let uniformName = gl.getActiveUniform(program, i).name;
            uniforms[uniformName] = gl.getUniformLocation(program, uniformName);
        }
        return uniforms;
    }

    function compileShader (type, source, keywords) {
        source = addKeywords(source, keywords);

        const shader = gl.createShader(type);
        gl.shaderSource(shader, source);
        gl.compileShader(shader);

        if (!gl.getShaderParameter(shader, gl.COMPILE_STATUS))
            console.trace(gl.getShaderInfoLog(shader));

        return shader;
    };

    function addKeywords (source, keywords) {
        if (keywords == null) return source;
        let keywordsString = '';
        keywords.forEach(keyword => {
            keywordsString += '#define ' + keyword + '\n';
        });
        return keywordsString + source;
    }

    const baseVertexShader = compileShader(gl.VERTEX_SHADER, `
        precision highp float;

        attribute vec2 aPosition;
        varying vec2 vUv;
        varying vec2 vL;
        varying vec2 vR;
        varying vec2 vT;
        varying vec2 vB;
        uniform vec2 texelSize;

        void main () {
            vUv = aPosition * 0.5 + 0.5;
            vL = vUv - vec2(texelSize.x, 0.0);
            vR = vUv + vec2(texelSize.x, 0.0);
            vT = vUv + vec2(0.0, texelSize.y);
            vB = vUv - vec2(0.0, texelSize.y);
            gl_Position = vec4(aPosition, 0.0, 1.0);
        }
    `);

    const copyShader = compileShader(gl.FRAGMENT_SHADER, `
        precision mediump float;
        precision mediump sampler2D;

        varying highp vec2 vUv;
        uniform sampler2D uTexture;

        void main () {
            gl_FragColor = texture2D(uTexture, vUv);
        }
    `);

    const clearShader = compileShader(gl.FRAGMENT_SHADER, `
        precision mediump float;
        precision mediump sampler2D;

        varying highp vec2 vUv;
        uniform sampler2D uTexture;
        uniform float value;

        void main () {
            gl_FragColor = value * texture2D(uTexture, vUv);
        }
    `);

    const splatShader = compileShader(gl.FRAGMENT_SHADER, `
        precision highp float;
        precision highp sampler2D;

        varying vec2 vUv;
        uniform sampler2D uTarget;
        uniform float aspectRatio;
        uniform vec3 color;
        uniform vec2 point;
        uniform float radius;

        void main () {
            vec2 p = vUv - point.xy;
            p.x *= aspectRatio;
            vec3 splat = exp(-dot(p, p) / radius) * color;
            vec3 base = texture2D(uTarget, vUv).xyz;
            gl_FragColor = vec4(base + splat, 1.0);
        }
    `);

    const advectionShader = compileShader(gl.FRAGMENT_SHADER, `
        precision highp float;
        precision highp sampler2D;

        varying vec2 vUv;
        uniform sampler2D uVelocity;
        uniform sampler2D uSource;
        uniform vec2 texelSize;
        uniform vec2 dyeTexelSize;
        uniform float dt;
        uniform float dissipation;

        vec4 bilerp (sampler2D sam, vec2 uv, vec2 tsize) {
            vec2 st = uv / tsize - 0.5;

            vec2 iuv = floor(st);
            vec2 fuv = fract(st);

            vec4 a = texture2D(sam, (iuv + vec2(0.5, 0.5)) * tsize);
            vec4 b = texture2D(sam, (iuv + vec2(1.5, 0.5)) * tsize);
            vec4 c = texture2D(sam, (iuv + vec2(0.5, 1.5)) * tsize);
            vec4 d = texture2D(sam, (iuv + vec2(1.5, 1.5)) * tsize);

            return mix(mix(a, b, fuv.x), mix(c, d, fuv.x), fuv.y);
        }

        void main () {
        #ifdef MANUAL_FILTERING
            vec2 coord = vUv - dt * bilerp(uVelocity, vUv, texelSize).xy * texelSize;
            vec4 result = bilerp(uSource, coord, dyeTexelSize);
        #else
            vec2 coord = vUv - dt * texture2D(uVelocity, vUv).xy * texelSize;
            vec4 result = texture2D(uSource, coord);
        #endif
            float decay = 1.0 + dissipation * dt;
            gl_FragColor = result / decay;
        }`,
        ext.supportLinearFiltering ? null : ['MANUAL_FILTERING']
    );

    const divergenceShader = compileShader(gl.FRAGMENT_SHADER, `
        precision mediump float;
        precision mediump sampler2D;

        varying highp vec2 vUv;
        varying highp vec2 vL;
        varying highp vec2 vR;
        varying highp vec2 vT;
        varying highp vec2 vB;
        uniform sampler2D uVelocity;

        void main () {
            float L = texture2D(uVelocity, vL).x;
            float R = texture2D(uVelocity, vR).x;
            float T = texture2D(uVelocity, vT).y;
            float B = texture2D(uVelocity, vB).y;

            vec2 C = texture2D(uVelocity, vUv).xy;
            if (vL.x < 0.0) { L = -C.x; }
            if (vR.x > 1.0) { R = -C.x; }
            if (vT.y > 1.0) { T = -C.y; }
            if (vB.y < 0.0) { B = -C.y; }

            float div = 0.5 * (R - L + T - B);
            gl_FragColor = vec4(div, 0.0, 0.0, 1.0);
        }
    `);

    const curlShader = compileShader(gl.FRAGMENT_SHADER, `
        precision mediump float;
        precision mediump sampler2D;

        varying highp vec2 vUv;
        varying highp vec2 vL;
        varying highp vec2 vR;
        varying highp vec2 vT;
        varying highp vec2 vB;
        uniform sampler2D uVelocity;

        void main () {
            float L = texture2D(uVelocity, vL).y;
            float R = texture2D(uVelocity, vR).y;
            float T = texture2D(uVelocity, vT).x;
            float B = texture2D(uVelocity, vB).x;
            float vorticity = R - L - T + B;
            gl_FragColor = vec4(0.5 * vorticity, 0.0, 0.0, 1.0);
        }
    `);

    const vorticityShader = compileShader(gl.FRAGMENT_SHADER, `
        precision highp float;
        precision highp sampler2D;

        varying vec2 vUv;
        varying vec2 vL;
        varying vec2 vR;
        varying vec2 vT;
        varying vec2 vB;
        uniform sampler2D uVelocity;
        uniform sampler2D uCurl;
        uniform float curl;
        uniform float dt;

        void main () {
            float L = texture2D(uCurl, vL).x;
            float R = texture2D(uCurl, vR).x;
            float T = texture2D(uCurl, vT).x;
            float B = texture2D(uCurl, vB).x;
            float C = texture2D(uCurl, vUv).x;

            vec2 force = 0.5 * vec2(abs(T) - abs(B), abs(R) - abs(L));
            force /= length(force) + 0.0001;
            force *= curl * C;
            force.y *= -1.0;

            vec2 velocity = texture2D(uVelocity, vUv).xy;
            velocity += force * dt;
            velocity = min(max(velocity, -1000.0), 1000.0);
            gl_FragColor = vec4(velocity, 0.0, 1.0);
        }
    `);

    const pressureShader = compileShader(gl.FRAGMENT_SHADER, `
        precision mediump float;
        precision mediump sampler2D;

        varying highp vec2 vUv;
        varying highp vec2 vL;
        varying highp vec2 vR;
        varying highp vec2 vT;
        varying highp vec2 vB;
        uniform sampler2D uPressure;
        uniform sampler2D uDivergence;

        void main () {
            float L = texture2D(uPressure, vL).x;
            float R = texture2D(uPressure, vR).x;
            float T = texture2D(uPressure, vT).x;
            float B = texture2D(uPressure, vB).x;
            float C = texture2D(uPressure, vUv).x;
            float divergence = texture2D(uDivergence, vUv).x;
            float pressure = (L + R + B + T - divergence) * 0.25;
            gl_FragColor = vec4(pressure, 0.0, 0.0, 1.0);
        }
    `);

    const gradientSubtractShader = compileShader(gl.FRAGMENT_SHADER, `
        precision mediump float;
        precision mediump sampler2D;

        varying highp vec2 vUv;
        varying highp vec2 vL;
        varying highp vec2 vR;
        varying highp vec2 vT;
        varying highp vec2 vB;
        uniform sampler2D uPressure;
        uniform sampler2D uVelocity;

        void main () {
            float L = texture2D(uPressure, vL).x;
            float R = texture2D(uPressure, vR).x;
            float T = texture2D(uPressure, vT).x;
            float B = texture2D(uPressure, vB).x;
            vec2 velocity = texture2D(uVelocity, vUv).xy;
            velocity.xy -= vec2(R - L, T - B);
            gl_FragColor = vec4(velocity, 0.0, 1.0);
        }
    `);

    const blit = (() => {
        gl.bindBuffer(gl.ARRAY_BUFFER, gl.createBuffer());
        gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, -1, 1, 1, 1, 1, -1]), gl.STATIC_DRAW);
        gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, gl.createBuffer());
        gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, new Uint16Array([0, 1, 2, 0, 2, 3]), gl.STATIC_DRAW);
        gl.vertexAttribPointer(0, 2, gl.FLOAT, false, 0, 0);
        gl.enableVertexAttribArray(0);

        return (target, clear = false) => {
            if (target == null)
            {
                gl.viewport(0, 0, gl.drawingBufferWidth, gl.drawingBufferHeight);
                gl.bindFramebuffer(gl.FRAMEBUFFER, null);
            }
            else
            {
                gl.viewport(0, 0, target.width, target.height);
                gl.bindFramebuffer(gl.FRAMEBUFFER, target.fbo);
            }
            if (clear)
            {
                gl.clearColor(0.0, 0.0, 0.0, 1.0);
                gl.clear(gl.COLOR_BUFFER_BIT);
            }
            // CHECK_FRAMEBUFFER_STATUS();
            gl.drawElements(gl.TRIANGLES, 6, gl.UNSIGNED_SHORT, 0);
        }
    })();

    let dye;
    let velocity;
    let divergence;
    let curl;
    let pressure;

    const copyProgram            = new Program(baseVertexShader, copyShader);
    const clearProgram           = new Program(baseVertexShader, clearShader);
    const splatProgram           = new Program(baseVertexShader, splatShader);
    const advectionProgram       = new Program(baseVertexShader, advectionShader);
    const divergenceProgram      = new Program(baseVertexShader, divergenceShader);
    const curlProgram            = new Program(baseVertexShader, curlShader);
    const vorticityProgram       = new Program(baseVertexShader, vorticityShader);
    const pressureProgram        = new Program(baseVertexShader, pressureShader);
    const gradienSubtractProgram = new Program(baseVertexShader, gradientSubtractShader);

    const displayMaterial = new Material(baseVertexShader, DISPLAY_SHADER);
    displayMaterial.setKeywords([]);

    const paper = makeFiberTexture(gl, opts.paperUrl);

    function initFramebuffers () {
        let simRes = getResolution(config.SIM_RESOLUTION);
        let dyeRes = getResolution(config.DYE_RESOLUTION);

        const texType = ext.halfFloatTexType;
        const rgba    = ext.formatRGBA;
        const rg      = ext.formatRG;
        const r       = ext.formatR;
        const filtering = ext.supportLinearFiltering ? gl.LINEAR : gl.NEAREST;

        gl.disable(gl.BLEND);

        if (dye == null)
            dye = createDoubleFBO(dyeRes.width, dyeRes.height, rgba.internalFormat, rgba.format, texType, filtering);
        else
            dye = resizeDoubleFBO(dye, dyeRes.width, dyeRes.height, rgba.internalFormat, rgba.format, texType, filtering);

        if (velocity == null)
            velocity = createDoubleFBO(simRes.width, simRes.height, rg.internalFormat, rg.format, texType, filtering);
        else
            velocity = resizeDoubleFBO(velocity, simRes.width, simRes.height, rg.internalFormat, rg.format, texType, filtering);

        divergence = createFBO      (simRes.width, simRes.height, r.internalFormat, r.format, texType, gl.NEAREST);
        curl       = createFBO      (simRes.width, simRes.height, r.internalFormat, r.format, texType, gl.NEAREST);
        pressure   = createDoubleFBO(simRes.width, simRes.height, r.internalFormat, r.format, texType, gl.NEAREST);

    }

    function createFBO (w, h, internalFormat, format, type, param) {
        gl.activeTexture(gl.TEXTURE0);
        let texture = gl.createTexture();
        gl.bindTexture(gl.TEXTURE_2D, texture);
        gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, param);
        gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, param);
        gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE);
        gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);
        gl.texImage2D(gl.TEXTURE_2D, 0, internalFormat, w, h, 0, format, type, null);

        let fbo = gl.createFramebuffer();
        gl.bindFramebuffer(gl.FRAMEBUFFER, fbo);
        gl.framebufferTexture2D(gl.FRAMEBUFFER, gl.COLOR_ATTACHMENT0, gl.TEXTURE_2D, texture, 0);
        gl.viewport(0, 0, w, h);
        gl.clear(gl.COLOR_BUFFER_BIT);

        let texelSizeX = 1.0 / w;
        let texelSizeY = 1.0 / h;

        return {
            texture,
            fbo,
            width: w,
            height: h,
            texelSizeX,
            texelSizeY,
            attach (id) {
                gl.activeTexture(gl.TEXTURE0 + id);
                gl.bindTexture(gl.TEXTURE_2D, texture);
                return id;
            }
        };
    }

    function createDoubleFBO (w, h, internalFormat, format, type, param) {
        let fbo1 = createFBO(w, h, internalFormat, format, type, param);
        let fbo2 = createFBO(w, h, internalFormat, format, type, param);

        return {
            width: w,
            height: h,
            texelSizeX: fbo1.texelSizeX,
            texelSizeY: fbo1.texelSizeY,
            get read () {
                return fbo1;
            },
            set read (value) {
                fbo1 = value;
            },
            get write () {
                return fbo2;
            },
            set write (value) {
                fbo2 = value;
            },
            swap () {
                let temp = fbo1;
                fbo1 = fbo2;
                fbo2 = temp;
            }
        }
    }

    function resizeFBO (target, w, h, internalFormat, format, type, param) {
        let newFBO = createFBO(w, h, internalFormat, format, type, param);
        copyProgram.bind();
        gl.uniform1i(copyProgram.uniforms.uTexture, target.attach(0));
        blit(newFBO);
        return newFBO;
    }

    function resizeDoubleFBO (target, w, h, internalFormat, format, type, param) {
        if (target.width == w && target.height == h)
            return target;
        target.read = resizeFBO(target.read, w, h, internalFormat, format, type, param);
        target.write = createFBO(w, h, internalFormat, format, type, param);
        target.width = w;
        target.height = h;
        target.texelSizeX = 1.0 / w;
        target.texelSizeY = 1.0 / h;
        return target;
    }

    function step (dt) {
        gl.disable(gl.BLEND);

        curlProgram.bind();
        gl.uniform2f(curlProgram.uniforms.texelSize, velocity.texelSizeX, velocity.texelSizeY);
        gl.uniform1i(curlProgram.uniforms.uVelocity, velocity.read.attach(0));
        blit(curl);

        vorticityProgram.bind();
        gl.uniform2f(vorticityProgram.uniforms.texelSize, velocity.texelSizeX, velocity.texelSizeY);
        gl.uniform1i(vorticityProgram.uniforms.uVelocity, velocity.read.attach(0));
        gl.uniform1i(vorticityProgram.uniforms.uCurl, curl.attach(1));
        gl.uniform1f(vorticityProgram.uniforms.curl, config.CURL);
        gl.uniform1f(vorticityProgram.uniforms.dt, dt);
        blit(velocity.write);
        velocity.swap();

        divergenceProgram.bind();
        gl.uniform2f(divergenceProgram.uniforms.texelSize, velocity.texelSizeX, velocity.texelSizeY);
        gl.uniform1i(divergenceProgram.uniforms.uVelocity, velocity.read.attach(0));
        blit(divergence);

        clearProgram.bind();
        gl.uniform1i(clearProgram.uniforms.uTexture, pressure.read.attach(0));
        gl.uniform1f(clearProgram.uniforms.value, config.PRESSURE);
        blit(pressure.write);
        pressure.swap();

        pressureProgram.bind();
        gl.uniform2f(pressureProgram.uniforms.texelSize, velocity.texelSizeX, velocity.texelSizeY);
        gl.uniform1i(pressureProgram.uniforms.uDivergence, divergence.attach(0));
        for (let i = 0; i < config.PRESSURE_ITERATIONS; i++) {
            gl.uniform1i(pressureProgram.uniforms.uPressure, pressure.read.attach(1));
            blit(pressure.write);
            pressure.swap();
        }

        gradienSubtractProgram.bind();
        gl.uniform2f(gradienSubtractProgram.uniforms.texelSize, velocity.texelSizeX, velocity.texelSizeY);
        gl.uniform1i(gradienSubtractProgram.uniforms.uPressure, pressure.read.attach(0));
        gl.uniform1i(gradienSubtractProgram.uniforms.uVelocity, velocity.read.attach(1));
        blit(velocity.write);
        velocity.swap();

        advectionProgram.bind();
        gl.uniform2f(advectionProgram.uniforms.texelSize, velocity.texelSizeX, velocity.texelSizeY);
        if (!ext.supportLinearFiltering)
            gl.uniform2f(advectionProgram.uniforms.dyeTexelSize, velocity.texelSizeX, velocity.texelSizeY);
        let velocityId = velocity.read.attach(0);
        gl.uniform1i(advectionProgram.uniforms.uVelocity, velocityId);
        gl.uniform1i(advectionProgram.uniforms.uSource, velocityId);
        gl.uniform1f(advectionProgram.uniforms.dt, dt);
        gl.uniform1f(advectionProgram.uniforms.dissipation, config.VELOCITY_DISSIPATION);
        blit(velocity.write);
        velocity.swap();

        if (!ext.supportLinearFiltering)
            gl.uniform2f(advectionProgram.uniforms.dyeTexelSize, dye.texelSizeX, dye.texelSizeY);
        gl.uniform1i(advectionProgram.uniforms.uVelocity, velocity.read.attach(0));
        gl.uniform1i(advectionProgram.uniforms.uSource, dye.read.attach(1));
        gl.uniform1f(advectionProgram.uniforms.dissipation, config.DENSITY_DISSIPATION);
        blit(dye.write);
        dye.swap();
    }

    function correctRadius (radius) {
        let aspectRatio = canvas.width / canvas.height;
        if (aspectRatio > 1)
            radius *= aspectRatio;
        return radius;
    }

    function getResolution (resolution) {
        let aspectRatio = gl.drawingBufferWidth / gl.drawingBufferHeight;
        if (aspectRatio < 1)
            aspectRatio = 1.0 / aspectRatio;

        let min = Math.round(resolution);
        let max = Math.round(resolution * aspectRatio);

        if (gl.drawingBufferWidth > gl.drawingBufferHeight)
            return { width: max, height: min };
        else
            return { width: min, height: max };
    }

    function getTextureScale (texture, width, height) {
        return {
            x: width / texture.width,
            y: height / texture.height
        };
    }

    function hashCode (s) {
        if (s.length == 0) return 0;
        let hash = 0;
        for (let i = 0; i < s.length; i++) {
            hash = (hash << 5) - hash + s.charCodeAt(i);
            hash |= 0; // Convert to 32bit integer
        }
        return hash;
    };

    initFramebuffers();

    // ---------- 画布尺寸（限制 DPR，避免 3× 屏过大）----------
    function scaleByPixelRatio (input) {
        const pixelRatio = Math.min(window.devicePixelRatio || 1, maxDpr);
        return Math.floor(input * pixelRatio);
    }

    function resizeCanvas () {
        const width = Math.max(2, scaleByPixelRatio(canvas.clientWidth));
        const height = Math.max(2, scaleByPixelRatio(canvas.clientHeight));
        if (canvas.width !== width || canvas.height !== height) {
            canvas.width = width;
            canvas.height = height;
            return true;
        }
        return false;
    }

    // ---------- 注入 ----------
    // 注意：半透明预乘混合在 render() 里开启，任何写 FBO 的操作前必须关闭
    function splat (x, y, dx, dy, color, radius) {
        gl.disable(gl.BLEND);
        splatProgram.bind();
        gl.uniform1i(splatProgram.uniforms.uTarget, velocity.read.attach(0));
        gl.uniform1f(splatProgram.uniforms.aspectRatio, canvas.width / canvas.height);
        gl.uniform2f(splatProgram.uniforms.point, x, y);
        gl.uniform3f(splatProgram.uniforms.color, dx, dy, 0.0);
        gl.uniform1f(splatProgram.uniforms.radius, correctRadius(radius / 100.0));
        blit(velocity.write);
        velocity.swap();

        gl.uniform1i(splatProgram.uniforms.uTarget, dye.read.attach(0));
        gl.uniform3f(splatProgram.uniforms.color, color.r, color.g, color.b);
        blit(dye.write);
        dye.swap();
    }

    // ---------- 渲染 ----------
    let strokeTexture = null;
    let strokeBox = [0, 0, 1, 1];

    function setStrokeLayer(surface, box) {
        if (destroyed) return;
        if (!surface) {
            if (strokeTexture) gl.deleteTexture(strokeTexture);
            strokeTexture = null;
            return;
        }
        strokeBox = box;
        gl.activeTexture(gl.TEXTURE2);
        if (!strokeTexture) {
            strokeTexture = gl.createTexture();
            gl.bindTexture(gl.TEXTURE_2D, strokeTexture);
            gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR);
            gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR);
            gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE);
            gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);
            gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA, gl.RGBA, gl.UNSIGNED_BYTE, surface);
        } else {
            gl.bindTexture(gl.TEXTURE_2D, strokeTexture);
            gl.texSubImage2D(gl.TEXTURE_2D, 0, 0, 0, gl.RGBA, gl.UNSIGNED_BYTE, surface);
        }
    }

    function drawDisplay () {
        const width = gl.drawingBufferWidth;
        const height = gl.drawingBufferHeight;
        const u = displayMaterial.uniforms;

        displayMaterial.bind();
        gl.uniform1i(u.uTexture, dye.read.attach(0));
        gl.uniform1i(u.uPaperTex, paper.attach(1));
        gl.activeTexture(gl.TEXTURE2);
        gl.bindTexture(gl.TEXTURE_2D, strokeTexture || paper.texture);
        gl.uniform1i(u.uStrokeTex, strokeTexture ? 2 : 1);
        gl.uniform1f(u.uStrokeEnabled, strokeTexture ? 1 : 0);
        gl.uniform4fv(u.uStrokeBox, strokeBox);
        const scale = getTextureScale(paper, width, height);
        gl.uniform2f(u.uPaperScale, scale.x, scale.y);
        gl.uniform1f(u.uSoft, config.SOFT);
        gl.uniform1f(u.uGrain, config.GRAIN);
        gl.uniform1f(u.uHalo, config.HALO);
        gl.uniform3fv(u.uInk, paletteRgb.ink);
        gl.uniform3fv(u.uRed, paletteRgb.red);
        gl.uniform3fv(u.uCream, paletteRgb.cream);
        blit(null);
    }

    function render () {
        gl.bindFramebuffer(gl.FRAMEBUFFER, null);
        gl.viewport(0, 0, gl.drawingBufferWidth, gl.drawingBufferHeight);
        gl.disable(gl.BLEND);
        gl.clearColor(0, 0, 0, 0);
        gl.clear(gl.COLOR_BUFFER_BIT);
        gl.blendFunc(gl.ONE, gl.ONE_MINUS_SRC_ALPHA);
        gl.enable(gl.BLEND);
        drawDisplay();
    }

    // ---------- 主循环（可停止）+ 帧率探测 ----------
    const slowFps = opts.slowFps != null ? opts.slowFps : 45;
    const probeFrames = opts.probeFrames != null ? opts.probeFrames : 30;
    let probeSkip = 6;               // 跳过前几帧（着色器编译、首次布局）
    let probeN = 0;
    let probeSum = 0;
    let probeDone = typeof opts.onSlow !== 'function';
    let lastTs = 0;

    function frame (ts) {
        if (!running) return;
        raf = requestAnimationFrame(frame);

        const real = lastTs ? (ts - lastTs) / 1000 : 1 / 60;
        lastTs = ts;

        if (!probeDone) {
            if (probeSkip > 0) {
                probeSkip--;
            } else {
                probeSum += Math.min(real, 0.1);   // 切后台造成的大间隔不计入
                probeN++;
                if (probeN >= probeFrames) {
                    probeDone = true;
                    const fps = probeN / probeSum;
                    if (fps < slowFps) {
                        opts.onSlow(fps);
                        if (!running) return;      // 回调里可能已 destroy
                    }
                }
            }
        }

        const dt = Math.min(real, 0.016666);       // 与原版一致，见方案 §7.2
        if (resizeCanvas()) initFramebuffers();
        step(dt);
        render();
    }

    function start () {
        if (destroyed || running) return;
        running = true;
        lastTs = 0;
        raf = requestAnimationFrame(frame);
    }

    function stop () {
        running = false;
        if (raf) cancelAnimationFrame(raf);
        raf = 0;
    }

    const onContextLost = (e) => {
        e.preventDefault();
        stop();
        if (typeof opts.onLost === 'function') opts.onLost();
    };
    canvas.addEventListener('webglcontextlost', onContextLost, false);

    // ---------- 对外 API ----------
    function pigmentColor (pigment, amount) {
        const ch = PIGMENT_CHANNEL[pigment] || 'r';
        const c = { r: 0, g: 0, b: 0 };
        c[ch] = amount;
        return c;
    }

    // 单点滴墨。amount≈2–5 为浓墨；dx/dy 为初速度（CSS 方向）
    function ink (x, y, o = {}) {
        if (destroyed) return;
        const pigment = o.pigment || 'ink';
        const amount = o.amount != null ? o.amount : 3;
        const radius = o.radius != null ? o.radius : config.SPLAT_RADIUS;
        const dx = o.dx || 0;
        const dy = o.dy || 0;
        splat(x, 1 - y, dx, -dy, pigmentColor(pigment, amount), radius);
    }

    // 沿折线落笔。points 为 CSS 归一化坐标 [[x,y],...]；返回 { to(p), reset() }
    function brush (points, o = {}) {
        const pigment = o.pigment || 'ink';
        const amount = o.amount != null ? o.amount : 3.5;     // 硬边阈值下，低浓度的细线会很快消失
        const radius = o.radius != null ? o.radius : 0.03;
        const spacing = o.spacing != null ? o.spacing : 0.006;   // 以画布高度为单位
        const speed = o.speed != null ? o.speed : 30;            // 相邻落点的速度会叠加，不宜大

        const aspect = canvas.clientWidth / Math.max(1, canvas.clientHeight);
        const cum = [0];
        for (let i = 1; i < points.length; i++) {
            const ddx = (points[i][0] - points[i - 1][0]) * aspect;
            const ddy = points[i][1] - points[i - 1][1];
            cum.push(cum[i - 1] + Math.hypot(ddx, ddy));
        }
        const total = cum[cum.length - 1];
        let lastD = 0;

        function sample (d) {
            let i = 1;
            while (i < cum.length - 1 && cum[i] < d) i++;
            const seg = cum[i] - cum[i - 1] || 1e-9;
            const t = clamp01((d - cum[i - 1]) / seg);
            const a = points[i - 1], b = points[i];
            const tx = (b[0] - a[0]) * aspect, ty = b[1] - a[1];
            const tl = Math.hypot(tx, ty) || 1;
            return { x: a[0] + (b[0] - a[0]) * t, y: a[1] + (b[1] - a[1]) * t, tx: tx / tl, ty: ty / tl };
        }

        return {
            to (p) {
                if (destroyed || total <= 0 || points.length < 2) return;
                const target = clamp01(p) * total;
                while (lastD + spacing <= target) {
                    lastD += spacing;
                    const s = sample(lastD);
                    ink(s.x, s.y, { pigment, amount, radius, dx: s.tx * speed, dy: s.ty * speed });
                }
                if (p >= 1) lastD = Math.max(lastD, target);
            },
            reset () { lastD = 0; }
        };
    }

    // 从 SVG <path> 采样（经 getScreenCTM 映射到画布，不受 viewBox / preserveAspectRatio / 变换影响）
    // 请在布局稳定后调用；之后若 path 被位移或缩放，需要重新创建。
    function brushFromPath (pathEl, o = {}) {
        const svg = pathEl.ownerSVGElement;
        const m = pathEl.getScreenCTM();
        const rect = canvas.getBoundingClientRect();
        const len = pathEl.getTotalLength();
        const samples = o.samples || 160;
        const pt = svg.createSVGPoint();
        const pts = [];
        for (let i = 0; i <= samples; i++) {
            const p = pathEl.getPointAtLength(len * i / samples);
            pt.x = p.x; pt.y = p.y;
            const c = pt.matrixTransform(m);
            pts.push([(c.x - rect.left) / rect.width, (c.y - rect.top) / rect.height]);
        }
        return brush(pts, o);
    }

    function clear () {
        if (destroyed) return;
        gl.disable(gl.BLEND);
        clearProgram.bind();
        gl.uniform1f(clearProgram.uniforms.value, 0.0);
        gl.uniform1i(clearProgram.uniforms.uTexture, dye.read.attach(0));
        blit(dye.write);
        dye.swap();
        gl.uniform1i(clearProgram.uniforms.uTexture, velocity.read.attach(0));
        blit(velocity.write);
        velocity.swap();
    }

    function set (o = {}) {
        if (destroyed) return;
        if (o.soft != null) config.SOFT = Math.max(0.02, o.soft);
        if (o.grain != null) config.GRAIN = o.grain;
        if (o.halo != null) config.HALO = o.halo;
        if (o.densityDissipation != null) config.DENSITY_DISSIPATION = o.densityDissipation;
        if (o.velocityDissipation != null) config.VELOCITY_DISSIPATION = o.velocityDissipation;
        if (o.curl != null) config.CURL = o.curl;
        if (o.radius != null) config.SPLAT_RADIUS = o.radius;
        if (o.palette) { Object.assign(palette, o.palette); refreshPalette(); }
    }

    function getParams () {
        return {
            soft: config.SOFT,
            grain: config.GRAIN,
            halo: config.HALO,
            densityDissipation: config.DENSITY_DISSIPATION,
            velocityDissipation: config.VELOCITY_DISSIPATION,
            curl: config.CURL,
            radius: config.SPLAT_RADIUS,
            palette: Object.assign({}, palette),
        };
    }

    // 幂等：React StrictMode 下可能被调用两次
    function destroy () {
        if (destroyed) return;
        setStrokeLayer(null);
        destroyed = true;
        stop();
        canvas.removeEventListener('webglcontextlost', onContextLost, false);
        const lose = gl.getExtension('WEBGL_lose_context');
        if (lose) lose.loseContext();
    }

    start();

    return {
        ink,
        brush,
        brushFromPath,
        setStrokeLayer,
        clear,
        set,
        getParams,
        pause: stop,
        resume: start,
        destroy,
        get running () { return running; },
        get destroyed () { return destroyed; },
        // flood(): 满屏墨涌转场，见方案 §11.1，v1 不实现
    };
}
