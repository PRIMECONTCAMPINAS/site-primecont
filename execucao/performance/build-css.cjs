const fs = require('node:fs');
const path = require('node:path');
const {execFileSync} = require('node:child_process');

const root = path.resolve(__dirname, '../../HTML_STICH');
const modules = process.argv[2] ? path.resolve(process.argv[2]) : path.join(__dirname, 'node_modules');
const generated = path.join(__dirname, 'generated');
fs.mkdirSync(generated, {recursive: true});
fs.mkdirSync(path.join(root, 'css'), {recursive: true});

for (const page of ['index.html', 'abertura-de-empresa.html']) {
  const html = fs.readFileSync(path.join(root, page), 'utf8');
  const match = html.match(/<script id="tailwind-config" type="application\/json">([\s\S]*?)<\/script>/);
  if (!match) throw new Error('Configuração Tailwind ausente: ' + page);
  const config = {...JSON.parse(match[1]), content: [path.join(root, page), path.join(root, 'js/main.js')]};
  const configPath = path.join(generated, page + '.config.cjs');
  fs.writeFileSync(configPath, 'module.exports=' + JSON.stringify(config) + ';\nmodule.exports.plugins=[' +
    ['@tailwindcss/forms', '@tailwindcss/container-queries'].map(name => 'require(' + JSON.stringify(path.join(modules, name)) + ')').join(',') + '];\n');
  execFileSync(process.execPath, [path.join(modules, 'tailwindcss/lib/cli.js'), '-c', configPath,
    '-i', path.join(__dirname, 'input.css'), '-o', path.join(root, 'css', page.replace('.html', '.css'))], {stdio: 'inherit'});
}
