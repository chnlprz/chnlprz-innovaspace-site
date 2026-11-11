"""Builds the static pages in public/ from the content below. Run: python3 scripts/build.py
No build step on Cloudflare: the generated HTML is committed."""
import html, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent / 'public'
E = html.escape
EMAIL = 'hello@innovaspace.app'
LINKEDIN = 'https://www.linkedin.com/in/chanel-perez-3306051a6/'
GITHUB = 'https://github.com/chnlprz'

ICON = {
 'nudge': '<rect width="100" height="100" rx="22.5" fill="#5e3449"/><g fill="none" stroke="#f3e9ec" stroke-width="5.5"><rect x="25" y="25" width="22" height="22" rx="6"/><rect x="53" y="25" width="22" height="22" rx="6"/><rect x="25" y="53" width="22" height="22" rx="6"/></g><g transform="rotate(14 66 66)"><rect x="56" y="56" width="22" height="22" rx="6" fill="#e0946f"/></g>',
 'noggin': '<rect width="100" height="100" rx="22.5" fill="#24505C"/><path d="M36 38 a14 14 0 1 1 20 12.6 c-4 2 -6 4.4 -6 9.4 V62" fill="none" stroke="#F1EDE4" stroke-width="5.5" stroke-linecap="round"/><circle cx="50" cy="75" r="6" fill="#E8B04B"/>',
 'drift': '<rect width="100" height="100" rx="22.5" fill="#2B3152"/><path d="M22 58 H78 L68 72 H32 Z M36 58 L50 30 L64 58" fill="none" stroke="#F1EDE4" stroke-width="5.5" stroke-linejoin="round"/><circle cx="50" cy="48" r="5.5" fill="#D9825B"/><path d="M18 82 q8 -5 16 0 t16 0 t16 0 t16 0" fill="none" stroke="#F1EDE4" stroke-width="4" stroke-opacity="0.45" stroke-linecap="round"/>',
 'aurasync': '<rect width="100" height="100" rx="22.5" fill="#3D6656"/><g fill="none" stroke="#F1EDE4" stroke-width="5.5" stroke-linejoin="round"><path d="M50 70 C40 58 40 38 50 26 C60 38 60 58 50 70 Z"/><path d="M50 70 C36 70 24 58 22 44 C36 44 46 54 50 70 Z"/><path d="M50 70 C64 70 76 58 78 44 C64 44 54 54 50 70 Z"/></g><circle cx="50" cy="78" r="4.5" fill="#EDB27A"/>',
}
WORD = {
 'nudge': 'Nudge<span class="gold">!</span>',
 'noggin': 'Noggin<span class="gold">?</span>',
 'drift': '<i>Drift</i><span class="gold">.</span>',
 'aurasync': 'AuraS<span class="gold">y</span>nc',
}
NAME = {'nudge': 'Nudge!', 'noggin': 'Noggin?', 'drift': 'Drift.', 'aurasync': 'AuraSync'}

def icon(k, size):
    return f'<svg class="icon" width="{size}" height="{size}" viewBox="0 0 100 100" aria-hidden="true">{ICON[k]}</svg>'

MOON = '<svg class="moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>'
SUN = '<svg class="sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4.5"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>'

def page(path, title, desc, body, current='', back=False):
    url = 'https://innovaspace.app/' + ('' if path == 'index.html' else path[:-5])
    nav = ''.join(f'<a href="{href}"{" aria-current=\"page\"" if key == current else ""}{" class=\"hide-sm\"" if key == "work" else ""}>{label}</a>'
                  for key, href, label in [('work', '/#work', 'Work'), ('about', '/about', 'About'), ('contact', '/contact', 'Contact')])
    left = '<a class="muted" href="/" style="font-size:14px">← All work</a>' if back else '<a class="brand" href="/"><span class="is-mark" aria-hidden="true">I<b>S</b></span>Chanel Perez <span>· Innova Space</span></a>'
    doc = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<meta name="theme-color" content="#F4F0E8" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0B0A09" media="(prefers-color-scheme: dark)">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" href="/assets/favicon-32.png" type="image/png" sizes="32x32">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Chanel Perez · Innova Space">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="https://innovaspace.app/assets/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="1200">
