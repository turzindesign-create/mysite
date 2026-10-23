"""
turzin. · SEO
Coloca nas páginas: descrição, endereço canônico, imagem de compartilhamento (Open Graph),
dados estruturados para o Google (JSON-LD), ícones e gera sitemap.xml e robots.txt.

Rode depois de gerar o site (build.py e gerar_cases_v5.py):  python src/seo.py
É seguro rodar várias vezes: o bloco entre <!-- seo --> e <!-- /seo --> é trocado inteiro.
"""
import os, re, json, html, datetime
from playwright.sync_api import sync_playwright

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/'
DOM = 'https://turzindesign.com.br'
HOJE = datetime.date.today().isoformat()
INSTA = ''   # cole aqui o link do Instagram da turzin. (ex.: https://www.instagram.com/seuperfil/) e rode de novo

MARCA = {'@type': 'ProfessionalService', '@id': DOM + '/#turzin', 'name': 'turzin.', 'alternateName': 'turzin design',
         'url': DOM + '/', 'logo': DOM + '/img/marca/simbolo-512.png', 'image': DOM + '/img/og/og-home.jpg',
         'description': 'Engenharia de design e tecnologia: identidade visual e sites para pequenos negócios. Do papel à tela, design como função.',
         'email': 'turzindesign@gmail.com', 'areaServed': {'@type': 'Country', 'name': 'Brasil'},
         'knowsAbout': ['Identidade visual', 'Branding', 'Criação de logotipo', 'Design de embalagem', 'Criação de sites', 'Design de interface'],
         'hasOfferCatalog': {'@type': 'OfferCatalog', 'name': 'Serviços', 'itemListElement': [
             {'@type': 'Offer', 'itemOffered': {'@type': 'Service', 'name': 'Identidade visual', 'description': 'Consultoria de mercado; símbolo, paleta de cores e tipografia; grafismos; animações; aplicações digitais e físicas; voz da marca; manual da marca. Pronta em 7 dias.'}},
             {'@type': 'Offer', 'itemOffered': {'@type': 'Service', 'name': 'Identidade visual + site', 'description': 'Identidade visual completa (consultoria de mercado, símbolo, cores, tipografia, grafismos, animações, aplicações, voz e manual da marca) com site e manual de uso do site.'}}]}}

if INSTA: MARCA['sameAs'] = [INSTA]

PAGINAS = {
    'index.html': dict(url='/', og='og-home.jpg', titulo_og='turzin. · Identidade visual e sites',
        desc='turzin. é engenharia de design e tecnologia: identidade visual, branding e sites para pequenos negócios. Veja os projetos e peça seu orçamento.'),
}
CASES = {
    'isabella': ('Isabella Gutierres', 'psicóloga de relacionamentos', 'img/isabella/1-capa/almofada.webp'),
    'margarett': ('Margarett', 'hamburgueria artesanal', 'img/margarett/1-capa/sacola.webp'),
    'acai-yo': ('Açaí Yo', 'açaíteria', 'img/acai-yo/1-capa/outdoor.webp'),
    'reigotta': ('Reigotta', 'e-commerce de moda fitness feminina', 'img/reigotta/1-capa/sacola.webp'),
    'kamisama': ('Kamisama', 'delivery de comida japonesa', 'img/kamisama/1-capa/sushi.webp'),
}
for slug, (nome, seg, capa) in CASES.items():
    PAGINAS[slug + '.html'] = dict(url='/' + slug, og=f'og-{slug}.jpg', titulo_og=f'{nome} · Estudo de caso · turzin.', capa=capa, nome=nome, seg=seg,
        desc=f'Estudo de caso da identidade visual de {nome}, {seg}: do problema ao símbolo, cores, tipografia e aplicações. Projeto da turzin.')


def bloco(arq, p):
    url = DOM + p['url']; og = DOM + '/img/og/' + p['og']
    t = html.escape(p['titulo_og']); d = html.escape(p['desc'])
    if arq == 'index.html':
        ld = {'@context': 'https://schema.org', '@graph': [MARCA, {'@type': 'WebSite', '@id': DOM + '/#site', 'url': DOM + '/', 'name': 'turzin.', 'inLanguage': 'pt-BR', 'publisher': {'@id': DOM + '/#turzin'}}]}
    else:
        ld = {'@context': 'https://schema.org', '@graph': [
            {'@type': 'CreativeWork', '@id': url + '#caso', 'name': f"Identidade visual {p['nome']}", 'headline': p['titulo_og'], 'description': p['desc'],
             'url': url, 'image': og, 'inLanguage': 'pt-BR', 'genre': 'Identidade visual', 'about': f"{p['nome']}, {p['seg']}",
             'creator': {'@id': DOM + '/#turzin'}, 'publisher': {'@id': DOM + '/#turzin'}},
            {'@type': 'BreadcrumbList', 'itemListElement': [
                {'@type': 'ListItem', 'position': 1, 'name': 'turzin.', 'item': DOM + '/'},
                {'@type': 'ListItem', 'position': 2, 'name': p['nome'], 'item': url}]},
            {**{k: MARCA[k] for k in ('@type', '@id', 'name', 'url', 'logo')}}]}
    return f'''<!-- seo -->
<meta name="description" content="{d}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="author" content="turzin.">
<meta name="theme-color" content="#212121">
<link rel="icon" href="/img/marca/favicon-32.png" type="image/png" sizes="32x32">
<link rel="apple-touch-icon" href="/img/marca/apple-touch-icon.png">
<meta property="og:type" content="{'website' if arq == 'index.html' else 'article'}">
<meta property="og:site_name" content="turzin.">
<meta property="og:locale" content="pt_BR">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{d}">
<meta property="og:image" content="{og}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{t}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{t}">
<meta name="twitter:description" content="{d}">
<meta name="twitter:image" content="{og}">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<!-- /seo -->'''


