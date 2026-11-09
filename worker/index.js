// Innova Space site: static pages from public/, plus /api/contact, which emails the Innova inbox.
import { EmailMessage } from 'cloudflare:email';

const json = (data, status = 200) => new Response(JSON.stringify(data), { status, headers: { 'content-type': 'application/json', 'cache-control': 'no-store' } });
const seen = new Map(); // best-effort limit per connection, per running instance
const b64 = (s) => btoa(String.fromCharCode(...new TextEncoder().encode(s)));
const word = (s) => `=?UTF-8?B?${b64(s)}?=`;
const clean = (v, n) => String(v ?? '').replace(/\r/g, '').trim().slice(0, n);

async function contact(req, env) {
  const body = await req.json().catch(() => ({}));
  if (body.website) return json({ ok: true }); // a bot filled the hidden field: pretend it worked
  if (Number(body.elapsed) < 3000) return json({ error: 'too-fast' }, 400);
  const name = clean(body.name, 100).replace(/\n/g, ' ');
  const email = clean(body.email, 120);
  const message = clean(body.message, 4000);
  const topic = clean(body.topic || 'Other', 40).replace(/\n/g, ' ');
  if (!name || !message || !/^[^\s@<>]+@[^\s@<>]+\.[^\s@<>]+$/.test(email)) return json({ error: 'missing' }, 400);

  const ip = req.headers.get('cf-connecting-ip') || '';
  const now = Date.now(), hits = (seen.get(ip) || []).filter((t) => now - t < 3600e3);
  if (hits.length >= 5) return json({ error: 'slow-down' }, 429);
  seen.set(ip, [...hits, now]);

  const id = crypto.randomUUID();
  const text = `${message}\n\n—\nFrom: ${name} <${email}>\nTopic: ${topic}\nSent from innovaspace.app/contact`;
  const raw = [
    `From: ${word('Innova Space site')} <${env.CONTACT_FROM}>`, `To: <${env.CONTACT_TO}>`, `Reply-To: <${email}>`,
    `Subject: ${word(`${topic} · ${name}`)}`, `Message-ID: <${id}@innovaspace.app>`, `Date: ${new Date().toUTCString()}`,
    'MIME-Version: 1.0', 'Content-Type: text/plain; charset=utf-8', 'Content-Transfer-Encoding: base64', '',
    b64(text).replace(/.{76}/g, '$&\r\n'),
  ].join('\r\n');
  try {
    await env.CONTACT_MAIL.send(new EmailMessage(env.CONTACT_FROM, env.CONTACT_TO, raw));
    return json({ ok: true });
  } catch (e) {
    return json({ error: 'mail' }, 502);
  }
}

export default {
  async fetch(req, env) {
    const url = new URL(req.url);
    if (url.pathname === '/api/contact') return req.method === 'POST' ? contact(req, env) : json({ error: 'method' }, 405);
    return env.ASSETS.fetch(req);
  },
};
