# Innova Space

Chanel's portfolio at https://innovaspace.app: a bento home, About and CV, Contact, and a case study for each product (Nudge!, Noggin, Drift, AuraSync).

- Pages are generated: edit `scripts/build.py`, run `python3 scripts/build.py`, commit `public/`.
- Styles and the theme toggle: `public/assets/site.css`, `public/assets/site.js`.
- `worker/index.js` serves the pages and `/api/contact`, which emails hello.innovaspace@gmail.com through Email Routing.

Push to `main` and Cloudflare deploys it.
