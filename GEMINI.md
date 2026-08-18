<!-- Diretrizes para Gemini e Google Antigravity -->
# PRIMECONT - Instruções para o Gemini

Consulte o arquivo principal [AGENT.md](./AGENT.md) para todas as regras de negócio, estrutura de pastas e diretrizes de desenvolvimento.

### Resumo Executivo:
* **Pasta de Produção:** Todo o site está localizado em `HTML_STICH/`.
* **Domínio Oficial:** `www.primecont.cnt.br` (preservar sempre `HTML_STICH/CNAME`).
* **Deploy:** Automático via GitHub Pages no `git push origin main`.
* **Regras de Links e Imagens:** 
  * Imagens sempre em `logos/` (minúsculo) e sem espaços nos nomes.
  * Links da Home sempre `href="./"`.
  * Favicon obrigatório em todas as páginas: `favicon.png` e `favicon.ico`.
