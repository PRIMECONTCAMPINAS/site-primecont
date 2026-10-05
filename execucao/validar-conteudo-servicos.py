from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import json, xml.etree.ElementTree as ET

root=Path('HTML_STICH')
class Page(HTMLParser):
    def __init__(self): super().__init__(); self.refs=[]; self.h1=0; self.details=0
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        self.h1+=tag=='h1'; self.details+=tag=='details'
        for key in ('href','src'):
            if a.get(key): self.refs.append(a[key])
        if a.get('srcset'):
            self.refs.extend(item.strip().split()[0] for item in a['srcset'].split(','))
errors=[]; refs=0
for name in ('index','servicos','abertura-de-empresa','trocar-de-contador'):
    text=(root/(name+'.html')).read_text(encoding='utf8'); page=Page(); page.feed(text)
    assert page.h1==1,(name,page.h1)
    if name in ('abertura-de-empresa','trocar-de-contador'):
        assert page.details==5
        for claim in ('licenças de funcionamento inclusas','dúvidas em tempo real','Conformidade total'):
            assert claim not in text
    import re
    for data in re.findall(r'<script type="application/ld\+json">(.*?)</script>',text,re.S): json.loads(data)
    assert 'js/analytics.js' in text and 'css/navigation.css' in text
    for ref in page.refs:
        u=urlsplit(ref)
        if u.scheme or u.netloc or not u.path: continue
        refs+=1; target=root/unquote(u.path)
        if not target.exists() and not Path(str(target)+'.html').exists(): errors.append((name,ref))
assert not errors,errors
assert (root/'CNAME').read_text().strip()=='www.primecont.cnt.br'
sitemap=ET.parse(root/'sitemap.xml')
locations=[node.text for node in sitemap.findall('.//{*}loc')]
assert len(locations)==len(set(locations))==11
assert 'https://www.primecont.cnt.br/trocar-de-contador' in locations
print(f'Validação OK: 4 páginas, {refs} referências locais, JSON-LD válido, 11 URLs no sitemap.')