<meta property="og:image:alt" content="Chanel Perez portfolio. Gentle systems for everyday life. Innova Space.">
<meta name="twitter:card" content="summary">
<meta name="author" content="Chanel Perez">
<script>try{{var t=localStorage.getItem('theme');if(t)document.documentElement.setAttribute('data-theme',t)}}catch(e){{}}</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,400..600;1,6..96,400..600&family=Inter+Tight:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/site.css">
</head>
<body>
<div class="page">
<header class="top">
  {left}
  <nav class="nav" aria-label="Main">{nav}<button type="button" class="theme-btn" aria-label="Switch theme">{MOON}{SUN}</button></nav>
</header>
{body}
<footer class="foot"><span>© 2026 Innova Space</span><span><a href="mailto:{EMAIL}">{EMAIL}</a></span></footer>
</div>
<script src="/assets/site.js" defer></script>
</body>
</html>
'''
    out = ROOT / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(doc)

def shot(name, alt, cls='shot'):
    return (f'<div class="{cls}"><img class="only-light" src="/assets/img/nudge-{name}-light.webp" alt="{E(alt)}" width="520" height="1125" loading="lazy">'
            f'<img class="only-dark" src="/assets/img/nudge-{name}-dark.webp" alt="{E(alt)}, Supernova theme" width="520" height="1125" loading="lazy"></div>')

# ── Home ──
PRODS = [
 ('noggin', 'An idea bank for passing questions. Stay curious.', 'Live demo · v1'),
 ('drift', 'Daily check-ins that earn letters to and from fictional pen pals across time.', 'Discovery'),
 ('aurasync', 'Your local wellness hub, all in one place.', 'Discovery'),
]
home = f'''<main id="work" class="bento">
  <section class="tile intro">
    <p class="muted" style="font-size:13px">Independent product builder · Behavioral science · Philippines</p>
    <div>
      <h1>Gentle systems for <span class="gold">everyday</span> life.</h1>
      <p class="lede">I build small, warm tools grounded in psychology and shaped around real habits. Nudge! is live, Noggin? has a v1 demo, and two more are in discovery.</p>
    </div>
    <div class="row"><a class="btn gold" href="/work/nudge">See my work</a><a class="btn line" href="/contact">Say hello</a></div>
  </section>
  <section class="tile feat">
    <div class="copy">
      <div style="display:flex;justify-content:space-between;align-items:center;gap:12px">{icon('nudge', 48)}<span class="muted" style="font-size:13px;display:inline-flex;align-items:center;gap:8px"><i class="dot"></i>Featured · Live v2.6</span></div>
      <div>
        <h2 class="wordmark">{WORD['nudge']}</h2>
        <p class="muted" style="font-size:21px;margin-top:10px">Your day, gently.</p>
        <p class="muted" style="font-size:15px;margin-top:12px">A priority tracker for the tired version of you. Capture first, sort later, and progress that never drops.</p>
      </div>
      <div class="row" style="gap:20px;font-weight:500"><a href="/work/nudge">Case study →</a><a class="gold" href="https://nudge.innovaspace.app">Open app ↗</a></div>
    </div>
    {shot('home', 'Nudge! home screen with the Task Banner')}
  </section>
''' + ''.join(f'''  <a class="tile prod" href="/work/{k}">
    <div class="head">{icon(k, 40)}<span>{'<i class="dot"></i> ' if st.startswith('Live') else ''}{st}</span></div>
    <div><h3>{WORD[k]}</h3><p>{E(d)}</p><span class="cta">Explore case study →</span></div>
  </a>
''' for k, d, st in PRODS) + '''  <a class="tile about-tile" href="/about">
    <span style="font-size:12px;opacity:.75">About me</span>
    <span style="font-size:15px;line-height:1.5">Psychology, e-commerce and a love for systems. Also cats, curating and a good declutter.</span>
    <span class="more"><span>Read more and CV</span><span class="plus" aria-hidden="true">+</span></span>
  </a>
