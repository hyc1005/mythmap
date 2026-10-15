import { spawn } from 'node:child_process';
import { once } from 'node:events';
import { createServer } from 'node:net';
import { fileURLToPath } from 'node:url';

const args = process.argv.slice(2);
const separator = args.indexOf('--');
const options = separator < 0 ? args : args.slice(0, separator);
const command = separator < 0 ? [] : args.slice(separator + 1);
const option = (name, fallback) => options.includes(name) ? options[options.indexOf(name) + 1] : fallback;
const port = Number(option('--port', '0'));
const base = option('--base', '/');
if (!Number.isInteger(port) || port < 0 || port > 65535 || !base.startsWith('/')) throw new Error('Invalid preview port or base');
if (port) {
  const probe = createServer();
  await new Promise((resolve, reject) => { probe.once('error', reject); probe.listen(port, '127.0.0.1', resolve); });
  await new Promise(resolve => probe.close(resolve));
}
const children = new Set();
let stopping = false;
let interrupted;
const interruption = new Promise(resolve => { interrupted = resolve; });
const signal = () => { stopping = true; interrupted(130); };
process.on('SIGINT', signal);
process.on('SIGTERM', signal);
const start = (executable, argv, extra = {}) => {
  const child = spawn(executable, argv, { cwd: fileURLToPath(new URL('..', import.meta.url)), windowsHide: true, ...extra });
  children.add(child);
  return child;
};
const stop = async child => {
  if (!child.pid || child.exitCode !== null || child.signalCode !== null) return;
  if (process.platform === 'win32') {
    const killer = spawn('taskkill', ['/PID', String(child.pid), '/T', '/F'], { windowsHide: true, stdio: 'ignore' });
    await once(killer, 'exit');
  } else {
    try { process.kill(-child.pid, 'SIGTERM'); } catch (error) { if (error.code !== 'ESRCH') throw error; }
  }
  if (child.exitCode === null && child.signalCode === null) {
    const timeout = setTimeout(() => {
      try { process.kill(-child.pid, 'SIGKILL'); } catch (error) { if (error.code !== 'ESRCH') console.error(error.message); }
    }, 3000);
    try { await once(child, 'exit'); } finally { clearTimeout(timeout); }
  }
};
let url;
try {
  const preview = start(process.execPath, ['node_modules/vite/bin/vite.js', 'preview', '--host', '127.0.0.1', '--port', String(port), '--strictPort', '--base', base], { stdio: ['ignore', 'pipe', 'pipe'], detached: process.platform !== 'win32' });
  const ready = new Promise((resolve, reject) => {
    let output = '';
    const timeout = setTimeout(() => reject(new Error('Preview startup timed out')), 15000);
    preview.stdout.on('data', chunk => {
      output += chunk.toString().replace(/\x1b\[[0-9;]*m/g, '');
      const match = output.match(/http:\/\/127\.0\.0\.1:\d+\/\S*/);
      if (match) { clearTimeout(timeout); resolve(match[0]); }
    });
    preview.stderr.on('data', chunk => process.stderr.write(chunk));
    preview.once('error', error => { clearTimeout(timeout); reject(error); });
    preview.once('exit', code => { clearTimeout(timeout); reject(new Error(`Preview exited before ready: ${code}`)); });
  });
  url = await Promise.race([ready, interruption.then(() => { throw new Error('Interrupted'); })]);
  console.log(`Preview PID=${preview.pid} URL=${url} command=vite preview --port ${port} --base ${base}`);
  if (command.length) {
    const executable = command[0] === 'node' ? process.execPath : command[0];
    const check = start(executable, command.slice(1), { stdio: 'inherit', env: { ...process.env, ATLAS_URL: url }, detached: process.platform !== 'win32' });
    const result = await Promise.race([new Promise((resolve, reject) => { check.once('error', reject); check.once('exit', code => resolve(code ?? 1)); }), interruption]);
    process.exitCode = result;
  } else await interruption;
} catch (error) {
  if (!stopping) console.error(error.message);
  process.exitCode = stopping ? 130 : 1;
} finally {
  await Promise.all([...children].reverse().map(stop));
  if (url) {
    const address = new URL(url);
    const probe = createServer();
    await new Promise((resolve, reject) => { probe.once('error', reject); probe.listen(Number(address.port), address.hostname, resolve); });
    await new Promise(resolve => probe.close(resolve));
    console.log(`Preview stopped; port ${address.port} released.`);
  }
  process.off('SIGINT', signal);
  process.off('SIGTERM', signal);
}
