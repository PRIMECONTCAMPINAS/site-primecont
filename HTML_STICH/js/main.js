(function(){
  const btn = document.getElementById('mobileMenuBtn');
  const closeBtn = document.getElementById('mobileMenuClose');
  const menu = document.getElementById('mobileMenu');
  const backdrop = document.getElementById('mobileMenuBackdrop');
  const drawer = document.getElementById('mobileMenuDrawer');
  const espBtn = document.getElementById('mobileEspBtn');
  const espMenu = document.getElementById('mobileEspMenu');
  const espIcon = document.getElementById('mobileEspIcon');

  function openMenu() {
    menu.classList.remove('pointer-events-none');
    backdrop.classList.remove('opacity-0');
    drawer.classList.remove('translate-x-full');
    document.body.style.overflow = 'hidden';
  }
  function closeMenu() {
    backdrop.classList.add('opacity-0');
    drawer.classList.add('translate-x-full');
    document.body.style.overflow = '';
    setTimeout(() => menu.classList.add('pointer-events-none'), 300);
  }

  btn.addEventListener('click', openMenu);
  closeBtn.addEventListener('click', closeMenu);
  backdrop.addEventListener('click', closeMenu);

  espBtn.addEventListener('click', function(){
    const isOpen = !espMenu.classList.contains('hidden');
    espMenu.classList.toggle('hidden');
    espMenu.classList.toggle('flex');
    espIcon.style.transform = isOpen ? '' : 'rotate(180deg)';
  });
})();