</main>'''
page('index.html', 'Chanel Perez · Gentle systems for everyday life', 'Independent product builder with a behavioral-science perspective. Founder of Innova Space, maker of Nudge!, Noggin, Drift and AuraSync.', home, 'work')

# ── About ──
JOBS = [
 ('Customer Support Advisor', '2019 – now', 'Buy It Direct Group, UK (remote) · Amazon, eBay, TikTok and more'),
 ('Course Creator and Online Learning Strategist', '2024 – 2025', 'Self-employed · Kajabi courses, funnels and email automation'),
 ('Customer Service Representative', '2019', '24-7 Intouch · Airbnb account, Resolutions 1'),
 ('Founder, Innova Space', '2026', 'Nudge! (live) · Noggin, Drift and AuraSync in discovery'),
]
TOOLS = ['Make.com', 'Airtable', 'Kajabi', 'Google Workspace', 'Microsoft Office', 'Canva', 'Claude · ChatGPT · Gemini']
about = f'''<main class="tile about">
  <aside>
    <div class="arch"><img src="/assets/img/chanel.webp" alt="Chanel Perez" width="600" height="600"></div>
    <div><h1 style="font-size:26px;font-weight:600;letter-spacing:-.02em">Chanel Perez</h1><p class="muted" style="font-size:14px">Founder, Innova Space · Quezon City</p></div>
    <div class="row"><a class="btn gold" href="/assets/Chanel-Perez-CV.pdf" download>Download CV</a><a class="btn line" href="mailto:{EMAIL}">Email me</a></div>
  </aside>
  <div class="body">
    <div style="display:flex;flex-direction:column;gap:10px">
      <p class="label">About me</p>
      <p class="intro-text">Psychology student, seven years in remote e-commerce, and an INTJ with a child-like sense of wonder. I’m in it for the vision, not just the invoice. I don’t stop at “it works”: I make things simple, intuitive and efficient, built around the habits people already have. Because human‑ing should be easy.</p>
    </div>
    <div class="how">
      <div><b>Vision first.</b><span>I want to understand the why before I build the what.</span></div>
      <div><b>Simple beats clever.</b><span>Efficient, intuitive, nothing extra.</span></div>
      <div><b>Habits, not willpower.</b><span>Tools should fit how people really live.</span></div>
    </div>
    <div class="cv">
      <div class="col"><p class="eyebrow">Experience</p>{''.join(f'<div class="job"><b>{E(a)}</b><span>{E(b)}</span><span>{E(c)}</span></div>' for a, b, c in JOBS)}</div>
      <div class="col">
        <p class="eyebrow">Education</p>
        <div><b style="font-size:15px">AB Psychology</b><p class="muted" style="font-size:13px">CAP College Foundation, Inc. · Currently enrolled</p></div>
        <p class="eyebrow" style="margin-top:6px">Tools</p>
        <div class="row" style="gap:6px">{''.join(f'<span class="chip" style="font-size:12px">{E(t)}</span>' for t in TOOLS)}</div>
        <p class="eyebrow" style="margin-top:6px">Languages</p>
        <p style="font-size:14px">English, Filipino</p>
      </div>
    </div>
    <p class="muted" style="margin-top:auto;font-size:14px"><span class="gold">✦</span> Off the clock: singing, piano, reading and the gym. Curating pretty things, a good declutter now and then, and any cat that lets me pet it.</p>
  </div>
