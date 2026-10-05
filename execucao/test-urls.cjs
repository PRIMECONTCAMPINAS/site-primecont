const fs = require('node:fs');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const source = fs.readFileSync('HTML_STICH/js/urls.js', 'utf8');
function resolve(pathname, search = '?origem=site', hash = '#contato') {
  let result;
  vm.runInNewContext(source, {window: {location: {pathname, search, hash, replace: value => result = value}}});
  return result;
}
assert.equal(resolve('/quem-somos.html'), '/quem-somos?origem=site#contato');
assert.equal(resolve('/index.html'), '/?origem=site#contato');
assert.equal(resolve('/site/contato.html'), '/site/contato?origem=site#contato');
assert.equal(resolve('/quem-somos'), undefined);
assert.equal(resolve('/qualquer.html'), undefined);
assert.equal(resolve('/imagens/logo.webp'), undefined);
console.log('Encaminhamento, parâmetros, fragmentos e ausência de loop aprovados.');
