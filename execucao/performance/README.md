# Estilos de produção

A home e a página de abertura de empresa usam CSS compilado com Tailwind 3.4.17. As demais páginas ainda usam a configuração anterior. A configuração de cores e fontes fica no bloco JSON `tailwind-config` de cada HTML.

Ao alterar classes nessas duas páginas ou em `HTML_STICH/js/main.js`, execute nesta pasta:

```powershell
npm install
npm run build
```

Revise o visual em celular e desktop e publique os HTML e os dois arquivos de `HTML_STICH/css/` juntos. Atualize a versão no link CSS quando mudar os estilos. O CSS fica salvo no repositório: a hospedagem não precisa executar Node ou Tailwind.

O script aceita como argumento um diretório `node_modules` já instalado com essas mesmas versões. Os arquivos em `generated/` e `node_modules/` não são publicados.
