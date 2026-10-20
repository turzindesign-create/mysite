"""Gera os mockups da landing page (img/lp/mockups/*.webp) desenhados em HTML/CSS.
Rode: python src/mockups_lp.py"""
import os, re, base64
from PIL import Image
import numpy as np
from playwright.sync_api import sync_playwright
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/'
L = '/home/claude/logos/'
O = R + 'img/lp/mockups/'; os.makedirs(O, exist_ok=True)

def simb(nome, cor, extra=''):
    s = open(L + nome + '.svg').read()
    s = re.sub(r'<text[^>]*class="rot"[^>]*>.*?</text>', '', s, flags=re.S)
    s = re.sub(r'<(line|ellipse|circle)[^>]*class="guia"[^>]*/?>(\s*</\1>)?', '', s)
    s = re.sub(r'fill="#(?!000"|fff")[0-9a-fA-F]{3,6}"', f'fill="{cor}"', s)
    s = re.sub(r'\saria-label="[^"]*"', '', s).replace('class="esboco"', f'style="width:100%;height:auto;display:block;{extra}"', 1)
    return s.replace('id="isa-m"', f'id="m{abs(hash(cor+extra))}"').replace('url(#isa-m)', f'url(#m{abs(hash(cor+extra))})')

def rei_simb(cor):
    s = open('/home/claude/reigotta-marca/marca/svg/simbolo-rosa.svg').read()
    return s.replace('#FF3EB5', cor).replace('<svg ', '<svg style="width:100%;height:auto;display:block" ', 1)

def logo_png(nome, cor):
    """logo da marca (PNG transparente) pintado de uma cor só, em data URI"""
    im = Image.open(R + f'img/lp/logos/{nome}.png').convert('RGBA'); a = np.asarray(im)
    c = tuple(int(cor[i:i+2], 16) for i in (1, 3, 5))
    out = np.zeros_like(a); out[..., 0], out[..., 1], out[..., 2] = c; out[..., 3] = a[..., 3]
    p = '/tmp/_logo.png'; Image.fromarray(out).save(p)
    return 'data:image/png;base64,' + base64.b64encode(open(p, 'rb').read()).decode()

def logo_orig(nome):
    return 'data:image/png;base64,' + base64.b64encode(open(R + f'img/lp/logos/{nome}.png', 'rb').read()).decode()

SOMBRA = 'box-shadow:0 2px 3px rgba(0,0,0,.18),0 18px 30px rgba(0,0,0,.18),0 50px 80px rgba(0,0,0,.14)'
BASE = '*{margin:0;box-sizing:border-box}body{width:1200px;height:1500px;overflow:hidden;position:relative}.o{position:absolute}'

C = {}
# 1 · ISABELLA: mesa da psicóloga (agenda, cartão de retorno, café, caneta)
C['isabella'] = f'''<body style="background:#E8DDD0">
<div class="o" style="left:110px;top:250px;width:600px;height:820px;transform:rotate(-7deg);background:#961B2E;border-radius:10px 26px 26px 10px;{SOMBRA}">
  <div class="o" style="left:0;top:0;bottom:0;width:46px;background:#7C1424;border-radius:10px 0 0 10px"></div>
  <div class="o" style="right:70px;top:0;bottom:0;width:22px;background:#6E1220"></div>
  <div class="o" style="left:170px;top:250px;width:260px">{simb('isabella', '#D8B072')}</div>
</div>
<div class="o" style="left:600px;top:860px;width:520px;height:300px;transform:rotate(7deg);background:#FBF7F2;border-radius:6px;{SOMBRA};display:grid;place-items:center">
  <img src="{logo_png('isabella', '#961B2E')}" style="width:330px">
</div>
<div class="o" style="left:760px;top:190px;width:330px;height:330px;border-radius:50%;background:#F6F1EA;{SOMBRA}">
  <div class="o" style="left:300px;top:130px;width:110px;height:70px;border-radius:0 40px 40px 0;border:22px solid #F6F1EA;border-left:0;box-shadow:6px 8px 14px rgba(0,0,0,.12)"></div>
  <div class="o" style="left:38px;top:38px;width:254px;height:254px;border-radius:50%;background:#4A2C1E;box-shadow:inset 0 6px 14px rgba(0,0,0,.35)"></div>
  <div class="o" style="left:110px;top:105px;width:110px;height:110px;border-radius:50%;background:#C79A6B;opacity:.55"></div>
</div>
<div class="o" style="left:560px;top:1290px;width:560px;height:24px;transform:rotate(-9deg);background:#B8924F;border-radius:12px;{SOMBRA}">
  <div class="o" style="right:0;top:0;width:90px;height:24px;background:#2a1a12;border-radius:0 12px 12px 0"></div></div>
</body>'''

