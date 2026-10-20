"""Gera identidade-visual.html (landing page) a partir de src/identidade-visual.src.html.
Rode: python src/lp_iv.py   (também gera a imagem de compartilhamento img/og/og-identidade-visual.jpg)"""
import os, re
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/'
idx = open(R + 'index.html').read()
logo = re.search(r'<a class="logo"[^>]*>(<svg class="marca".*?</svg>)</a>', idx, re.S).group(1)
src = open(R + 'src/identidade-visual.src.html').read().replace('{{LOGO}}', logo)
open(R + 'identidade-visual.html', 'w').write(src)
print('identidade-visual.html ok')
sm = open(R + 'sitemap.xml').read()
if '/identidade-visual<' not in sm:
    lm = re.search(r'<lastmod>([^<]+)', sm).group(1)
    sm = sm.replace('</urlset>', f'  <url><loc>https://turzindesign.com.br/identidade-visual</loc><lastmod>{lm}</lastmod><changefreq>monthly</changefreq><priority>0.9</priority></url>\n</urlset>')
    open(R + 'sitemap.xml', 'w').write(sm); print('sitemap ok')
try:
    from playwright.sync_api import sync_playwright
    lg = open(R + 'img/marca/logotipo.svg').read().replace('<svg ', '<svg style="width:100%;height:auto;display:block" ', 1)
    fonte = f"@font-face{{font-family:B;font-weight:200 800;font-stretch:75% 100%;src:url(file://{R}fonts/bricolage-latin.woff2)}}"
    tmp = R + '_og_tmp.html'
    open(tmp, 'w').write(f'''<html><head><meta charset="utf-8"><style>{fonte}*{{margin:0}}body{{width:1200px;height:630px;overflow:hidden;font-family:B;background:#212121;color:#F7F7F7}}.t,.s{{fill:#F7F7F7}}.d{{fill:#44D62D}}</style></head><body>
<div style="position:absolute;left:0;top:0;width:520px;height:630px;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:10px;padding:10px">
<img src="file://{R}img/isabella/4-aplicacoes/cartao.webp" style="width:100%;height:100%;object-fit:cover"><img src="file://{R}img/acai-yo/3-tipografia/embalagem-acai.webp" style="width:100%;height:100%;object-fit:cover">
<img src="file://{R}img/margarett/1-capa/sacola.webp" style="width:100%;height:100%;object-fit:cover"><img src="file://{R}img/reigotta/4-aplicacoes/post-novos-ciclos.webp" style="width:100%;height:100%;object-fit:cover"></div>
<div style="position:absolute;left:580px;top:70px;width:220px">{lg}</div>
<div style="position:absolute;left:580px;bottom:150px;font:800 84px/.9 B;text-transform:uppercase;font-variation-settings:'wdth' 76">Identidade<br>visual<span style="display:inline-block;width:.16em;height:.16em;background:#44D62D;margin-left:.05em"></span></div>
<div style="position:absolute;left:584px;bottom:80px;font:500 26px B;color:rgba(247,247,247,.75)">Sua marca pronta em até 5 dias.</div></body></html>''')
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1200, 'height': 630})
        pg.goto('file://' + tmp); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(500)
        pg.screenshot(path=R + 'img/og/og-identidade-visual.jpg', type='jpeg', quality=86); b.close()
    os.remove(tmp); print('og ok')
except ImportError:
    print('playwright não instalado: imagem de compartilhamento não gerada')
