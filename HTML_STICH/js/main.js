(function(){
  const btn = document.getElementById('mobileMenuBtn');
  const closeBtn = document.getElementById('mobileMenuClose');
  const menu = document.getElementById('mobileMenu');
  const backdrop = document.getElementById('mobileMenuBackdrop');
  const drawer = document.getElementById('mobileMenuDrawer');
  const espBtn = document.getElementById('mobileEspBtn');
  const espMenu = document.getElementById('mobileEspMenu');
  const espIcon = document.getElementById('mobileEspIcon');
  let closeTimer;
  let isOpen = false;
  let previousOverflow = '';

  function openMenu() {
    clearTimeout(closeTimer);
    if (!isOpen) previousOverflow = document.body.style.overflow;
    isOpen = true;
    menu.inert = false;
    btn.setAttribute('aria-expanded', 'true');
    menu.classList.remove('pointer-events-none');
    backdrop.classList.remove('opacity-0');
    drawer.classList.remove('translate-x-full');
    document.body.style.overflow = 'hidden';
    closeBtn.focus({preventScroll: true});
  }
  function closeMenu() {
    if (!isOpen) return;
    isOpen = false;
    btn.setAttribute('aria-expanded', 'false');
    backdrop.classList.add('opacity-0');
    drawer.classList.add('translate-x-full');
    document.body.style.overflow = previousOverflow;
    if (btn.getClientRects().length) btn.focus({preventScroll: true});
    menu.inert = true;
    closeTimer = setTimeout(() => menu.classList.add('pointer-events-none'), 300);
  }

  btn.addEventListener('click', openMenu);
  closeBtn.addEventListener('click', closeMenu);
  backdrop.addEventListener('click', closeMenu);

  espBtn.addEventListener('click', function(){
    const isOpen = !espMenu.classList.contains('hidden');
    espMenu.classList.toggle('hidden');
    espMenu.classList.toggle('flex');
    espIcon.style.transform = isOpen ? '' : 'rotate(180deg)';
    espBtn.setAttribute('aria-expanded', String(!isOpen));
  });

  document.addEventListener('keydown', function(event) {
    if (!isOpen) return;
    if (event.key === 'Escape') {
      event.preventDefault();
      closeMenu();
      return;
    }
    if (event.key !== 'Tab') return;
    const controls = Array.from(drawer.querySelectorAll('a[href], button')).filter(
      element => !element.disabled && element.getClientRects().length
    );
    const first = controls[0];
    const last = controls[controls.length - 1];
    if (event.shiftKey && document.activeElement === first) {
      event.preventDefault();
      last.focus();
    } else if (!event.shiftKey && document.activeElement === last) {
      event.preventDefault();
      first.focus();
    }
  });

  window.matchMedia('(min-width: 1024px)').addEventListener('change', function(event) {
    if (event.matches) closeMenu();
  });
})();