# 2 · MARGARETT: caixa de hambúrguer, batata, molho e selo
fritas = ''.join(f'<div class="o" style="left:{40+i*30}px;top:{-90+(i*37)%70}px;width:24px;height:170px;background:#F1C04A;border-radius:4px;transform:rotate({(i*7)%15-7}deg);box-shadow:inset -4px 0 0 #D9A233"></div>' for i in range(8))
C['margarett'] = f'''<body style="background:#1C1510">
<div class="o" style="left:140px;top:260px;width:640px;height:640px;transform:rotate(-6deg);background:#C59A6A;border-radius:14px;{SOMBRA}">
  <div class="o" style="inset:26px;border:3px solid rgba(80,50,20,.25);border-radius:8px"></div>
  <div class="o" style="left:0;right:0;top:470px;height:3px;background:rgba(80,50,20,.3)"></div>
  <div class="o" style="left:110px;top:170px;width:420px"><img src="{logo_png('margarett', '#1A130D')}" style="width:100%"></div>
</div>
<div class="o" style="left:770px;top:860px;width:300px;height:360px;transform:rotate(9deg)">
  {fritas}
  <div class="o" style="left:0;top:40px;width:300px;height:320px;background:#F2E8D8;clip-path:polygon(0 0,100% 0,88% 100%,12% 100%);border-radius:6px"></div>
  <div class="o" style="left:95px;top:150px;width:110px">{simb('margarett', '#1A130D')}</div>
</div>
<div class="o" style="left:840px;top:250px;width:200px;height:200px;border-radius:50%;background:#F2E8D8;{SOMBRA}">
  <div class="o" style="inset:26px;border-radius:50%;background:#B0281C;box-shadow:inset 0 6px 12px rgba(0,0,0,.35)"></div>
  <div class="o" style="left:62px;top:56px;width:40px;height:22px;border-radius:50%;background:rgba(255,255,255,.35)"></div></div>
<div class="o" style="left:150px;top:1040px;width:230px;height:230px;border-radius:50%;background:#F2E8D8;transform:rotate(-12deg);{SOMBRA};display:grid;place-items:center">
  <div style="width:130px">{simb('margarett', '#1A130D')}</div></div>
</body>'''

