from pathlib import Path
import re, json, html, zipfile, hashlib

root = Path('HTML_STICH')
spec = Path('docs/superpowers/specs/2026-10-05-conteudo-abertura-troca-design.md').read_text(encoding='utf8')
backup = Path('execucao/backups/2026-10-05-antes-conteudo-servicos')
manifest = json.loads((backup/'manifesto-sha256.json').read_text())
for name, digest in manifest.items():
    assert hashlib.sha256(Path(name).read_bytes()).hexdigest() == digest, f'Base mudou: {name}'
opening, swap = spec.split('## Texto proposto — abertura de empresa')[1].split('## Texto proposto — troca de contador')
swap = swap.split('## Fontes oficiais consultadas')[0]
def section(text, name):
    return text.split('### '+name+'\n\n')[1].split('\n### ')[0]
def esc(s): return html.escape(s, quote=True)
def block(title, body, shade=False):
    return f'<section class="service-content{" service-content-shade" if shade else ""}"><div class="service-container"><h2>{esc(title)}</h2>{body}</div></section>\n'
def paras(text): return ''.join('<p>'+esc(p)+'</p>' for p in text.strip().split('\n\n'))
def list_content(text):
    pieces=text.strip().split('\n\n'); out=''
    for piece in pieces:
        if piece.startswith('- '): out+='<ul class="service-checklist">'+''.join('<li>'+esc(line[2:])+'</li>' for line in piece.splitlines())+'</ul>'
        else: out+=paras(piece)
    return out
def faq(text):
    pairs=re.findall(r'\*\*(.+?)\*\* (.+)', section(text,'Perguntas frequentes'))
    assert len(pairs)==5
    return block('Perguntas frequentes','<div class="service-faq">'+''.join('<details><summary>'+esc(q)+'</summary><p>'+esc(a)+'</p></details>' for q,a in pairs)+'</div>')
csslink='<link rel="stylesheet" href="css/conteudo-servicos.css?v=20261005"/>\n'
p=root/'abertura-de-empresa.html'; original=p.read_text(encoding='utf8'); content=original
old='Abra sua empresa com segurança e agilidade. A PRIMECONT cuida de todo o processo: CNPJ, enquadramento tributário, alvarás e muito mais.'
desc=re.search(r'Descrição: (.+)', opening)[1]
content=content.replace(old,desc).replace('</head>',csslink+'</head>')
content=content.replace('<main class="site-main">','<main class="site-main service-page">')
content=content.replace('Abra ou regularize sua empresa com mais segurança, clareza e apoio em cada etapa.','Abertura de empresa em Campinas.')
intro=re.search(r'Introdução da hero: (.+)',opening)[1]
content=content.replace('</h1>','</h1><p class="service-hero-lead">'+esc(intro)+'</p>',1)
replacements={
 'Um alinhamento sólido entre a visão societária e a conformidade institucional para garantir o crescimento sustentável do seu negócio.':'Atividade, endereço e composição dos sócios precisam ser avaliados em conjunto para orientar os registros e as exigências da abertura.',
 'Apoio Societário e Cadastral de Excelência':'Apoio para os registros da sua empresa',
 'Nossa equipe técnica atua na linha de frente dos processos burocráticos, garantindo que as decisões societárias sejam refletidas com exatidão nos registros públicos. Atuamos em Juntas Comerciais, Receita Federal e Prefeituras com agilidade institucional.':'A PRIMECONT orienta a preparação dos documentos e acompanha os procedimentos de registro, conforme a estrutura da empresa e os órgãos competentes.',
 'Do enquadramento tributário inicial à definição da estrutura de capital, cada detalhe é revisado por especialistas. Não entregamos apenas documentos; entregamos a tranquilidade de saber que sua empresa está operando sob as melhores práticas do mercado.':'O atendimento considera a atividade e a composição societária para orientar as decisões iniciais. O escopo dos serviços é esclarecido na proposta, de acordo com as necessidades do negócio.',
 'Processo estruturado de ponta a ponta para novos negócios. Consultoria prévia, registro em todos os órgãos e licenças de funcionamento inclusas.':'Orientação inicial, organização da documentação e acompanhamento dos registros e das exigências de licenciamento aplicáveis. O escopo do atendimento é definido na proposta.',
 'Suporte especializado disponível para tirar dúvidas em tempo real durante todo o processo.':'Orientação para esclarecer dúvidas e acompanhar os próximos passos durante o processo.',
 'Conformidade total com a LGPD e normas contábeis internacionais.':'Atenção à organização dos documentos e às exigências aplicáveis à atividade da empresa.',
 'Jornada de Condução Institucional':'Etapas da abertura de empresa',
 'Abrir minha Empresa':'Abrir minha empresa',
 'Limpeza de restrições e pendências em órgãos governamentais.':'Análise e encaminhamento de pendências cadastrais nos órgãos competentes.'}
