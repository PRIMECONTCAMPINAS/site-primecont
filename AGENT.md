# 🌐 PRIMECONT - Guia de Manutenção e Diretrizes para Agentes de IA

> **ATENÇÃO PARA AGENTES DE IA (Gemini, Claude, Antigravity, Copilot, etc.):**
> Este workspace é **exclusivo** para a manutenção, evolução e publicação do site institucional oficial da **PRIMECONT Contabilidade e Perícias** (`www.primecont.cnt.br`).
> Antes de realizar qualquer modificação no código ou nos arquivos, **leia e siga rigorosamente as diretrizes abaixo**.

---

## 📁 1. Arquitetura e Estrutura do Projeto

* Todo o código que vai para o ar está contido na pasta **`HTML_STICH/`**.
* **NÃO** edite arquivos fora de `HTML_STICH/` esperando que eles apareçam no site de produção.

### Mapa de Diretórios:
```text
SITE_PRIMECONT/
├── .github/
│   └── workflows/
│       └── deploy.yml            # Pipeline do GitHub Actions para Deploy no GitHub Pages
├── HTML_STICH/                   # 🚨 PASTA RAIZ DO SITE DE PRODUÇÃO
│   ├── CNAME                     # Configuração do domínio oficial (www.primecont.cnt.br)
│   ├── index.html                # Página Principal (Home)
│   ├── quem-somos.html           # Página Quem Somos
│   ├── servicos.html             # Página de Serviços
│   ├── diferenciais.html         # Página de Diferenciais
│   ├── pericias.html             # Página de Perícias
│   ├── contato.html              # Página de Contato
│   ├── abertura-de-empresa.html  # Landing Page: Abertura de Empresa
│   ├── contabilidade-eleitoral.html # Landing Page: Contabilidade Eleitoral
│   ├── reforma-tributaria.html   # Landing Page: Reforma Tributária
│   ├── declaracao-ir.html        # Landing Page: Declaração de IR
│   ├── favicon.png / favicon.ico # Ícones oficiais da aba (Gaivota Primecont)
│   ├── sitemap.xml               # Mapa do site para indexação no Google
│   ├── robots.txt                # Regras para robôs de busca
│   ├── js/
│   │   └── main.js               # Scripts de menu mobile e interatividade
│   ├── logos/                    # Logos institucionais e parceiros (Omie, Jettax, SCI, etc.)
│   └── Fotos_para_site/          # Fotos e imagens conceituais do site
├── AGENT.md                      # Este guia de diretrizes para IAs
├── CLAUDE.md                     # Link para este guia
├── GEMINI.md                     # Link para este guia
└── README.md                     # Informações de clonagem e repositório
```

---

## 🚀 2. Hospedagem e Fluxo de Deploy

* **Hospedagem:** GitHub Pages (Servidores seguros da GitHub / Microsoft).
* **Repositório Oficial:** `https://github.com/PRIMECONTCAMPINAS/site-primecont`
* **Domínio Oficial de Produção:** `https://www.primecont.cnt.br` (com redirecionamento de `primecont.cnt.br`).
* **Deploy Automático:** Qualquer alteração enviada (`git push`) para a branch **`main`** dispara automaticamente o workflow `.github/workflows/deploy.yml` que publica a pasta `HTML_STICH/` em produção em ~20 segundos.

---

## ⚠️ 3. Melhores Práticas e Regras Inegociáveis

Ao realizar qualquer alteração, o agente de IA **DEVE** respeitar as seguintes regras:

### A. Case Sensitivity e Caminhos de Arquivos (Linux / Web Server)
1. **Sempre use caminhos em minúsculas para pastas:** Exemplo: `logos/...` (nunca `Logos/...`).
2. **Sem espaços ou caracteres especiais em nomes de imagens:** Use hifens para separar palavras (ex: `logo-dorpa.webp`, `logo-sci.webp`, `logo-m365.webp`).
3. **Formatos de imagem preferenciais:** Dê preferência para `.webp` para melhor performance e velocidade de carregamento (Core Web Vitals).

### B. URLs Limpas e Links Relativos
1. **Página Inicial:** Use sempre links relativos de raiz: `href="./"` (nunca `href="home-page.html"` nem `href="index.html"`).
2. **Páginas Internas:** Use `href="servicos.html"`, `href="quem-somos.html"`, etc.
3. **Preservação do CNAME:** O arquivo `HTML_STICH/CNAME` **nunca deve ser deletado** em produção, pois ele mantém o domínio `www.primecont.cnt.br` conectado ao GitHub Pages.

### C. Identidade Visual e Favicon
1. **Favicon:** Toda nova página criada deve conter no `<head>`:
   ```html
   <link rel="icon" type="image/png" href="favicon.png"/>
   <link rel="apple-touch-icon" href="favicon.png"/>
   ```
2. **Logo Superior e Rodapé:** A logo principal deve sempre carregar de `logos/PRINCIPAL HORIZONTAL.webp` com `alt="PRIMECONT"`.
3. **Estilização:** O site utiliza utilitários Tailwind CSS via CDN e tipografias do Google Fonts (`Outfit`, `Plus Jakarta Sans`, `Work Sans`). Mantenha a harmonia das cores institucionais (tons de azul Primecont, ardósia e superfícies claras).

### D. SEO e Meta Tags
Em todas as páginas HTML, mantenha preenchidos:
* `<title>` descritivo e alinhado com a marca.
* `<meta name="description" content="...">`
* `<link rel="canonical" href="https://www.primecont.cnt.br/[pagina].html"/>`
* Tags Open Graph (`og:title`, `og:description`, `og:image`, `og:url`).

---

## 🛠️ 4. Checklist do Agente Após Fazer Alterações

Antes de encerrar sua tarefa, execute esta rotina:

1. [ ] Verificar se todos os caminhos `src` de imagens e `href` de links existem fisicamente na pasta `HTML_STICH/`.
2. [ ] Garantir que o arquivo `HTML_STICH/CNAME` está presente com `www.primecont.cnt.br`.
3. [ ] Executar o commit com mensagem clara (ex: `feat: ...` ou `fix: ...`).
4. [ ] Realizar o `git push origin main` para acionar o GitHub Actions.
5. [ ] Confirmar o sucesso do workflow de deploy via `gh run list --limit 1` ou verificando o status do GitHub Pages.

---
*Documento de governança criado para garantir a estabilidade e qualidade contínua do site PRIMECONT.*
