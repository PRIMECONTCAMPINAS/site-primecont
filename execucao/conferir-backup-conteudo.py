from pathlib import Path
import hashlib
import json
import zipfile

root = Path('HTML_STICH')
backup = Path('execucao/backups/2026-10-05-antes-conteudo-servicos')
files = sorted(p for p in root.rglob('*') if p.is_file())
manifest = {p.as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
with zipfile.ZipFile(backup / 'site-antes.zip') as archive:
    assert archive.testzip() is None
    archived = {name.replace('\\', '/'): name for name in archive.namelist()}
    for name, digest in manifest.items():
        assert name in archived, name
        assert hashlib.sha256(archive.read(archived[name])).hexdigest() == digest, name
(backup / 'manifesto-sha256.json').write_text(json.dumps(manifest, indent=2), encoding='utf8')
(backup / 'RESTAURACAO.md').write_text(
    'Base: 261fbe80ecc4a369b52e395eb0148f12354ea794. Backup integral anterior às melhorias '
    'de abertura e troca de contador. Extrair o ZIP em pasta separada e revisar os arquivos '
    'antes de restaurar. Preservar CNAME, Search Console e Analytics com consentimento. '
    'Se a nova página for publicada, retirar trocar-de-contador.html e o CSS específico '
    'que não existiam nesta base, e recuperar home, serviços, sitemap e js/urls.js anteriores. '
    'Restaurar arquivos não altera os dados já recebidos por Analytics ou Search Console.',
    encoding='utf8')
print(f'Backup íntegro: {len(files)} arquivos conferidos por SHA-256.')