# 3 · AÇAÍ YO: tigela vista de cima, colher e guardanapo
import random; random.seed(7)
granola = ''.join(f'<div class="o" style="left:{random.randint(170,480)}px;top:{random.randint(150,470)}px;width:{random.randint(16,30)}px;height:{random.randint(12,22)}px;background:{random.choice(["#B9864C","#A9773F","#CFA066"])};border-radius:40%;transform:rotate({random.randint(0,90)}deg)"></div>' for _ in range(70))
banana = ''.join(f'<div class="o" style="left:{x}px;top:{y}px;width:96px;height:96px;border-radius:50%;background:#F6E7A6;box-shadow:inset 0 0 0 6px #EBD27E"><div class="o" style="left:38px;top:38px;width:20px;height:20px;border-radius:50%;background:#D9BD6A"></div></div>' for x, y in [(90,250),(420,110),(470,430),(170,470)])
morango = ''.join(f'<div class="o" style="left:{x}px;top:{y}px;width:110px;height:92px;background:#E0324A;border-radius:50% 50% 46% 46%/60% 60% 40% 40%;transform:rotate({r}deg);box-shadow:inset -8px -8px 0 rgba(0,0,0,.12)"><div class="o" style="left:20px;top:18px;width:70px;height:6px;background:repeating-linear-gradient(90deg,#FBD3D9 0 6px,transparent 6px 14px);border-radius:4px"></div></div>' for x, y, r in [(250,70,-20),(330,520,15),(70,370,-5)])
leite = '<svg class="o" style="left:60px;top:60px" width="520" height="520" viewBox="0 0 520 520"><path d="M60 300 C120 200 180 380 240 260 S360 140 420 260 S470 380 500 300" fill="none" stroke="#FFF8F0" stroke-width="18" stroke-linecap="round" opacity=".92"/></svg>'
C['acai-yo'] = f'''<body style="background:#EFE5FB">
<div class="o" style="left:250px;top:240px;width:700px;height:700px;border-radius:50%;background:#FFFFFF;{SOMBRA}">
  <div class="o" style="left:30px;top:30px;width:640px;height:640px;border-radius:50%;background:#4A1A5C;box-shadow:inset 0 10px 24px rgba(0,0,0,.45);overflow:hidden">
    {granola}{banana}{morango}{leite}
  </div>
</div>
<div class="o" style="left:780px;top:860px;width:90px;height:520px;transform:rotate(-32deg);transform-origin:top center">
  <div class="o" style="left:0;top:0;width:90px;height:130px;border-radius:50%;background:#8B3AC1;box-shadow:inset 0 -10px 0 rgba(0,0,0,.15),0 14px 24px rgba(0,0,0,.2)"></div>
  <div class="o" style="left:32px;top:110px;width:26px;height:410px;border-radius:13px;background:#8B3AC1;box-shadow:0 14px 24px rgba(0,0,0,.2)"></div></div>
<div class="o" style="left:110px;top:1000px;width:400px;height:400px;transform:rotate(-9deg);background:#8B3AC1;border-radius:6px;{SOMBRA};display:grid;place-items:center">
  <img src="{logo_orig('acai-yo')}" style="width:240px"></div>
</body>'''

# 4 · REIGOTTA: squeeze, tapete de yoga enrolado e etiqueta
C['reigotta'] = f'''<body style="background:#EFEFEF">
<div class="o" style="left:0;right:0;top:1180px;bottom:0;background:#E4E4E4"></div>
<div class="o" style="left:250px;top:330px;width:290px;height:860px">
  <div class="o" style="left:95px;top:0;width:100px;height:70px;background:#262626;border-radius:18px 18px 4px 4px"></div>
  <div class="o" style="left:60px;top:60px;width:170px;height:90px;background:#262626;border-radius:10px"></div>
  <div class="o" style="left:0;top:140px;width:290px;height:720px;background:#FF3EB5;border-radius:70px 70px 40px 40px;{SOMBRA};overflow:hidden">
    <div class="o" style="left:30px;top:40px;width:40px;height:620px;background:rgba(255,255,255,.22);border-radius:20px"></div>
    <div class="o" style="right:0;top:0;width:60px;height:100%;background:rgba(0,0,0,.08)"></div>
    <div class="o" style="left:145px;top:360px;width:520px;transform:translate(-50%,-50%) rotate(-90deg)"><img src="{logo_png('reigotta', '#FFFFFF')}" style="width:100%"></div>
  </div>
</div>
<div class="o" style="left:500px;top:1030px;width:600px;height:240px;background:#262626;border-radius:120px;{SOMBRA}">
  <div class="o" style="right:0;top:0;width:240px;height:240px;border-radius:50%;background:#333;box-shadow:inset 0 0 0 26px #262626,inset 0 0 0 30px #FF3EB5,inset 0 0 0 56px #262626,inset 0 0 0 60px #FF3EB5,inset 0 0 0 86px #262626"></div>
  <div class="o" style="left:150px;top:-6px;width:46px;height:252px;background:#FF3EB5;border-radius:8px"></div>
</div>
<div class="o" style="left:735px;top:180px;width:2px;height:240px;background:#262626;transform:rotate(-4deg)"></div>
<div class="o" style="left:640px;top:400px;width:250px;height:400px;background:#FFFFFF;clip-path:polygon(18% 0,82% 0,100% 12%,100% 100%,0 100%,0 12%);transform:rotate(-4deg);filter:drop-shadow(0 20px 30px rgba(0,0,0,.2))">
  <div class="o" style="left:113px;top:22px;width:24px;height:24px;border-radius:50%;background:#EFEFEF"></div>
  <div class="o" style="left:45px;top:120px;width:160px">{rei_simb('#FF3EB5')}</div>
  <div class="o" style="left:0;right:0;bottom:0;height:110px;background:#FF3EB5"></div>
</div>
</body>'''