def aplica():
    for arq, p in PAGINAS.items():
        s = open(R + arq).read()
        s = re.sub(r'\n?<!-- seo -->.*?<!-- /seo -->', '', s, flags=re.S)
        s = re.sub(r'\n?<meta name="description"[^>]*>', '', s, count=1)
        s = s.replace('</title>', '</title>\n' + bloco(arq, p), 1)
        open(R + arq, 'w').write(s)
        print('seo ok', arq)


def sitemap():
    urls = [('/', '1.0', 'monthly')] + [('/' + k, '0.8', 'yearly') for k in CASES]
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(
        f'  <url><loc>{DOM}{u}</loc><lastmod>{HOJE}</lastmod><changefreq>{c}</changefreq><priority>{pr}</priority></url>\n' for u, pr, c in urls) + '</urlset>\n'
    open(R + 'sitemap.xml', 'w').write(xml)
    open(R + 'robots.txt', 'w').write(f'User-agent: *\nAllow: /\n\nSitemap: {DOM}/sitemap.xml\n')
    print('sitemap.xml e robots.txt ok')


def imagens():
    os.makedirs(R + 'img/og', exist_ok=True)
    simb = open(R + 'img/marca/simbolo.svg').read().replace('<svg ', '<svg style="width:100%;height:auto;display:block" ', 1)
    logo = open(R + 'img/marca/logotipo.svg').read().replace('<svg ', '<svg style="width:100%;height:auto;display:block" ', 1)
    fonte = f"@font-face{{font-family:B;font-weight:200 800;font-stretch:75% 100%;src:url(file://{R}fonts/bricolage-latin.woff2)}}"
    with sync_playwright() as pw:
        b = pw.chromium.launch(); pg = b.new_page(viewport={'width': 1200, 'height': 630})
        def foto(nome, corpo):
            tmp = R + '_og_tmp.html'
            open(tmp, 'w').write(f'<html><head><meta charset="utf-8"><style>{fonte}*{{margin:0}}body{{width:1200px;height:630px;overflow:hidden;font-family:B,sans-serif}}.t{{fill:#F7F7F7}}.d{{fill:#44D62D}}.s{{fill:#F7F7F7}}</style></head><body>{corpo}</body></html>')
            pg.goto('file://' + tmp); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(400); os.remove(tmp)
            pg.screenshot(path=R + 'img/og/' + nome, type='jpeg', quality=86)
        # home
        foto('og-home.jpg', f'''<div style="position:relative;width:1200px;height:630px;background:#212121;color:#F7F7F7">
          <div style="position:absolute;inset:0;background-image:linear-gradient(rgba(247,247,247,.07) 1px,transparent 1px),linear-gradient(90deg,rgba(247,247,247,.07) 1px,transparent 1px);background-size:60px 60px"></div>
          <div style="position:absolute;right:70px;top:80px;width:330px">{simb.replace('class="s"', 'class="s" style="fill:#2E2E2E"')}</div>
          <div style="position:absolute;left:80px;top:80px;width:260px">{logo}</div>
          <div style="position:absolute;left:80px;bottom:150px;font:800 92px/.9 B;text-transform:uppercase;font-variation-settings:'wdth' 76;letter-spacing:-.01em">Identidade visual<br>e sites<span style="display:inline-block;width:.16em;height:.16em;background:#44D62D;margin-left:.05em"></span></div>
          <div style="position:absolute;left:84px;bottom:80px;font:500 26px B;color:rgba(247,247,247,.75)">Do papel à tela. Design como função.</div></div>''')
        # cases
        for slug, (nome, seg, capa) in CASES.items():
            foto(f'og-{slug}.jpg', f'''<div style="position:relative;width:1200px;height:630px;background:#212121">
              <img src="file://{R}{capa}" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover">
              <div style="position:absolute;left:40px;bottom:40px;background:#212121;color:#F7F7F7;padding:26px 30px;display:grid;gap:10px;max-width:760px">
               <span style="font:600 18px B;letter-spacing:.12em;text-transform:uppercase;color:#44D62D">Estudo de caso · identidade visual</span>
               <b style="font:800 64px/.95 B;text-transform:uppercase;font-variation-settings:'wdth' 78">{html.escape(nome)}</b>
               <div style="width:150px;margin-top:6px">{logo}</div></div></div>''')
        # ícones
        for nome, tam in [('favicon-32.png', 32), ('apple-touch-icon.png', 180), ('simbolo-512.png', 512)]:
            pg.set_viewport_size({'width': tam, 'height': tam})
            pg.set_content(f'<html><body style="margin:0;width:{tam}px;height:{tam}px;background:{"#212121" if tam > 32 else "transparent"};display:grid;place-items:center"><div style="width:{int(tam * (.62 if tam > 32 else .9))}px">{simb.replace("class=\"s\"", "class=\"s\" style=\"fill:#44D62D\"" if tam == 32 else "class=\"s\"")}</div><style>.s{{fill:#F7F7F7}}</style></body></html>')
            pg.screenshot(path=R + 'img/marca/' + nome, omit_background=tam == 32)
        b.close()
    print('imagens de compartilhamento e ícones ok')


if __name__ == '__main__':
    imagens(); aplica(); sitemap()