</main>'''
page('about.html', 'About · Chanel Perez', 'Psychology student with seven years in e-commerce, building gentle tools under Innova Space.', about, 'about')

# ── Contact ──
TOPICS = ['A project', 'Hiring', 'App feedback', 'Just saying hi']
contact = f'''<main class="contact">
  <section class="tile say">
    <p class="label">Contact</p>
    <div style="display:flex;flex-direction:column;gap:16px">
      <h1>Let’s <span class="gold">talk</span>.</h1>
      <p class="muted" style="font-size:17px;max-width:420px">A project, a role, feedback on one of my apps, or just hello. I usually reply within two days.</p>
    </div>
    <div class="links">
      <a href="mailto:{EMAIL}"><span class="muted">Email</span><span>{EMAIL} ↗</span></a>
      <a href="{LINKEDIN}" rel="noopener"><span class="muted">LinkedIn</span><span>chanel-perez ↗</span></a>
      <a href="{GITHUB}" rel="noopener"><span class="muted">GitHub</span><span>@chnlprz ↗</span></a>
    </div>
  </section>
  <form id="contact-form" class="tile" novalidate>
    <fieldset><legend>What’s it about?</legend><div class="topics">{''.join(f'<input type="radio" name="topic" id="tp{i}" value="{E(t)}"{" checked" if i == 0 else ""}><label for="tp{i}">{E(t)}</label>' for i, t in enumerate(TOPICS))}</div></fieldset>
    <div class="two">
      <div class="field"><label for="cn">Your name</label><input id="cn" name="name" type="text" autocomplete="name" required maxlength="100"></div>
      <div class="field"><label for="ce">Your email</label><input id="ce" name="email" type="email" autocomplete="email" required maxlength="120"></div>
    </div>
    <div class="field" style="flex:1"><label for="cm">Message</label><textarea id="cm" name="message" required maxlength="4000"></textarea></div>
    <div class="hp" aria-hidden="true"><label for="cw">Leave this empty</label><input id="cw" name="website" type="text" tabindex="-1" autocomplete="off"></div>
    <div class="form-foot"><span class="muted" style="font-size:13px">Goes straight to my inbox. No spam, ever.</span><button class="btn gold" type="submit">Send message</button></div>
    <p id="form-status" class="status-msg" role="status" aria-live="polite"></p>
  </form>
</main>'''
page('contact.html', 'Contact · Chanel Perez', 'Get in touch with Chanel about a project, a role or one of her apps.', contact, 'contact')

# ── Case studies ──
def hero(k, tagline, status, facts, extra=''):
    return f'''<section class="tile case-hero">
  <div class="left">{icon(k, 72)}<h1 class="wordmark">{WORD[k]}</h1><p class="tag">{E(tagline)}</p><div class="row">{extra}<span class="chip" style="min-height:44px;align-items:center;padding:0 16px;gap:8px">{status}</span></div></div>
  <dl class="facts">{''.join(f'<div><dt>{E(a)}</dt><dd>{E(b)}</dd></div>' for a, b in facts)}</dl>
</section>'''

def pair(a_label, a, b_label, b):
    return f'''<div class="pair">
  <section class="tile"><p class="label">{a_label}</p><p class="big">{E(a)}</p></section>
  <section class="tile dark"><p class="label">{b_label}</p><p class="big">{E(b)}</p></section>