# 5 · KAMISAMA: caixa de delivery com sushi, hashi com luva e shoyu
def nigiri(x, y, r):
    return f'''<div class="o" style="left:{x}px;top:{y}px;width:150px;height:84px;transform:rotate({r}deg)">
  <div class="o" style="left:4px;top:10px;width:142px;height:72px;background:#F7F3EA;border-radius:36px;box-shadow:0 6px 10px rgba(0,0,0,.35)"></div>
  <div class="o" style="left:0;top:0;width:150px;height:70px;background:#FF7A45;border-radius:34px 40px 30px 36px;background-image:repeating-linear-gradient(115deg,transparent 0 16px,rgba(255,235,215,.75) 16px 22px)"></div></div>'''
pecas = ''.join(nigiri(40 + (i % 4) * 160, 50 + (i // 4) * 120, (i * 13) % 9 - 4) for i in range(8))
C['kamisama'] = f'''<body style="background:#2A1517">
<div class="o" style="left:110px;top:400px;width:740px;height:520px;transform:rotate(-5deg);background:#111;border-radius:26px;{SOMBRA}">
  <div class="o" style="inset:18px;border-radius:16px;background:#1C1C1C;box-shadow:inset 0 0 0 2px #2a2a2a"></div>
  <div class="o" style="left:18px;top:18px;width:704px;height:300px">{pecas}</div>
  <div class="o" style="left:60px;top:340px;width:130px;height:120px;background:#9CC25B;border-radius:44% 56% 50% 50%"></div>
  <div class="o" style="left:220px;top:350px;width:180px;height:110px;background:#F4B7A6;border-radius:40%;background-image:repeating-linear-gradient(30deg,transparent 0 14px,rgba(255,255,255,.35) 14px 18px)"></div>
  <div class="o" style="left:500px;top:330px;width:160px;height:160px;border-radius:50%;background:#93282C;display:grid;place-items:center"><div style="width:62px">{simb('kamisama', '#FFFFFF')}</div></div>
</div>
<div class="o" style="left:930px;top:180px;width:120px;height:900px;transform:rotate(10deg)">
  <div class="o" style="left:30px;top:0;width:18px;height:900px;background:#D7B886;border-radius:8px"></div>
  <div class="o" style="left:62px;top:0;width:18px;height:900px;background:#CFAF7C;border-radius:8px"></div>
  <div class="o" style="left:0;top:240px;width:120px;height:620px;background:#FF5C35;border-radius:4px;{SOMBRA}">
    <div class="o" style="left:22px;top:120px;width:76px">{simb('kamisama', '#FFFFFF')}</div></div>
</div>
<div class="o" style="left:150px;top:1060px;width:280px;height:280px;border-radius:50%;background:#F4F0E8;{SOMBRA}">
  <div class="o" style="inset:40px;border-radius:50%;background:#2B120A;box-shadow:inset 0 8px 16px rgba(0,0,0,.6)"></div>
  <div class="o" style="left:100px;top:90px;width:50px;height:26px;border-radius:50%;background:rgba(255,255,255,.18)"></div></div>
<div class="o" style="left:560px;top:1080px;width:300px;height:220px;transform:rotate(6deg);background:#FBF7F0;border-radius:8px;{SOMBRA};display:grid;place-items:center">
  <img src="{logo_png('kamisama', '#93282C')}" style="width:170px"></div>
</body>'''

with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1200, 'height': 1500})
    for k, body in C.items():
        t = '/tmp/_mock.html'; open(t, 'w').write(f'<html><head><meta charset="utf-8"><style>{BASE}</style></head>{body}</html>')
        pg.goto('file://' + t); pg.wait_for_timeout(300)
        pg.screenshot(path='/tmp/_mock.png')
        Image.open('/tmp/_mock.png').convert('RGB').save(O + k + '.webp', 'WEBP', quality=86)
        print('mockup ok', k)
    b.close()