for a,b in replacements.items():
    assert a in content,a
    content=content.replace(a,b)
steps=re.findall(r'^\d\. (.+?): (.+)$',section(opening,'Etapas da abertura de empresa'),re.M)
assert len(steps)==5
for n,(title,body) in enumerate(steps):
    pattern=rf'(<div class="relative pt-16 group timeline-step" data-step="{n}">.*?<h3[^>]*>)(.*?)(</h3>\s*<p[^>]*>)(.*?)(</p>)'
    content,count=re.subn(pattern,lambda m:m[1]+esc(title)+m[3]+esc(body)+m[5],content,flags=re.S)
    assert count==1
content=content.replace('opacity: 0;\n    transform: translateY(10px);','opacity: 1;\n    transform: none;')
note='Essas etapas podem ser integradas pelos sistemas públicos e variam conforme o tipo de empresa e a atividade. O CNPJ é uma parte do processo; as condições para começar a operar precisam ser verificadas.'
content=content.replace('<h2 class="font-headline text-4xl font-bold text-white mb-20 text-center">Etapas da abertura de empresa</h2>', '<h2 class="font-headline text-4xl font-bold text-white mb-20 text-center">Etapas da abertura de empresa</h2><p class="service-timeline-note">'+note+'</p>')
check=section(opening,'O que precisamos entender antes de começar')
content=content.replace('<!-- Block 06: Process Timeline -->',block('O que precisamos entender antes de começar',list_content(check))+'<!-- Block 06: Process Timeline -->')
cost=section(opening,'Prazo e custo: o que influencia a abertura')
sources='<p class="service-source">Conteúdo institucional da PRIMECONT · Atualizado em 05/10/2026. Referências: <a href="https://www.gov.br/empresas-e-negocios/pt-br/redesim/abrir-cnpj" target="_blank" rel="noopener noreferrer">REDESIM</a> e <a href="https://portal-adm.campinas.sp.gov.br/servico/solicitar-alvara-de-uso" target="_blank" rel="noopener noreferrer">Prefeitura de Campinas</a>.</p>'
extra=block('Prazo e custo: o que influencia a abertura',paras(cost),True)+faq(opening)+block('Sua empresa já está aberta?','<p>Conheça nossos <a href="servicos">serviços contábeis</a> ou veja como a PRIMECONT orienta a <a href="trocar-de-contador">troca de contador em Campinas</a>.</p>'+sources,True)
content=content.replace('<!-- Block 09: Final CTA -->',extra+'<!-- Block 09: Final CTA -->') if '<!-- Block 09: Final CTA -->' in content else content.replace('</main>',extra+'</main>')
p.write_text(content,encoding='utf8')
# Reuse the existing head, navigation, hero composition, footer, logos and integrations.
head=content.split('<main class="site-main service-page">')[0]
head=head.replace('Abertura de Empresa em Campinas | PRIMECONT','Trocar de Contador em Campinas | PRIMECONT').replace(desc,re.search(r'Descrição: (.+)',swap)[1])
head=head.replace('https://www.primecont.cnt.br/abertura-de-empresa','https://www.primecont.cnt.br/trocar-de-contador')
head=head.replace('"name": "Abertura de Empresa em Campinas"','"name": "Troca de Contador em Campinas"').replace('"serviceType": "Abertura de Empresa"','"serviceType": "Troca de Contador"')
# New page uses only verified provider data; no duplicate local coordinates or price claims.
head=re.sub(r'<script type="application/ld\+json">\s*\{.*?"@type": "AccountingService".*?</script>\s*','',head,count=1,flags=re.S)
hero=content.split('<!-- Block 01: Hero -->')[1].split('<!-- Block 02: Intro -->')[0]
hero=hero.replace('Abertura de empresa em Campinas.','Trocar de contador em Campinas.').replace(esc(intro),esc(re.search(r'Introdução: (.+)',swap)[1]))
hero=hero.replace('Abrir minha empresa','Conversar sobre a troca de contador').replace('quero%20abrir%20uma%20empresa.','quero%20trocar%20de%20contador.')
hero=re.sub(r'<a href="https://wa.me/551932535083\?text=Quero%20Regularizar%20minha%20Empresa".*?</a>','',hero,flags=re.S)
hero=hero.replace('alt="Abertura de empresa PRIMECONT"','alt="Ilustração institucional PRIMECONT"')
body=block('Quando considerar a troca',paras(section(swap,'Quando considerar a troca')))
transition=section(swap,'O que observar na transição')
items=re.findall(r'^\d\. (.+?): (.+)$',transition,re.M)
assert len(items)==4
body+=block('O que observar na transição','<ol class="service-steps">'+''.join('<li><h3>'+esc(t)+'</h3><p>'+esc(b)+'</p></li>' for t,b in items)+'</ol>'+paras(transition.split('\n\n')[-1]),True)
info=section(swap,'Informações úteis para conversar com a equipe').split('\n\nA equipe orienta')[0]
body+=block('Informações úteis para conversar com a equipe',list_content(info)+'<p>A equipe orienta a documentação necessária conforme o caso.</p>')+faq(swap)
body+=block('Vamos conversar sobre o atendimento da sua empresa?','<p>Conheça também nossos <a href="servicos">serviços contábeis</a> e o apoio à <a href="abertura-de-empresa">abertura de empresa em Campinas</a>.</p><a class="service-button" href="https://wa.me/551932535083?text=Ol%C3%A1%2C%20quero%20conversar%20sobre%20a%20troca%20de%20contador." target="_blank" rel="noopener noreferrer">Falar com a PRIMECONT</a><p class="service-source">Conteúdo institucional da PRIMECONT · Atualizado em 05/10/2026. Referência informativa: <a href="https://www.crcsp.org.br/portal/fiscalizacao/contrate.htm" target="_blank" rel="noopener noreferrer">CRCSP — contrato de prestação de serviços</a>.</p>',True)
tail=content.split('</main>')[1]
(root/'trocar-de-contador.html').write_text(head+'<main class="site-main service-page">'+hero+body+'</main>'+tail,encoding='utf8')
p=root/'index.html'; s=p.read_text(encoding='utf8')
s,n=re.subn(r'href="https://wa.me/551932535083\?text=Ol%C3%A1%2C%20vim%20pelo%20site%20da%20PRIMECONT%20e%20quero%20trocar%20de%20contabilidade\." target="_blank" rel="noopener noreferrer"','href="trocar-de-contador"',s); assert n==1
p.write_text(s,encoding='utf8')
p=root/'servicos.html'; s=p.read_text(encoding='utf8'); assert '</main>' in s
s=s.replace('</head>',csslink+'</head>').replace('</main>',block('Pensando em trocar de contador?','<p>Veja o que observar na transição e como a PRIMECONT pode orientar sua empresa. <a href="trocar-de-contador">Conheça a troca de contador em Campinas</a>.</p>',True)+'</main>')
p.write_text(s,encoding='utf8')
p=root/'js/urls.js'; s=p.read_text().replace("'abertura-de-empresa',", "'abertura-de-empresa', 'trocar-de-contador',"); p.write_text(s,encoding='utf8')
p=root/'sitemap.xml'; s=p.read_text().replace('</urlset>','  <url>\n    <loc>https://www.primecont.cnt.br/trocar-de-contador</loc>\n    <lastmod>2026-10-05</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.8</priority>\n  </url>\n</urlset>'); p.write_text(s,encoding='utf8')
print('Conteúdo aplicado: abertura, troca, home, serviços, sitemap e URLs.')
