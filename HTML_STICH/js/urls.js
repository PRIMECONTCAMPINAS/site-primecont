(function () {
  const pages = ['quem-somos', 'servicos', 'diferenciais', 'pericias', 'contato',
    'abertura-de-empresa', 'trocar-de-contador', 'contabilidade-eleitoral', 'reforma-tributaria', 'declaracao-ir'];
  const path = window.location.pathname;
  const filename = path.slice(path.lastIndexOf('/') + 1);
  if (!filename.endsWith('.html')) return;
  const page = filename.slice(0, -5);
  if (page !== 'index' && !pages.includes(page)) return;
  const directory = path.slice(0, path.lastIndexOf('/') + 1);
  const destination = directory + (page === 'index' ? '' : page);
  window.location.replace(destination + window.location.search + window.location.hash);
})();
