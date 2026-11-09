import { createInk } from './createInk';
import markup from './stage.html?raw';
import css from './stage.css?raw';
const STROKE_DATA = {"stage": [1440, 600], "glyphs": [{"i": 0, "bbox": [184.9, 224.3, 210.1, 179.5], "strokes": [[[280.0, 239.5, 11.0], [283.5, 250.0, 14.0], [282.5, 355.5, 20.5], [279.5, 363.0, 23.0], [282.0, 356.0, 20.5]], [[209.5, 335.0, 11.0], [212.0, 315.0, 10.5]], [[201.0, 373.5, 16.0], [206.5, 346.5, 13.0]], [[202.0, 374.5, 17.0], [229.0, 369.0, 10.0]], [[269.5, 365.5, 17.5], [264.0, 363.5, 11.0], [246.5, 363.5, 10.5], [230.0, 368.5, 10.0], [245.5, 364.0, 10.5], [235.5, 340.0, 3.5]], [[359.0, 362.5, 19.5], [285.0, 358.5, 22.0]], [[365.0, 365.5, 26.0], [366.5, 366.5, 24.0], [365.5, 376.5, 18.0], [367.0, 368.5, 23.0], [369.0, 331.0, 15.0], [373.0, 345.0, 19.0], [368.5, 365.0, 22.5]], [[275.5, 383.0, 14.0], [274.5, 368.5, 22.5], [277.0, 366.0, 22.5]]]}, {"i": 1, "bbox": [470.8, 186.2, 218.4, 241.7], "strokes": [[[583.0, 193.5, 4.0], [585.5, 206.5, 10.0], [580.0, 218.0, 10.0], [578.0, 229.0, 9.5], [570.0, 233.5, 8.0], [577.5, 229.5, 9.0]], [[529.0, 220.5, 11.5], [526.0, 217.5, 9.5]], [[563.0, 243.5, 7.0], [565.0, 241.0, 7.5]], [[568.5, 236.0, 8.0], [567.0, 237.5, 7.5]], [[581.0, 232.5, 9.0], [586.5, 233.5, 8.0]], [[633.5, 227.5, 8.5], [595.0, 233.0, 7.5]], [[478.5, 280.0, 7.5], [478.5, 280.0, 7.5]], [[484.5, 284.0, 10.0], [486.0, 285.0, 10.5]], [[536.5, 277.5, 2.0], [532.0, 283.0, 1.0]], [[542.5, 270.5, 3.5], [541.0, 272.0, 3.0]], [[544.5, 267.5, 3.5], [548.5, 263.0, 5.0]], [[550.5, 260.0, 4.5], [552.0, 258.5, 5.5]], [[560.0, 248.0, 6.5], [558.5, 249.5, 6.0]], [[587.5, 264.0, 4.5], [624.5, 263.0, 7.0], [620.5, 261.0, 5.5], [590.0, 263.0, 5.0]], [[518.5, 333.5, 2.5], [515.0, 339.0, 3.0]], [[558.5, 317.5, 9.5], [539.0, 319.5, 6.5], [521.5, 328.5, 2.5], [523.5, 326.0, 3.5], [534.5, 321.5, 7.5]], [[559.0, 318.0, 10.5], [557.5, 331.0, 6.5], [549.5, 346.0, 7.5], [544.5, 361.0, 12.5], [549.0, 347.0, 7.5]], [[565.5, 314.0, 10.5], [568.0, 298.5, 6.0], [565.5, 314.5, 10.0], [560.5, 316.5, 10.5], [592.5, 310.5, 7.0]], [[568.5, 297.5, 6.0], [570.5, 276.5, 2.0], [571.5, 286.0, 5.5], [570.0, 293.0, 5.5]], [[578.5, 332.5, 6.0], [578.5, 332.5, 6.0]], [[599.0, 307.0, 7.0], [598.5, 292.5, 9.0], [596.5, 288.5, 9.0]], [[621.5, 309.5, 12.5], [601.5, 309.5, 6.5]], [[631.5, 308.0, 15.0], [678.0, 308.5, 9.5]], [[504.5, 356.0, 6.0], [505.5, 354.5, 5.5]], [[509.5, 348.0, 4.5], [508.0, 350.0, 5.0]], [[542.5, 375.0, 6.0], [542.0, 363.5, 10.0]], [[585.5, 338.0, 8.5], [585.5, 353.5, 9.5]], [[610.0, 358.0, 12.5], [588.5, 357.5, 8.0], [545.0, 362.0, 13.0], [588.0, 357.5, 8.0]], [[614.5, 362.5, 17.5], [611.5, 379.5, 14.5], [602.0, 397.0, 16.0]], [[618.0, 359.5, 21.5], [616.0, 361.0, 20.5]], [[622.0, 355.5, 21.5], [628.0, 357.5, 13.5], [642.0, 357.5, 10.0], [622.0, 355.0, 21.5], [625.5, 313.5, 14.5], [629.0, 305.5, 16.0], [632.0, 277.0, 11.0], [628.5, 268.5, 8.5]], [[496.5, 385.5, 12.5], [493.5, 376.0, 10.0], [502.0, 360.0, 6.5]], [[559.5, 408.0, 3.5], [581.0, 413.0, 12.0], [587.5, 412.0, 15.0], [595.5, 405.0, 16.5], [591.5, 409.0, 16.0]]]}, {"i": 2, "bbox": [768.8, 202.7, 190.5, 220.6], "strokes": [[[828.5, 213.0, 4.5], [845.5, 209.0, 4.5], [870.5, 208.5, 5.5]], [[835.5, 245.0, 7.0], [870.0, 240.5, 18.0]], [[879.0, 220.5, 14.0], [877.0, 231.0, 15.5]], [[831.5, 281.0, 7.0], [838.0, 278.5, 8.0]], [[848.0, 275.0, 8.5], [867.5, 271.5, 10.0], [871.5, 269.0, 11.5], [872.5, 243.5, 16.5], [875.5, 237.5, 15.5], [873.0, 243.0, 16.0]], [[867.0, 285.0, 3.5], [867.0, 272.0, 10.0]], [[818.0, 321.5, 7.0], [799.5, 324.5, 7.5], [783.5, 330.0, 8.5]], [[826.0, 320.0, 7.5], [858.5, 315.0, 8.5], [939.0, 310.5, 10.5], [880.0, 311.5, 15.0], [874.0, 314.0, 19.5], [868.0, 287.5, 5.5], [873.5, 313.5, 20.5], [874.0, 370.0, 12.0], [871.5, 385.0, 13.0], [866.5, 395.0, 15.0]], [[819.5, 388.5, 1.0], [821.5, 390.0, 2.0]], [[828.5, 395.0, 4.5], [824.0, 392.0, 3.5]], [[832.0, 397.0, 5.5], [853.5, 405.5, 13.5], [859.5, 403.5, 17.0]]]}, {"i": 3, "bbox": [1036.3, 204.5, 213.4, 211.0], "strokes": [[[1065.0, 235.5, 8.5], [1066.0, 248.5, 5.5], [1074.0, 266.5, 6.0]], [[1073.0, 230.0, 7.5], [1077.5, 228.0, 7.0]], [[1113.0, 225.0, 7.0], [1097.0, 224.0, 6.5], [1078.5, 227.5, 7.0], [1091.5, 225.0, 6.0]], [[1115.0, 228.0, 10.0], [1117.0, 233.0, 9.5], [1111.0, 250.0, 10.5]], [[1177.0, 234.0, 9.0], [1182.5, 236.5, 6.0], [1208.5, 240.5, 6.0]], [[1079.0, 272.0, 8.0], [1091.5, 269.5, 7.0]], [[1107.5, 260.5, 11.0], [1101.0, 265.0, 8.5]], [[1137.0, 255.0, 10.5], [1134.0, 265.0, 10.0], [1133.0, 284.0, 5.5], [1133.5, 268.0, 10.0]], [[1139.0, 251.5, 11.5], [1144.0, 246.5, 9.0], [1170.5, 237.0, 7.5], [1175.0, 233.0, 10.5], [1170.0, 216.0, 7.5]], [[1164.5, 288.0, 8.0], [1172.5, 285.5, 7.5], [1192.5, 284.0, 8.0]], [[1229.0, 253.0, 13.0], [1220.0, 261.5, 7.5]], [[1095.5, 318.0, 9.5], [1109.5, 315.5, 7.5]], [[1143.0, 327.0, 8.5], [1176.5, 319.5, 8.5], [1158.5, 321.5, 7.5], [1148.0, 325.0, 8.0]], [[1050.0, 380.5, 11.0], [1053.0, 378.0, 10.5]], [[1062.5, 372.0, 10.5], [1068.0, 364.5, 10.5], [1082.5, 360.5, 9.0], [1068.5, 364.0, 10.5]], [[1067.0, 362.5, 9.0], [1065.0, 314.5, 5.5]], [[1090.0, 357.5, 8.5], [1086.0, 359.5, 8.5]], [[1093.0, 355.0, 10.5], [1096.0, 349.0, 9.5], [1109.0, 346.0, 6.5], [1115.5, 342.5, 6.5]], [[1095.0, 349.0, 8.5], [1095.0, 318.5, 9.0], [1092.0, 294.5, 5.5], [1094.0, 316.5, 8.0]], [[1208.5, 359.0, 5.0], [1216.5, 362.5, 8.0]], [[1224.5, 367.0, 11.5], [1220.5, 364.5, 9.5]], [[1131.5, 386.0, 4.0], [1139.0, 361.5, 8.0]], [[1148.5, 385.0, 3.0], [1158.0, 389.0, 5.5]], [[1166.0, 393.5, 13.0], [1171.0, 393.5, 17.5]], [[1178.0, 384.0, 11.5], [1179.0, 341.5, 9.5], [1177.0, 319.5, 8.5], [1216.5, 316.5, 10.0]]]}]};
export function mountSplash(host, onDone) {
const root = host.shadowRoot || host.attachShadow({ mode: 'open' });
root.innerHTML = `<style>${css}</style>${markup}`;
let sparkRaf, fallbackTimer;
const viewport = root.getElementById('viewport');
const opening = root.getElementById('opening');
const stageInner = root.getElementById('stageInner');
const canvas = root.getElementById('ink');
const titleSvg = root.getElementById('titleSvg');
const ghostSvg = root.getElementById('ghostSvg');
const glyphEls = [...root.querySelectorAll('#titleSvg .glyph')];
const ghostEls = [...root.querySelectorAll('#ghostSvg .ghost-path')];
const seal = root.getElementById('seal');
const sealRing = root.getElementById('sealRing');
const edge = root.getElementById('edge');
const phaseEl = root.getElementById('phase');
const curModeBadge = root.getElementById('curModeBadge');

const Q = new URLSearchParams(location.search);
const num = (k, d) => (Q.has(k) ? Number(Q.get(k)) : d);

const GHOST = num('ghost', 0);
const cl01 = v => Math.min(1, Math.max(0, v));
const sstep = p => { const x = cl01(p); return x * x * (3 - 2 * x); };

/* 字稿叠加的可调项：?glyph=0.8 调淡、?glyph=0 关掉、?glyphat=0.55 提前显形 */
const GLYPH_OP = num('glyph', 1);
const GLYPH_AT = num('glyphat', 0.70);

/* ---------- 设计坐标系 ---------- */
const STAGE = { w: 1000, h: 1000 };
let PX = 1;               // 每个设计单位对应的 CSS 像素
let rep = null;
const NS = 'http://www.w3.org/2000/svg';

function syncStage() {
  const vw = viewport.clientWidth, vh = viewport.clientHeight;
  STAGE.w = 1000;
  STAGE.h = 1000 * vh / vw;
  PX = vw / STAGE.w;
  const vb = `0 0 ${STAGE.w} ${STAGE.h.toFixed(2)}`;
  titleSvg.setAttribute('viewBox', vb);
  ghostSvg.setAttribute('viewBox', vb);
  if (rep) rep.setAttribute('viewBox', vb);
}
const toCanvas = (x, y) => ({ x: x / STAGE.w, y: y / STAGE.h });

/* ---------- 原稿数据（不改动） ---------- */
const G = STROKE_DATA.glyphs.map(g => ({
  bbox: g.bbox.slice(),
  strokes: g.strokes.map(st => st.map(p => p.slice())),
}));

/* ---------- 额外图层 ---------- */
rep = document.createElementNS(NS, 'svg');
rep.id = 'repSvg';
rep.setAttribute('preserveAspectRatio', 'xMidYMid meet');
rep.setAttribute('aria-hidden', 'true');
ghostSvg.after(rep);

const clr = document.createElement('div');
clr.id = 'clear';
ghostSvg.after(clr);

const ORIG = new Map();
[...root.querySelectorAll('#titleSvg path'), ...root.querySelectorAll('#ghostSvg path')]
  .forEach(el => ORIG.set(el, el.getAttribute('transform')));

/* ---------- 参数 ---------- */
const P = {
  soft: num('soft', 0.30),
  grain: num('grain', 0.4),
  halo: num('halo', 0.02),
  curl: num('curl', 12),
  dens: num('dens', 0.02),
  vel: num('vel', 0.7),

  writeAmount: num('wa', 0.85),
  writeRedAmount: num('wra', 0.95),

  coverAmount: num('ca', 1.7),
  coverRadius: num('cr', 0.070),

  creamAmount: num('ma', 1.15),
  creamRadius: num('mr', 0.050),
};

const SLOW = num('slow', 1);
const RED_INK = '#c73a20';

const T = {
  writeStart: 0.35,
  perChar: 0.72,
  gap: 0.05,
  coverDelay: 1.0,
  coverDur: 0.9,
  diffuseWait: 1.0,
  creamDur: 0.55,
  creamGap: 0.18,
  panDur: 0.42,
  panStep: 0,
  panZoom: 0.0,
  wipeDur: 1.5,
};

const ink = createInk(canvas, {
  quality: 'low',
  palette: { ink: '#140d08', red: RED_INK, cream: '#e3bd82' },
  soft: P.soft, grain: P.grain, halo: P.halo,
});
ink && ink.set({ curl: P.curl, densityDissipation: P.dens, velocityDissipation: P.vel });

/* ---------- 笔画工具 ---------- */
const SPACING_INK = 1.45;   // px 级，绘制时按 PX 折算
const SPACING_RED = 1.15;
const PIGMENT = ['ink', 'ink', 'red', 'red'];

/* 笔头半径按“屏幕上的字高”折算：手机与桌面保持同样的相对粗细 */
const REF_H = Math.max(...G.map(g => g.bbox[3]));
function brushRadius(isRed) {
  const k = isRed ? 0.036 : 0.041;
  return k * REF_H * (LAY ? LAY.s : 1) / STAGE.h * num('wr', 1);
}

function dashes(stroke, spacingPx) {
  const sp = spacingPx / PX;
  const out = [];
  for (let i = 1; i < stroke.length; i++) {
    const [x0, y0, r0] = stroke[i - 1];
    const [x1, y1, r1] = stroke[i];
    const len = Math.hypot(x1 - x0, y1 - y0);
    const n = Math.max(1, Math.round(len / sp));
    for (let k = 0; k < n; k++) {
      const t = k / n;
      out.push({
        x: x0 + (x1 - x0) * t, y: y0 + (y1 - y0) * t,
        r: r0 + (r1 - r0) * t,
        dx: (x1 - x0) / (len || 1), dy: (y1 - y0) / (len || 1),
      });
    }
  }
  const last = stroke[stroke.length - 1];
  out.push({ x: last[0], y: last[1], r: last[2], dx: 0, dy: 0 });
  return out;
}

function orderStrokes(strokes) {
  const left = strokes.slice();
  left.sort((a, b) => (a[0][1] / 60) - (b[0][1] / 60) || a[0][0] - b[0][0]);
  if (!left.length) return [];
  const seq = [left.shift()];
  let end = seq[0][seq[0].length - 1];
  while (left.length) {
    let best = -1, bestD = Infinity, bestRev = false;
    left.forEach((s, i) => {
      const d0 = Math.hypot(s[0][0] - end[0], s[0][1] - end[1]);
      const d1 = Math.hypot(s[s.length - 1][0] - end[0], s[s.length - 1][1] - end[1]);
      if (d0 < bestD) { bestD = d0; best = i; bestRev = false; }
      if (d1 < bestD) { bestD = d1; best = i; bestRev = true; }
    });
    const s = bestRev ? left[best].slice().reverse() : left[best];
    seq.push(s);
    end = s[s.length - 1];
    left.splice(best, 1);
  }
  return seq;
}

/* ---------- 排版 ---------- */
let plan = [];
let LAY = null;

function buildLayout() {
  const W = STAGE.w, H = STAGE.h;
  const portrait = viewport.clientWidth / viewport.clientHeight < 1.05;

  const wR = Math.max(G[0].bbox[2], G[1].bbox[2]);   // 山海 列宽
  const wL = Math.max(G[2].bbox[2], G[3].bbox[2]);   // 寻踪 列宽
  const hR = G[0].bbox[3] + G[1].bbox[3];
  const hL = G[2].bbox[3] + G[3].bbox[3];

  const gapCol = (portrait ? 0.06 : 0.04) * W;
  const gapRow = 0.045 * H;

  let s;
  if (portrait) {
    s = Math.min(
      (0.43 * W - gapCol) / ((wR + wL) / 2),
      (0.38 * H - gapRow) / ((Math.max(G[0].bbox[3], G[2].bbox[3]) + Math.max(G[1].bbox[3], G[3].bbox[3])) / 2),
    );
  } else {
    s = Math.min(
      (0.86 * W - gapCol) / (wR + wL),
      (0.70 * H - gapRow) / Math.max(hR, hL),
    );
  }
  s = Math.max(0.2, s);

  const bwR = wR * s, bwL = wL * s;
  const blockW = bwR + bwL + gapCol;
  const x0 = (W - blockW) / 2;
  const xLeft = x0 + bwL / 2;
  const xRight = x0 + bwL + gapCol + bwR / 2;

  const cx = { 0: xRight, 1: xRight, 2: xLeft, 3: xLeft };
  const cy = {};

  if (portrait) {
    cy[0] = cy[2] = 0.31 * H;
    cy[1] = cy[3] = 0.69 * H;
  } else {
    let y = H / 2 - (hR * s + gapRow) / 2;
    cy[0] = y + G[0].bbox[3] * s / 2; y += G[0].bbox[3] * s + gapRow;
    cy[1] = y + G[1].bbox[3] * s / 2;
    y = H / 2 - (hL * s + gapRow) / 2;
    cy[2] = y + G[2].bbox[3] * s / 2; y += G[2].bbox[3] * s + gapRow;
    cy[3] = y + G[3].bbox[3] * s / 2;
  }

  LAY = { s, cx, cy, portrait };

  plan = G.map((g, i) => {
    const ox = g.bbox[0] + g.bbox[2] / 2;
    const oy = g.bbox[1] + g.bbox[3] / 2;
    const moved = g.strokes.map(st => st.map(([x, y, r]) => [
      cx[i] + (x - ox) * s,
      cy[i] + (y - oy) * s,
      r * s,
    ]));
    const strokes = orderStrokes(moved).map(st => dashes(st, i >= 2 ? SPACING_RED : SPACING_INK));
    let sumR = 0, nR = 0;
    strokes.forEach(st => st.forEach(q => { sumR += q.r; nR++; }));
    return {
      strokes,
      rRef: nR ? sumR / nR : 1,
      total: strokes.reduce((n, st) => n + st.length, 0),
      bbox: [cx[i] - g.bbox[2] * s / 2, cy[i] - g.bbox[3] * s / 2, g.bbox[2] * s, g.bbox[3] * s],
    };
  });

  applySvgTransforms();
  layoutSeal();
  updateRep();
}

function applySvgTransforms() {
  const { s, cx, cy } = LAY;
  const put = (el, i) => {
    const g = G[i];
    const ox = g.bbox[0] + g.bbox[2] / 2;
    const oy = g.bbox[1] + g.bbox[3] / 2;
    el.setAttribute('transform',
      `translate(${cx[i].toFixed(2)} ${cy[i].toFixed(2)}) scale(${s.toFixed(4)}) translate(${(-ox).toFixed(2)} ${(-oy).toFixed(2)}) ${ORIG.get(el)}`);
  };
  glyphEls.forEach((el, i) => put(el, i));
  ghostEls.forEach(el => put(el, Number(el.dataset.g)));
}

function focusOf(i) {
  const b = plan[i].bbox;
  return toCanvas(b[0] + b[2] / 2, b[1] + b[3] / 2);
}

function layoutSeal() {
  const b = plan[3].bbox;
  const vw = viewport.clientWidth, vh = viewport.clientHeight;
  const size = Math.max(38, Math.min(76, vw * 0.05));
  seal.classList.toggle('small', size < 58);
  const lb = toCanvas(b[0], b[1] + b[3]);
  const zx = lb.x * vw, zy = lb.y * vh;
  let x, y;
  if (LAY.portrait) {
    x = zx + size * 0.05;
    y = zy + size * 0.95;
  } else {
    x = zx - size * 0.90;
    y = zy - size * 0.60;
  }
  x = Math.min(Math.max(10, x), vw - size - 10);
  y = Math.min(Math.max(10, y), vh - size - 10);

  Object.assign(seal.style, {
    width: size + 'px', height: size + 'px',
    left: x + 'px', top: y + 'px',
  });
  Object.assign(sealRing.style, {
    width: size + 'px', height: size + 'px',
    left: (x + size / 2) + 'px', top: (y + size / 2) + 'px',
  });
  sealXY = { x: x + size / 2, y: y + size / 2 };

  const minX = Math.min(...plan.map(p => p.bbox[0])) - LAY.s * 46;
  const maxX = Math.max(...plan.map(p => p.bbox[0] + p.bbox[2])) + LAY.s * 46;
  const minY = Math.min(...plan.map(p => p.bbox[1])) - LAY.s * 40;
  const maxY = Math.max(...plan.map(p => p.bbox[1] + p.bbox[3])) + LAY.s * 40;
  const a = toCanvas(minX, minY), z = toCanvas(maxX, maxY);
  Object.assign(clr.style, {
    left: (a.x * vw) + 'px', top: (a.y * vh) + 'px',
    width: ((z.x - a.x) * vw) + 'px', height: ((z.y - a.y) * vh) + 'px',
  });
}

/* ---------- 题字重现层 ---------- */
let clearMode = 1;
let stylePolicy = 'wash';
if (Q.get('style') === 'invert') stylePolicy = 'invert';
else if (Q.get('style') === 'wash') stylePolicy = 'wash';

function applyRepStyle() {
  if (!rep) return;
  const btn = root.getElementById('styleBtn');
  const policyLabel = stylePolicy === 'random' ? '随机' : (stylePolicy === 'wash' ? '洗墨留白' : '泥金反白');
  if (btn) btn.textContent = '重现：' + policyLabel;
  if (curModeBadge) curModeBadge.textContent = '本轮：' + (clearMode ? '洗墨留白' : '泥金反白');

  rep.querySelectorAll('.glyph').forEach((g, i) => {
    g.style.opacity = '1';
    g.style.transition = 'none';
    g.style.filter = 'url(#inkEdge)';
    g.style.paintOrder = 'normal';
    if (clearMode) {
      g.style.fill = i < 2 ? '#140d08' : '#b8341a';
      g.style.stroke = 'none';
      g.style.strokeWidth = '0';
    } else {
      g.style.fill = i < 2 ? '#f7f0e0' : '#e8745a';
      g.style.stroke = 'rgba(201,164,92,.7)';
      g.style.strokeWidth = '0.7';
    }
  });
}

function updateRep() {
  if (!rep) return;
  rep.innerHTML = titleSvg.innerHTML;
  applyRepStyle();
}

function pickStyleForRun() {
  if (stylePolicy === 'random') clearMode = Math.random() < 0.5 ? 1 : 0;
  else clearMode = stylePolicy === 'wash' ? 1 : 0;
  applyRepStyle();
}

/* ---------- 扫墨 / 淡彩（均在设计坐标系的归一化空间） ---------- */
const COVER_STROKES = [
  [0.02, 0.13, 0.98, 0.23],
  [0.98, 0.38, 0.03, 0.47],
  [0.03, 0.63, 0.97, 0.73],
  [0.97, 0.82, 0.02, 0.91],
];
const coverBrushes = COVER_STROKES.map(([x0, y0, x1, y1], i) => {
  const pts = [];
  const bend = (i % 2 ? 1 : -1) * 0.008;
  for (let k = 0; k <= 14; k++) {
    const u = k / 14;
    pts.push([x0 + (x1 - x0) * u, y0 + (y1 - y0) * u + Math.sin(u * Math.PI) * bend]);
  }
  return pts;
});

const CREAM_STROKES = [
  { a: [-0.02, 0.20], c: [0.45, 0.06], b: [1.02, 0.30], r: 1.10, m: 0.80 },
  { a: [1.01, 0.46],  c: [0.62, 0.34], b: [0.18, 0.64], r: 0.95, m: 0.72 },
  { a: [0.04, 0.70],  c: [0.46, 0.92], b: [0.97, 0.72], r: 0.80, m: 0.62 },
  { a: [0.92, 0.90],  c: [0.65, 0.80], b: [0.32, 0.96], r: 0.58, m: 0.42 },
];
const creamPts = CREAM_STROKES.map(({ a, c, b }, i) => {
  const pts = [];
  for (let k = 0; k <= 16; k++) {
    const u = k / 16, v = 1 - u;
    pts.push([
      v * v * a[0] + 2 * v * u * c[0] + u * u * b[0],
      v * v * a[1] + 2 * v * u * c[1] + u * u * b[1] + Math.sin(u * Math.PI * 3 + i * 1.7) * 0.006,
    ]);
  }
  return pts;
});

function polyDashes(pts, spacingNorm) {
  const out = [];
  const seg = [];
  let total = 0;
  for (let i = 1; i < pts.length; i++) {
    const d = Math.hypot(pts[i][0] - pts[i - 1][0], pts[i][1] - pts[i - 1][1]);
    seg.push(d); total += d;
  }
  const n = Math.max(2, Math.round(total / spacingNorm));
  for (let k = 0; k <= n; k++) {
    let target = (k / n) * total;
    let i = 0;
    while (i < seg.length - 1 && target > seg[i]) { target -= seg[i]; i++; }
    const t = seg[i] ? target / seg[i] : 0;
    out.push({
      x: pts[i][0] + (pts[i + 1][0] - pts[i][0]) * t,
      y: pts[i][1] + (pts[i + 1][1] - pts[i][1]) * t,
      u: k / n,
    });
  }
  return out;
}

const COVER_DASH = coverBrushes.map(pts => polyDashes(pts, 0.008));
const CREAM_DASH = creamPts.map(pts => polyDashes(pts, 0.007));
const taperOf = u => Math.min(1, u / 0.10) * Math.min(1, (1 - u) / 0.12);

/* ---------- 时序 ---------- */
const charStarts = [];
{
  const USE_CAM = num('cam', 1) === 1;
  const CAM_MOVE = num('cammove', 0.40);
  const CAM_HOLD = 0.10;
  let t0 = T.writeStart;
  for (let i = 0; i < 4; i++) {
    const move = USE_CAM ? CAM_MOVE : (i ? T.gap : 0);
    charStarts.push({ camFrom: t0, writeFrom: t0 + move, writeTo: t0 + move + T.perChar });
    t0 = t0 + move + T.perChar + (USE_CAM ? CAM_HOLD : 0);
  }
}
const USE_CAM = num('cam', 1) === 1;
const CAM_ZOOM = num('camzoom', 1.24);
const CAM_BACK = 0.55;
const writeEnd = charStarts[3].writeTo;
const camBackFrom = writeEnd + 0.10;
const writeDone = camBackFrom + CAM_BACK;

const coverStart = writeDone + T.coverDelay;
const coverEnd = coverStart + T.coverDur;
const creamStart = coverEnd + T.diffuseWait;
const creamStep = T.creamDur + T.creamGap;
const creamEnd = creamStart + creamStep * (CREAM_STROKES.length - 1) + T.creamDur;

const repAt = creamEnd + 0.15;
const sealAt = repAt + num('repwait', 1.75);
const pushAt = sealAt + num('sealwait', 1.15);
const liftAt = pushAt + T.wipeDur + num('sealhold', 1.0);
const SEAL_LIFT = 1.3;

/* ---------- 状态 ---------- */
let raf = 0, startAt = 0, playing = false;
let state = null;
const easeIO = p => (p < 0.5 ? 2 * p * p : 1 - Math.pow(-2 * p + 2, 2) / 2);
const CENTER = { x: 0.5, y: 0.5, z: 1 };

function reset() {
  playing = false; cancelAnimationFrame(raf);
  glyphEls.forEach(g => { g.style.opacity = '0'; g.style.transition = ''; });
  titleSvg.style.zIndex = '2';
  ghostSvg.style.opacity = '0';
  rep.style.opacity = '0';
  mtn.style.opacity = '0';
  seal.classList.remove('on', 'lift');
  sealRing.classList.remove('boom');
  clr.style.opacity = '0'; edge.style.opacity = '0'; parts.length = 0;
  opening.classList.remove('wipe');
  canvas.style.zIndex = '1';
  phaseEl.textContent = '待开始';
  ink && ink.clear();
  ink && ink.set({ palette: { red: RED_INK } });
  state = {
    idx: plan.map(p => p.strokes.map(() => 0)),
    idxC: new Array(COVER_STROKES.length).fill(0),
    idxM: new Array(CREAM_STROKES.length).fill(0),
    writingInk: false, redInk: false, coverInk: false,
    creamCurl: false, sealed: false, lifted: false,
  };
  ink && ink.set({ curl: P.curl });
  stageInner.style.transform = '';
  root.getElementById('time').textContent = '0.00s';
}

function splat(d, pigment, amount, radius, rRef) {
  /* v11：用骨架半径做提按，粗笔更厚、细笔更薄；以本字均值为 1.0 */
  const f = Math.min(1.55, Math.max(0.55, 0.55 + 0.45 * (d.r / (rRef || 1))));
  const c = toCanvas(d.x, d.y);
  ink.ink(c.x, c.y, {
    pigment,
    amount: amount * (0.94 + 0.12 * f),
    radius: radius * f,
    dx: d.dx * 3, dy: d.dy * 3,
  });
}

function writeGlyph(gi, p) {
  const item = plan[gi];
  const pig = PIGMENT[gi];
  const isRed = gi >= 2;
  const amt = isRed ? P.writeRedAmount : P.writeAmount;
  const rad = brushRadius(isRed);
  let done = 0;
  item.strokes.forEach((list, si) => {
    const share = list.length / item.total;
    const localEnd = done + share;
    done = localEnd;
    const startIdx = state.idx[gi][si];
    if (p >= localEnd) {
      for (let i = startIdx; i < list.length; i++) splat(list[i], pig, amt, rad, item.rRef);
      state.idx[gi][si] = list.length;
    } else if (p > localEnd - share) {
      const target = Math.floor(list.length * ((p - (localEnd - share)) / share));
      for (let i = startIdx; i < target; i++) splat(list[i], pig, amt, rad, item.rRef);
      state.idx[gi][si] = Math.max(startIdx, target);
    }
  });
}

function runCover(p) {
  COVER_DASH.forEach((list, i) => {
    const local = Math.min(1, (p - i * 0.20) / 0.55);
    if (local <= 0) return;
    const from = state.idxC[i] || 0;
    const to = Math.floor(list.length * local);
    for (let k = from; k < to; k++) {
      const d = list[k];
      const tp = taperOf(d.u);
      ink.ink(d.x, d.y, {
        pigment: 'ink',
        amount: P.coverAmount * (0.35 + 0.65 * tp) * (0.85 + 0.3 * Math.sin(d.u * 15 + i)),
        radius: P.coverRadius * (0.55 + 0.45 * tp) * (0.88 + 0.24 * Math.sin(d.u * 11 + i * 2)),
        dx: 10, dy: 0,
      });
    }
    state.idxC[i] = Math.max(from, to);
  });
}

function runCream(t) {
  CREAM_DASH.forEach((list, i) => {
    const s = creamStart + i * creamStep;
    const local = Math.min(1, Math.max(0, (t - s) / T.creamDur));
    if (local <= 0) return;
    const from = state.idxM[i] || 0;
    const to = Math.floor(list.length * local);
    for (let k = from; k < to; k++) {
      const d = list[k];
      const tp = taperOf(d.u);
      ink.ink(d.x, d.y, {
        pigment: 'cream',
        amount: P.creamAmount * CREAM_STROKES[i].m * (0.30 + 0.70 * tp) * (0.85 + 0.3 * Math.sin(d.u * 13 + i)),
        radius: P.creamRadius * CREAM_STROKES[i].r * (0.5 + 0.5 * tp) * (0.88 + 0.24 * Math.sin(d.u * 9 + i * 2)),
        dx: 7, dy: 0,
      });
    }
    state.idxM[i] = Math.max(from, to);
  });
}

/* ---------- 镜头 ---------- */
function applyCam(v) {
  stageInner.style.transform =
    `translate(${((0.5 - v.x) * v.z * 100).toFixed(2)}%, ${((0.5 - v.y) * v.z * 100).toFixed(2)}%) scale(${v.z.toFixed(3)})`;
}
const lerpCam = (a, b, p) => ({ x: a.x + (b.x - a.x) * p, y: a.y + (b.y - a.y) * p, z: a.z + (b.z - a.z) * p });

function applyCamera(t) {
  if (!USE_CAM) { stageInner.style.transform = ''; return; }
  let prev = CENTER;
  for (let i = 0; i < charStarts.length; i++) {
    const c = charStarts[i];
    const f = focusOf(i);
    const target = { x: f.x, y: f.y, z: CAM_ZOOM };
    if (t < c.camFrom) { applyCam(prev); return; }
    if (t < c.writeFrom) {
      const p = easeIO((t - c.camFrom) / Math.max(1e-3, c.writeFrom - c.camFrom));
      applyCam(lerpCam(prev, target, p));
      return;
    }
    prev = target;
  }
  if (t >= camBackFrom) {
    const p = easeIO(Math.min(1, (t - camBackFrom) / CAM_BACK));
    applyCam(lerpCam(prev, CENTER, p));
    return;
  }
  applyCam(prev);
}

/* ---------- 主循环 ---------- */
function tick(ts) {
  if (!playing) return;
  const t = (ts - startAt) / 1000 / SLOW;
  root.getElementById('time').textContent = t.toFixed(2) + 's';

  if (t < coverStart) {
    phaseEl.textContent = '逐字勾绘';
    if (!state.writingInk) {
      ink.set({ soft: num('wsoft', 0.085), velocityDissipation: num('wvel', 2.4), densityDissipation: num('wdens', 0.30) });
      state.writingInk = true;
    }
    if (!state.redInk && t >= charStarts[2].writeFrom) {
      ink.set({ soft: num('wsoft_red', 0.050), velocityDissipation: num('wvel_red', 2.8) });
      state.redInk = true;
    }
    plan.forEach((item, gi) => {
      const c = charStarts[gi];
      const p = (t - c.writeFrom) / T.perChar;
      if (p > 0) writeGlyph(gi, Math.min(1, p));
      if (p >= GLYPH_AT) glyphEls[gi].style.opacity = String(GLYPH_OP);
    });
    applyCamera(t);
  } else {
    /* v12：扫墨开始时字稿仍留在墨层之下，用 0.7s 溶解；墨条从上面扫过，字是“化进墨里”而不是被瞬间盖掉 */
    const fade = 1 - sstep((t - coverStart - 0.08) / 0.65);
    glyphEls.forEach(g => { g.style.transition = 'none'; g.style.opacity = String(GLYPH_OP * fade); });
    canvas.style.zIndex = '3';
    if (!state.coverInk) {
      ink.set({ soft: P.soft, velocityDissipation: P.vel, densityDissipation: P.dens });
      state.coverInk = true;
    }
    stageInner.style.transform = '';

    const ghostT = cl01((t - coverStart) / 0.9);
    const ghostA = t >= repAt ? GHOST * (1 - cl01((t - repAt) / 0.9)) : GHOST * ghostT;
    ghostSvg.style.opacity = ghostA.toFixed(3);

    runCover(Math.min(1, (t - coverStart) / T.coverDur));

    if (t >= creamStart) {
      if (!state.creamCurl) { ink.set({ curl: num('mcurl', 2.2) }); state.creamCurl = true; }
      runCream(t);
      const mtnP = cl01((t - creamStart) / (creamEnd - creamStart + 0.8));
      mtn.style.opacity = (0.46 * mtnP).toFixed(3);
      const drift = (t - creamStart) * 4.2;
      if (mtnR1) mtnR1.setAttribute('transform', `translate(${(drift * 0.4).toFixed(1)}, 0)`);
      if (mtnR2) mtnR2.setAttribute('transform', `translate(${(-drift * 0.65).toFixed(1)}, 0)`);
      if (mtnR3) mtnR3.setAttribute('transform', `translate(${(drift * 0.9).toFixed(1)}, 0)`);

      if (t >= repAt) {
        const rp = easeIO(cl01((t - repAt) / 0.9));
        rep.style.opacity = rp.toFixed(3);
        clr.style.opacity = (rp * clearMode).toFixed(3);
        const shadowCol = clearMode ? 'rgba(246,240,224,.95)' : 'rgba(18,12,6,.85)';
        rep.style.filter = clearMode
          ? `blur(${((1 - rp) * 4.2).toFixed(2)}px)`
          : `blur(${((1 - rp) * 4.2).toFixed(2)}px) drop-shadow(0 0 6px ${shadowCol})`;
        rep.style.transform = `scale(${(1.025 - 0.025 * rp).toFixed(4)})`;

        if (t > repAt + 0.85 && t < pushAt && Math.random() < 0.28) {
          const rx = 0.25 + Math.random() * 0.5;
          const ry = 0.22 + Math.random() * 0.56;
          const ang = Math.random() * 6.283;
          ink.ink(rx, ry, { pigment: 'cream', amount: 0.04, radius: 0.045, dx: Math.cos(ang) * 4, dy: Math.sin(ang) * 4 });
        }
      }
      if (t >= sealAt && !state.sealed) {
        state.sealed = true;
        seal.classList.add('on');
        sealRing.classList.add('boom');
        burst(sealXY.x, sealXY.y, 44, 4.4, 0.9);
      }
    }

    if (t >= pushAt) {
      playing = false;
      ink.pause();
      onDone();
      return;
    } else if (t >= sealAt) {
      phaseEl.textContent = '落印定帧';
    } else if (t >= repAt) {
      phaseEl.textContent = '题字重现';
    } else if (t >= creamStart) {
      phaseEl.textContent = '淡彩笔触';
    } else {
      phaseEl.textContent = '扫墨覆页';
    }
  }
  raf = requestAnimationFrame(tick);
}

/* ---------- 播放 ---------- */
function play() {
  reset();
  pickStyleForRun();
  if (!ink) {
    rep.style.opacity = '1';
    fallbackTimer = setTimeout(onDone, 1200);
    return;
  }
  layoutSeal();
  startAt = performance.now();
  playing = true;
  raf = requestAnimationFrame(tick);
}

/* ---------- 远山与青海波 ---------- */
const mtn = document.createElementNS(NS, 'svg');
mtn.id = 'mtn';
mtn.setAttribute('viewBox', '0 0 1440 600');
mtn.setAttribute('preserveAspectRatio', 'xMidYMax slice');
const ridge = (base, amp, sd, gradId) => {
  let d = 'M-80 600 L-80 ' + base;
  for (let x = -80; x <= 1520; x += 16) {
    const y = base
      - amp * (0.5 + 0.5 * Math.sin(x * 0.0038 + sd))
      - amp * 0.34 * Math.sin(x * 0.0095 + sd * 2.1)
      - amp * 0.14 * Math.cos(x * 0.021 - sd * 1.4);
    d += ` L${x} ${y.toFixed(1)}`;
  }
  return `<path d="${d} L1520 600Z" fill="url(#${gradId})"/>`;
};
mtn.innerHTML = `<defs>
  <linearGradient id="rg1" x1="0" y1="255" x2="0" y2="600" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#4f7a78" stop-opacity="0.03"/>
    <stop offset="38%" stop-color="#4f7a78" stop-opacity="0.22"/>
    <stop offset="100%" stop-color="#35605f" stop-opacity="0.35"/>
  </linearGradient>
  <linearGradient id="rg2" x1="0" y1="335" x2="0" y2="600" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#35605f" stop-opacity="0.06"/>
    <stop offset="42%" stop-color="#35605f" stop-opacity="0.30"/>
    <stop offset="100%" stop-color="#1f4546" stop-opacity="0.45"/>
  </linearGradient>
  <linearGradient id="rg3" x1="0" y1="410" x2="0" y2="600" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#1f4546" stop-opacity="0.10"/>
    <stop offset="45%" stop-color="#1f4546" stop-opacity="0.38"/>
    <stop offset="100%" stop-color="#163435" stop-opacity="0.54"/>
  </linearGradient>
  <linearGradient id="mistGrad" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0%" stop-color="#f6efe0" stop-opacity="0"/>
    <stop offset="50%" stop-color="#f6efe0" stop-opacity="0.42"/>
    <stop offset="100%" stop-color="#f6efe0" stop-opacity="0"/>
  </linearGradient>
  <linearGradient id="waveFade" x1="0" y1="490" x2="0" y2="600" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#ffffff" stop-opacity="0"/>
    <stop offset="38%" stop-color="#ffffff" stop-opacity="0.55"/>
    <stop offset="100%" stop-color="#ffffff" stop-opacity="1"/>
  </linearGradient>
  <mask id="waveMask"><rect x="0" y="490" width="1440" height="110" fill="url(#waveFade)"/></mask>
  <pattern id="sg" width="60" height="30" patternUnits="userSpaceOnUse"><g fill="none" stroke="#1f4546" stroke-width="1.15">
    <circle cx="0" cy="30" r="28"/><circle cx="0" cy="30" r="20"/><circle cx="0" cy="30" r="12"/><circle cx="60" cy="30" r="28"/><circle cx="60" cy="30" r="20"/><circle cx="60" cy="30" r="12"/>
    <circle cx="30" cy="15" r="28"/><circle cx="30" cy="15" r="20"/><circle cx="30" cy="15" r="12"/></g></pattern>
</defs>
  ${ridge(355, 76, 1.0, 'rg1')}
  <ellipse cx="520" cy="410" rx="420" ry="26" fill="url(#mistGrad)"/>
  ${ridge(418, 60, 3.1, 'rg2')}
  <ellipse cx="920" cy="468" rx="460" ry="24" fill="url(#mistGrad)"/>
  ${ridge(478, 46, 5.7, 'rg3')}
  <rect x="0" y="490" width="1440" height="110" fill="url(#sg)" opacity=".32" mask="url(#waveMask)"/>`;
ghostSvg.after(mtn);
const [mtnR1, mtnR2, mtnR3] = mtn.querySelectorAll('path');

/* ---------- 金粒 ---------- */
const sparks = root.getElementById('sparks'), sx = sparks.getContext('2d');
let parts = [];
let sealXY = { x: 0, y: 0 };

function burst(x, y, n, spread, upBias = 0.8) {
  for (let i = 0; i < n; i++) {
    parts.push({
      x, y,
      vx: (Math.random() - 0.5) * spread,
      vy: -Math.random() * spread * upBias - 0.15,
      life: 0.85 + Math.random() * 0.35,
      r: 0.75 + Math.random() * 2.1,
      c: Math.random() < 0.25 ? '238,112,72' : '218,174,74',
    });
  }
}
(function sparkLoop() {
  if (sparks.width !== innerWidth || sparks.height !== innerHeight) { sparks.width = innerWidth; sparks.height = innerHeight; }
  sx.clearRect(0, 0, sparks.width, sparks.height);
  sx.shadowBlur = 8; sx.shadowColor = 'rgba(240,200,100,.8)';
  parts = parts.filter(q => q.life > 0);
  for (const q of parts) {
    q.x += q.vx; q.y += q.vy; q.vy += 0.022; q.vx *= 0.99; q.life -= 0.013;
    sx.fillStyle = `rgba(${q.c},${Math.min(1, q.life * 0.92).toFixed(3)})`;
    sx.beginPath(); sx.arc(q.x, q.y, q.r, 0, 6.283); sx.fill();
  }
  sparkRaf = requestAnimationFrame(sparkLoop);
})();


let resizeTimer;
let width = innerWidth;
const resize = () => {
  if (innerWidth === width) return;
  width = innerWidth;
  clearTimeout(resizeTimer);
  resizeTimer = setTimeout(() => { syncStage(); buildLayout(); layoutSeal(); }, 150);
};
const contextLost = () => onDone();
window.addEventListener('resize', resize);
canvas.addEventListener('webglcontextlost', contextLost);
syncStage();
buildLayout();
return {
  play,
  pause() {
    playing = false;
    cancelAnimationFrame(raf);
    cancelAnimationFrame(sparkRaf);
    ink?.pause();
  },
  destroy() {
    playing = false;
    cancelAnimationFrame(raf);
    cancelAnimationFrame(sparkRaf);
    clearTimeout(fallbackTimer);
    clearTimeout(resizeTimer);
    window.removeEventListener('resize', resize);
    canvas.removeEventListener('webglcontextlost', contextLost);
    ink?.destroy();
    root.replaceChildren();
  },
};

}