</div>'''

def steps(title, note, items, num=False, now_last=False):
    lis = ''.join(f'<li{" class=\"now\"" if now_last and i == len(items) - 1 else ""}><span class="k">{E(k)}</span><b>{E(t)}</b><span>{E(d)}</span></li>' for i, (k, t, d) in enumerate(items))
    return f'<section class="tile"><div class="sec-head"><h2>{title}</h2><span class="muted" style="font-size:13px">{E(note)}</span></div><ol class="steps{" num" if num else ""}" style="--n:{len(items)}">{lis}</ol></section>'

def grid4(items):
    return '<div class="grid4">' + ''.join(f'<div class="tile"><b>{E(a)}</b><span>{E(b)}</span></div>' for a, b in items) + '</div>'

nudge = hero('nudge', 'Your day, gently. A priority tracker built for the tired version of you.', '<i class="dot"></i>Live · v2.6',
  [('Role', 'Research, design and build. Solo, with AI as pair programmer'), ('Timeline', 'v1.0 to v2.6, November 2026'), ('Platform', 'Installable PWA, offline first, phone and desktop'), ('Stack', 'TypeScript, IndexedDB, Cloudflare Workers and D1')],
  '<a class="btn gold" href="https://nudge.innovaspace.app">Open Nudge! ↗</a>')
nudge += pair('The problem', 'Task apps expect you to organize while you capture. On tired days that’s too much, so the app gets abandoned and missed tasks start to feel like failure.',
              'What Nudge! does', 'Capture first and sort later. The right task rises at the right time, and effort is rewarded instead of streaks, so a slow week never costs you progress.')
nudge += steps('Process', 'From a single HTML file to a synced app', [
  ('v1.0', 'One HTML file', 'Matrix, effort points and peso rewards. Used daily to find what worked.'),
  ('Plan', 'Bible and design system', 'Every rule, the data model and design tokens written down first.'),
  ('v2.0', 'Rebuilt in 8 phases', 'Foundation, tasks, Home, Matrix, points, energy, onboarding, desktop.'),
  ('v2.2', 'Sync', 'Passkey sign-in, sync between devices and push reminders.'),
  ('v2.3–2.5', 'Polish', 'Supernova and Aurora skies, a warmer welcome, haptics.'),
  ('v2.6', 'New home', 'nudge.innovaspace.app and in-app feedback.')], now_last=True)
nudge += f'''<div class="pair">
  <article class="tile feature"><div><p class="label">Best feature · Task Banner</p><h3>What to do now, and what’s next.</h3><p>Home shows one task at a time. Order it your way, by the Matrix, or by Task Demand (light tasks first, or heavy first on a strong day). Timed tasks rise about an hour before they start.</p></div>
    <div class="mini" aria-hidden="true"><span class="eyebrow" style="font-size:10px">Now</span><div class="now"><b style="font-size:14px">Reply to supplier</b><span style="font-size:11px;opacity:.8">in 45 min · 15 min</span></div><span class="eyebrow" style="font-size:10px">Up next</span><div class="box">Thesis edits · heavy</div><div class="box">Piano practice</div></div></article>
  <article class="tile feature"><div><p class="label">Best feature · B=MAP insights</p><h3>Learning why tasks get avoided.</h3><p>Based on the Fogg Behavior Model (Behavior = Motivation, Ability, Prompt). Deleting an overdue task asks three skippable questions, and Analytics turns the answers into one gentle tip.</p></div>
    <div class="mini" aria-hidden="true"><b style="font-size:12px">Before it goes…</b><div class="box" style="display:flex;flex-direction:column;gap:6px"><span><b class="gold">M</b> · Does it still matter?</span><span><b class="gold">A</b> · Too big or too hard?</span><span><b class="gold">P</b> · Did it slip your mind?</span></div><div class="tip">Most of what you dropped felt too big. Try a 15-minute start.</div></div></article>
