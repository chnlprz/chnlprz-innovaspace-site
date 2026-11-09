// Theme: follows the device until you pick one; your pick is remembered on this browser.
(function () {
  var root = document.documentElement;
  var btn = document.querySelector('.theme-btn');
  function current() {
    var t = root.getAttribute('data-theme');
    if (t) return t;
    return window.matchMedia && matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }
  function label() { if (btn) btn.setAttribute('aria-label', current() === 'dark' ? 'Switch to light theme' : 'Switch to dark theme'); }
  label();
  if (btn) btn.addEventListener('click', function () {
    var next = current() === 'dark' ? 'light' : 'dark';
    root.setAttribute('data-theme', next);
    try { localStorage.setItem('theme', next); } catch (e) {}
    label();
  });

  // Contact form: sends to Innova Space without opening an email app.
  var form = document.getElementById('contact-form');
  if (!form) return;
  var started = Date.now();
  var msg = document.getElementById('form-status');
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var data = Object.fromEntries(new FormData(form).entries());
    data.elapsed = Date.now() - started;
    if (!data.name || !data.email || !data.message) { msg.textContent = 'Please fill in your name, email and message. Nothing was sent yet.'; return; }
    var b = form.querySelector('button[type="submit"]');
    b.disabled = true; b.textContent = 'Sending…'; msg.textContent = '';
    fetch('/api/contact', { method: 'POST', headers: { 'content-type': 'application/json' }, body: JSON.stringify(data) })
      .then(function (r) { return r.json().then(function (j) { return { ok: r.ok, j: j }; }); })
      .then(function (res) {
        if (res.ok) { form.reset(); msg.textContent = 'Thank you! Your message is on its way. I usually reply within two days.'; b.textContent = 'Sent'; return; }
        throw new Error(res.j && res.j.error);
      })
      .catch(function () {
        b.disabled = false; b.textContent = 'Send message';
        msg.innerHTML = 'That didn’t send this time. Your message is still here. Try again, or email <a href="mailto:hello@innovaspace.app"><u>hello@innovaspace.app</u></a>.';
      });
  });
})();
