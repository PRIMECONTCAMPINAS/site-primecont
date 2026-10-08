(() => {
  'use strict';
  const id = 'G-SN5WVRNGPL';
  const key = 'primecont-medicao-v1';
  const disabled = 'ga-disable-' + id;
  let active = false;
  let choice = null;
  let scrolled = false;
  try { choice = localStorage.getItem(key); } catch (_) { /* Sem armazenamento, pedir escolha nesta visita. */ }
  window[disabled] = true;
  const clean = value => {
    try { const url = new URL(value); return url.origin + url.pathname; } catch (_) { return ''; }
  };
  function start() {
    if (active) return;
    active = true;
    window[disabled] = false;
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag('consent', 'default', {
      analytics_storage: 'granted', ad_storage: 'denied',
      ad_user_data: 'denied', ad_personalization: 'denied'
    });
    window.gtag('js', new Date());
    window.gtag('config', id, {
      page_location: clean(location.href), page_referrer: clean(document.referrer),
      allow_google_signals: false, allow_ad_personalization_signals: false
    });
    const script = document.createElement('script');
    script.async = true;
    script.src = 'https://www.googletagmanager.com/gtag/js?id=' + id;
    document.head.appendChild(script);
  }
  function event(name, parameters) {
    if (active && !window[disabled]) window.gtag('event', name, parameters);
  }
  function removeCookies() {
    document.cookie.split(';').forEach(pair => {
      const name = pair.trim().split('=')[0];
      if (!/^_ga($|_)/.test(name)) return;
      const suffix = '; Max-Age=0; path=/; SameSite=Lax';
      document.cookie = name + '=' + suffix;
      const parts = location.hostname.split('.');
      for (let i = 0; i < parts.length - 1; i++) {
        document.cookie = name + '=' + suffix + '; domain=.' + parts.slice(i).join('.');
      }
    });
  }
  function remember(value) {
    try { localStorage.setItem(key, value); } catch (_) { /* A decisão vale apenas nesta página. */ }
    choice = value;
  }
  const box = document.createElement('section');
  box.className = 'pc-medicao';
  box.setAttribute('aria-label', 'Preferências de medição');
  box.innerHTML = '<div><strong>Medição de visitas</strong><p>Podemos usar cookies do Google Analytics para entender as visitas e melhorar o site. Você pode aceitar ou recusar e mudar sua escolha no rodapé. <a href="aviso-de-medicao">Saiba como funciona</a>.</p></div><div class="pc-medicao-acoes"><button type="button" data-pc="accept">Aceitar medição</button><button type="button" data-pc="deny">Recusar</button></div>';
  document.body.appendChild(box);
  box.hidden = choice === 'accepted' || choice === 'denied';
  box.querySelector('[data-pc="accept"]').addEventListener('click', () => {
    remember('accepted'); box.hidden = true; start(); preferences.focus({preventScroll: true});
  });
  box.querySelector('[data-pc="deny"]').addEventListener('click', () => {
    remember('denied'); box.hidden = true; window[disabled] = true;
    removeCookies();
    if (active) location.reload(); else preferences.focus({preventScroll: true});
  });
  const preferences = document.createElement('button');
  preferences.type = 'button';
  preferences.className = 'pc-medicao-preferencias';
  preferences.textContent = 'Preferências de medição';
  preferences.addEventListener('click', () => {
    box.hidden = false; box.querySelector('[data-pc="accept"]').focus({preventScroll: true});
  });
  const controls = document.createElement('div');
  controls.className = 'pc-medicao-rodape';
  const notice = document.createElement('a');
  notice.href = 'aviso-de-medicao'; notice.textContent = 'Aviso sobre medição de visitas';
  controls.append(notice, preferences);
  (document.querySelector('footer') || document.body).appendChild(controls);
  if (choice === 'accepted') start();
  document.addEventListener('click', e => {
    const link = e.target.closest('a[href]');
    if (!link) return;
    let category;
    try {
      const url = new URL(link.href);
      if (url.protocol === 'mailto:') category = 'email';
      else if (url.protocol === 'tel:') category = 'telefone';
      else if (url.hostname === 'wa.me' || url.hostname === 'api.whatsapp.com') category = 'whatsapp';
      else if (/^https?:$/.test(url.protocol) && url.hostname !== location.hostname) category = 'externo';
    } catch (_) { return; }
    if (category) event(category === 'externo' ? 'outbound_click' : 'contact_click', { contact_method: category, transport_type: 'beacon' });
  });
  window.addEventListener('scroll', () => {
    if (scrolled || !active) return;
    const height = document.documentElement.scrollHeight - window.innerHeight;
    if (height > 0 && window.scrollY / height >= 0.9) {
      scrolled = true; event('scroll', { percent_scrolled: 90 });
    }
  }, { passive: true });
  window.addEventListener('storage', e => {
    if (e.key !== key) return;
    if (e.newValue === 'accepted') { choice = e.newValue; box.hidden = true; start(); }
    else { window[disabled] = true; removeCookies(); location.reload(); }
  });
})();