</div>'''
nudge += grid4([('Capture first, sort later', 'Fast capture to Unsorted with an optional batch date, then a Sort flow when you have headspace.'),
                ('Effort points, up only', '1 point per 15 minutes. Constellation levels never drop. Stardust and peso rewards.'),
                ('Energy aware', 'A daily energy check-in, plus an optional cycle-based estimate. Your answer always wins.'),
                ('Offline, synced if you want', 'Works without an account. Passkey sign-in syncs devices and sends reminders.')])
nudge += steps('Decisions that changed', 'What I changed after using v1 every day, and why', [
  ('Rebuild', 'Start over, on paper first', 'v1 grew as one HTML file. For 2.0 I wrote every rule and the data model down first, then rebuilt in reviewed phases.'),
  ('Rewards', 'Effort, not completion', '1 point per 15 minutes of effort, and multi-day tasks are checked off per day, so big tasks still pay off along the way.'),
  ('Ranks', 'Alchemy to constellations', 'Levels come from lifetime XP and never drop. Stardust is spent separately, so spending never costs you a level.'),
  ('Capture', 'Categories became optional', 'Anything unpicked is Uncategorized. Sorting can wait, so capture stays instant on tired days.'),
  ('Energy', 'Your answer always wins', 'The optional cycle-based estimate only suggests. The daily check-in overrides it and feeds Analytics.'),
  ('Accounts', 'Offline first, sign-up optional', 'Everything works on the device. Passkeys and sync are there for people who want more than one device.')])
nudge += '<section class="tile dark usp"><p class="label">Why it’s different</p><p>Built on behavior science, not willpower. It plans for low-energy days instead of punishing them.</p></section>'
nudge += ('<section class="tile"><div class="sec-head"><h2>Screens</h2><span class="muted" style="font-size:13px">Real screens from v2.6 with sample data. Dark mode shows the Supernova theme.</span></div><div class="screens">'
          + ''.join(f'<figure>{shot(n, "Nudge! " + c)}<figcaption>{E(c)}</figcaption></figure>' for n, c in [('home', 'Home · Task Banner, widgets and today'), ('matrix', 'Matrix · sorted for today'), ('avoided', 'Analytics · avoided tasks and B=MAP'), ('rank', 'Rank · constellations that only go up')])
          + '</div></section>')
nudge += '''<div class="next"><section class="tile"><p class="label">What’s next</p><p style="font-size:18px;margin-top:12px">Speak a batch of tasks and let AI suggest where they go, confirmed in one tap like the Sort flow. Then a native app for the App Store.</p></section>
<a class="tile" href="https://nudge.innovaspace.app"><span>Try it</span><span>nudge.innovaspace.app ↗</span></a></div>'''
page('work/nudge.html', 'Nudge! case study · Chanel Perez', 'How Nudge! went from a single HTML file to a synced, behavior-science task app.', nudge, back=True)

def wire(blocks):
    out = []
    for b in blocks:
        k = b[0]
        if k == 'title': out.append(f'<span class="t">{E(b[1])}</span>')
        elif k == 'hint': out.append(f'<span class="h">{E(b[1])}</span>')
        elif k == 'input': out.append(f'<span class="in" style="min-height:{b[2]}px">{E(b[1])}</span>')
        elif k == 'chips': out.append('<span class="chips">' + ''.join(f'<span>{E(c)}</span>' for c in b[1]) + '</span>')
        elif k == 'card': out.append(f'<span class="card"><b>{E(b[1])}</b><span>{E(b[2])}</span></span>')
        elif k == 'ph': out.append(f'<span class="ph" style="height:{b[2]}px">{E(b[1])}</span>')
        elif k == 'scale': out.append('<span class="scale"><i></i><i></i><i></i><i></i><i></i></span>')
        elif k == 'go': out.append(f'<span class="go">{E(b[1])}</span>')
        elif k == 'ghost': out.append(f'<span class="ghost">{E(b[1])}</span>')
    return '<div class="wire" aria-hidden="true">' + ''.join(out) + '</div>'

DISC = [
 dict(k='noggin', tag='Stay curious. A place for the thoughts you don’t want to lose.', stage='Live demo · v1', demo='https://noggin.innovaspace.app',
  facts=[('Stage', 'v1 demo live, still in discovery'), ('Platform', 'Planned: mobile-first PWA'), ('Role', 'Research, design, build'), ('Ecosystem', 'Learn here, then sync to Nudge! to act')],
  problem='Curious thoughts arrive when you can’t stop to look them up. They get forgotten, scattered across notes or lost in open tabs.',
  hyp='If saving a question takes seconds and the first answer is short and clear, people will come back to their curiosity instead of losing it.',
  note='Save first, explore later',
  how=[('Capture', 'Type or say a question in your own words. One tap to save.'), ('Sort', 'Noggin suggests a category. Change it anytime, or ignore it.'), ('Explore', 'When you have time, get a short, clear answer saved with the question.')],
  feats=[('Thought Nuggets', 'Small saved questions you can browse, revisit and pick up later.'), ('Suggested categories', 'Helps you find things again without planning folders.'), ('Quick research', 'A concise first answer instead of a long list of links.'), ('Sync to Nudge!', 'When curiosity becomes a plan, send it to Nudge! as steps.')],
  screens=[('Capture', [('title', 'What are you wondering?'), ('input', 'How is origami done?', 70), ('hint', 'Suggested category'), ('chips', ['Arts and crafts', 'Science', 'Change']), ('go', 'Save Nugget')]),
           ('Question bank', [('title', 'Your Nuggets'), ('chips', ['All', 'Science', 'Arts', 'Life']), ('card', 'How is origami done?', 'Arts and crafts · today'), ('card', 'Why are we human?', 'Life · 3 days ago'), ('card', 'Where did we come from?', 'Science · last week'), ('ghost', '+ New Nugget')]),
           ('Nugget detail', [('hint', 'Arts and crafts'), ('title', 'How is origami done?'), ('ph', 'Short answer: folding one square sheet without cuts or glue…', 150), ('ghost', 'Explore more'), ('go', 'Sync to Nudge!')])],
  progress=[(1, 'Concept, principles and product discovery doc'), (1, 'Name, tagline and brand mark'), (1, 'v1 demo live: capture without an account, categories, sorting, steps, Sync to Nudge! and backups'), (0, 'Interviews with people who collect random questions'), (0, 'Clickable prototype of capture and the question bank'), (0, 'Test suggested categories against manual sorting')],
  qs=['How much source transparency does a quick answer need to be trusted?', 'Do people need search, tags or pins to find Nuggets again?', 'How should duplicate or closely related questions be handled?']),
 dict(k='drift', tag='A daily check-in with a twist.', stage='Concept',
  facts=[('Stage', 'Concept and discovery'), ('Platform', 'Planned: mobile-first PWA'), ('Role', 'Research, design, build'), ('Pen pals', 'Fictional characters, never real strangers')],
  problem='Mood journals ask a lot and give little back, so most people stop within a week. Streaks make every missed day feel like failure.',
  hyp='If a quick check-in earns something to look forward to, like a letter that might arrive, people will keep showing up without streak pressure.',
  note='Reflection and a letter game, kept separate',
  how=[('Check in', 'A quick mood check-in, notes optional. Each one earns points.'), ('Drift a letter', 'Spend points to send a letter to the past or the future, on stationery you choose.'), ('Wait and wonder', 'A fictional pen pal may write back, and random letters can arrive. Replies are never guaranteed, so each one feels special.')],
  feats=[('Quick check-ins', 'Light and fast. No streaks and nothing lost for missed days.'), ('Patterns, not diagnoses', 'Weekly and monthly reflections show what you logged, gently.'), ('Letters through time', 'A cast of fictional correspondents, from a 1700s sailor to someone in the future.'), ('Stationery and keepsakes', 'Paper, ink and wax seals nudge who might reply. Letters can hold small mementos.')],
  screens=[('Daily check-in', [('title', 'How are you today?'), ('scale',), ('hint', 'Okay · a little tired'), ('input', 'Add a note (optional)', 70), ('go', 'Check in · +5 points')]),
           ('Write a letter', [('title', 'Drift a letter'), ('chips', ['To the past', 'To the future', 'Blind drift']), ('input', 'Dear friend in another time…', 110), ('hint', 'Stationery: navy ink · wax seal'), ('go', 'Send · 10 points')]),
           ('Inbox', [('title', 'Inbox'), ('ph', 'A letter has arrived. From the past?', 150), ('card', 'Sealed letter', 'Common · free to open'), ('ghost', 'Open letter')])],
  progress=[(1, 'Concept, two-system design and principles'), (1, 'Draft points economy and rarity tiers'), (1, 'Mock brand mark'), (0, 'Check-in questions and mood scale'), (0, 'First cast of fictional pen pals and their voices'), (0, 'Playtest letter arrival odds')],
  qs=['How can analytics show patterns without sounding clinical?', 'How often should letters arrive to keep anticipation fun?', 'Are the point prices balanced against daily check-ins?']),
 dict(k='aurasync', tag='Your local wellness hub.', stage='Early concept',
  facts=[('Stage', 'Early concept'), ('Platform', 'Planned: web and mobile'), ('Role', 'Research, design, build'), ('Focus', 'Local discovery, curated')],
  problem='Wellness options are scattered: coaches on social media, events on separate pages, spas on maps, retreats on travel sites. Finding the right fit takes too long.',
  hyp='If coaches, events, places and products live in one place, matched to what you need, people will try more wellness options close to home.',
  note='One place, matched to you',
  how=[('Tell us', 'A short survey on what you need right now: rest, movement, someone to talk to, or something to learn.'), ('Discover', 'See coaches, events, wellness centers, spas and retreats near you.'), ('Keep', 'Save coaches, follow recurring events and use exclusive offers.')],
  feats=[('Matched recommendations', 'Suggestions shaped by short surveys and what you save.'), ('Nearby and saved', 'Places and coaches close to you, plus a list of favorites.'), ('Groups and retreats', 'Recurring classes, small groups and getaways.'), ('Products and offers', 'Links to wellness products and apps, with member deals.')],
  screens=[('What do you need?', [('title', 'What do you need right now?'), ('chips', ['Rest', 'Move', 'Talk', 'Learn', 'Treat myself']), ('hint', 'Near me · this week'), ('go', 'Show me options')]),
           ('Discover nearby', [('title', 'Near you'), ('ph', 'Map', 120), ('card', 'Morning yoga in the park', 'Event · Saturday · 1.2 km'), ('card', 'Breathwork coach', 'Coach · online or in person'), ('card', 'Neighborhood spa', 'Place · open now')]),
           ('Coach profile', [('ph', 'Photo', 110), ('title', 'Breathwork coach'), ('hint', 'Sessions: 1-on-1 · small group'), ('card', 'Next session', 'Thursday · 6 pm'), ('ghost', 'Save'), ('go', 'Book a session')])],
  progress=[(1, 'Concept and feature list'), (1, 'Name and tagline chosen'), (1, 'Mock brand mark'), (0, 'Interviews with wellness seekers and providers'), (0, 'Map local supply in one area'), (0, 'Prototype the survey and discovery flow')],
  qs=['How does it stay curated instead of becoming another directory?', 'How do coaches and places join, and how is quality checked?', 'Which matters more at first: nearby places or matched coaches?']),
]
for d in DISC:
    k = d['k']
    demo = d.get('demo')
    b = hero(k, d['tag'], (f'<i class="dot"></i>{E(d["stage"])}' if demo else f'In discovery · {E(d["stage"])}'), d['facts'],
             f'<a class="btn gold" href="{demo}">Try the demo ↗</a>' if demo else '')
    b += pair('The problem', d['problem'], 'Hypothesis', d['hyp'])
    b += steps('How it works', d['note'], [(f'0{i+1}', t, x) for i, (t, x) in enumerate(d['how'])], num=True)
    b += grid4(d['feats'])
    b += ('<section class="tile"><div class="sec-head"><h2>Early wireframes</h2><span class="muted" style="font-size:13px">Low fidelity, for testing the flow</span></div><div class="screens" style="--n:3">'
          + ''.join(f'<figure>{wire(bl)}<figcaption>{E(c)}</figcaption></figure>' for c, bl in d['screens']) + '</div></section>')
    b += ('<div class="pair"><section class="tile"><div class="sec-head" style="margin-bottom:18px"><h2 style="font-size:24px">Progress</h2></div><ul class="check">'
          + ''.join(f'<li class="{"done" if ok else ""}"><i>{"✓" if ok else ""}</i><span>{E(t)}</span></li>' for ok, t in d['progress'])
          + '</ul></section><section class="tile"><div class="sec-head" style="margin-bottom:18px"><h2 style="font-size:24px">Open questions</h2></div><ul class="qs">'
          + ''.join(f'<li>{E(q)}</li>' for q in d['qs']) + '</ul></section></div>')
    page(f'work/{k}.html', f'{NAME[k]} case study · Chanel Perez', f'{NAME[k]}: {d["tag"]}', b, back=True)

_unused = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><rect width="100" height="100" rx="22.5" fill="#0B0A09"/><text x="50" y="70" text-anchor="middle" font-family="Georgia,serif" font-size="62" fill="#D8B46A">C</text></svg>')
print('built')
