# [OTIMIZAÇÃO] converte todas as imagens de img/ para WebP no tamanho certo e atualiza os links nas páginas
import os, re, glob
from PIL import Image
D='/home/claude/site_v5/'
def limite(rel):
    if rel.startswith('img/home/2-faixa'): return 520
    if rel.startswith('img/home/1-hero'): return 760
    if rel.startswith('img/home/3-projetos'): return 1300
    if '/1-capa/' in rel: return 1800
    if '/5-site/desktop' in rel: return 1440
    if '/5-site/celular' in rel: return 780
    return 1400
antes=depois=0
for f in glob.glob(D+'img/**/*.*', recursive=True):
    ext=f.rsplit('.',1)[1].lower()
    if ext not in ('jpg','jpeg','png'): continue
    rel=f.replace(D,''); antes+=os.path.getsize(f)
    im=Image.open(f); im=im.convert('RGBA') if im.mode in ('RGBA','LA','P') and 'A' in im.getbands() else im.convert('RGB')
    m=limite(rel)
    if max(im.size)>m:
        k=m/max(im.size); im=im.resize((round(im.width*k), round(im.height*k)), Image.LANCZOS)
    out=f.rsplit('.',1)[0]+'.webp'; im.save(out,'WEBP',quality=76,method=6); depois+=os.path.getsize(out); os.remove(f)
print(f'imagens: {antes/1e6:.1f} MB -> {depois/1e6:.1f} MB')
rx=re.compile(r'([A-Za-z0-9_-]+)\.(jpg|jpeg|png)(?=["\'`)])')
for h in glob.glob(D+'*.html')+[D+'src/index.src.html']:
    s=open(h).read(); n=len(rx.findall(s)); s=rx.sub(r'\1.webp',s); open(h,'w').write(s); print(os.path.basename(h), n, 'links')
