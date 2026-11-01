import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import { readFile, mkdir } from 'node:fs/promises';
import { spawn } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import { chromium } from 'playwright';

const frontend = new URL('../../', import.meta.url);
const source = new URL('public/data/atlas/myth-icons/characters/', frontend);
const output = new URL('public/data/atlas/refined/', frontend);
const svg = (await readFile(new URL('fuxi-corrected.svg', source), 'utf8')).replace(/\r\n/g, '\n');
const bitmap = await readFile(new URL('fuxi-clean.webp', source));
assert.equal((svg.match(/<image\b/g) || []).length, 1, 'One existing figure dependency');
assert.ok(svg.includes('href="fuxi-clean.webp"'), 'Expected existing figure');
const composite = svg.replace('href="fuxi-clean.webp"', `href="data:image/webp;base64,${bitmap.toString('base64')}"`);
await mkdir(output, { recursive: true });
const browser = await chromium.launch();
let png, renderer;
try {
  renderer = browser.version();
  const page = await browser.newPage({ viewport: { width: 1021, height: 1540 }, deviceScaleFactor: 1 });
  await page.route('**/*', route => route.abort());
  await page.setContent('<html><meta charset="utf-8"><style>html,body{margin:0;background:transparent}svg{display:block}</style>' + composite + '</html>');
  await page.evaluate(async () => {
    const image = new Image();
    image.src = document.querySelector('svg image').getAttribute('href');
    await image.decode();
    await document.fonts.ready;
    await new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve)));
  });
  png = await page.screenshot({ omitBackground: true });
} finally { await browser.close(); }

const encode = String.raw`
import io,json,sys,hashlib
from pathlib import Path
from PIL import Image
destination=Path(sys.argv[1]); variants={}
with Image.open(io.BytesIO(sys.stdin.buffer.read())) as source:
    assert source.mode=='RGBA' and source.getchannel('A').getextrema()[0]==0
    for variant,edge in {'full':1280,'card':320,'preview':480,'map':128}.items():
        image=source.copy(); image.thumbnail((round(edge*.88),round(edge*.88)),Image.Resampling.LANCZOS)
        canvas=Image.new('RGBA',(edge,edge),(0,0,0,0)); canvas.alpha_composite(image,((edge-image.width)//2,(edge-image.height)//2))
        name='fuxi-corrected-v1-'+variant+'.webp'; target=destination/name
        canvas.save(target,'WEBP',quality=88,method=6,alpha_quality=100)
        data=target.read_bytes(); variants[variant]={'path':'/data/atlas/refined/'+name,'bytes':len(data),'dimensions':[edge,edge],'sha256':hashlib.sha256(data).hexdigest()}
print(json.dumps(variants))
`;
const child = spawn('python', ['-c', encode, fileURLToPath(output)], { windowsHide: true, stdio: ['pipe', 'pipe', 'inherit'] });
let result = '';
child.stdout.on('data', chunk => { result += chunk; });
child.stdin.on('error', () => {});
child.stdin.end(png);
const exit = await new Promise((resolve, reject) => { child.once('error', reject); child.once('close', resolve); });
assert.equal(exit, 0, 'Existing Pillow WebP export completed');
console.log(JSON.stringify({ tool: 'Chromium SVG rasterization + Pillow WebP export', model: 'not_applicable_no_AI_generation', renderer, platform: process.platform,
  sources: [{ path: 'frontend/public/data/atlas/myth-icons/characters/fuxi-corrected.svg', sha256_lf: createHash('sha256').update(svg).digest('hex') },
    { path: 'frontend/public/data/atlas/myth-icons/characters/fuxi-clean.webp', sha256: createHash('sha256').update(bitmap).digest('hex') }], variants: JSON.parse(result) }, null, 2));
