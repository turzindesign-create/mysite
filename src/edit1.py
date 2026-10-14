p='/home/claude/site_v4/src/index.src.html'; s=open(p).read()
def R(a,b,cnt=1):
    global s
    assert s.count(a)>=1, 'NAO ACHEI: '+a[:90]
    s=s.replace(a,b) if cnt==0 else s.replace(a,b,cnt)

# ---------------- cabeçalho do arquivo / fontes ----------------
R("""     TURZIN DESIGN · PORTFÓLIO""","""     turzin. · PORTFÓLIO (engenharia de design)""")
R("<title>Turzin Design</title>","<title>turzin. · engenharia de design</title>\n<link rel=\"icon\" href=\"img/marca/simbolo.svg\" type=\"image/svg+xml\">")
R('content="Turzin Design: identidade visual, sites e movimento para negócios. Uberaba, MG."','content="turzin. é engenharia de design: identidade visual, sites e movimento. Tecnologia, design e planejamento no mesmo trampo. Uberaba, MG."')
R("""<!-- [GUIA: fontes-google] Fontes carregadas do Google Fonts.
     Para trocar uma fonte: escolha em fonts.google.com, troque o nome aqui
     E troque também nas variáveis --fonte-* do PAINEL DE CONTROLE (CSS).
     Bricolage Grotesque = títulos | Figtree = textos | JetBrains Mono = etiquetas pequenas
     Bodoni Moda, Jost e Fraunces = só usadas no Playground ("Teste a sua marca") -->""",
"""<!-- [GUIA: fontes-google] Fonte da marca: Bricolage Grotesque (variável: peso 200–800, largura 75–100, tamanho óptico 12–96).
     É a única fonte do site. Bodoni Moda, Jost e Fraunces aparecem SÓ dentro do Playground,
     porque ali são as marcas de mentira que o visitante testa (não é a tipografia da turzin.). -->""")
R("family=Bricolage+Grotesque:opsz,wdth,wght@12..96,75..100,200..800&family=Figtree:wght@400;500;600&family=JetBrains+Mono:wght@400;500&family=","family=Bricolage+Grotesque:opsz,wdth,wght@12..96,75..100,200..800&family=")

# ---------------- cores e fontes ----------------
R("""  --ground: #0c0c0b;                  /* fundo da página */
  --ink: #f2f0e9;                     /* cor principal do texto */
  --mute: rgba(242,240,233,.6);       /* texto secundário, mais apagado */
  --line: rgba(242,240,233,.16);      /* linhas e bordas finas */
  --green: #1fdc2a;                   /* verde Turzin: botões, destaques, barra de progresso */
  --green-ink: #062b08;               /* texto escuro usado em cima do verde */
  --panel: #161614;                   /* fundo dos cartões do Playground */""",
"""  --ground: #212121;                  /* cinza escuro da marca: fundo da página */
  --ink: #F7F7F7;                     /* off-white: cor principal do texto */
  --mute: rgba(247,247,247,.62);      /* texto secundário, mais apagado */
  --line: rgba(247,247,247,.16);      /* linhas e bordas finas */
  --green: #44D62D;                   /* verde turzin.: destaques, ponto final, barra de progresso */
  --green-ink: #212121;               /* texto escuro usado em cima do verde */
  --panel: rgba(247,247,247,.05);     /* fundo dos cartões do Playground */""")
R("""  --display: 'Bricolage Grotesque', 'Arial Narrow', system-ui, sans-serif;  /* títulos e logo */
  --body: 'Figtree', system-ui, -apple-system, sans-serif;                  /* textos corridos */
  --mono: 'JetBrains Mono', ui-monospace, Menlo, monospace;                 /* etiquetas pequenas em maiúsculas */""",
"""  /* uma família só, a Bricolage. Os três nomes existem só para organizar os usos */
  --display: 'Bricolage Grotesque', 'Arial Narrow', system-ui, sans-serif;  /* títulos (sempre em CAIXA ALTA) */
  --body: 'Bricolage Grotesque', system-ui, -apple-system, sans-serif;      /* textos corridos */
  --mono: 'Bricolage Grotesque', system-ui, sans-serif;                     /* etiquetas pequenas em CAIXA ALTA */
  /* [GUIA: largura-titulos] largura da Bricolage nos títulos (75 = bem condensada, 100 = normal) */
  --largura: 78;""")
R("""  --ground: #efece3;
  --ink: #121210;
  --mute: rgba(18,18,16,.62);
  --line: rgba(18,18,16,.16);
  --panel: #e4e0d4;
  --green: #12a51b;""","""  --ground: #F7F7F7;
  --ink: #212121;
  --mute: rgba(33,33,33,.66);
  --line: rgba(33,33,33,.16);
  --panel: rgba(33,33,33,.05);
  --green: #44D62D;""")
# base: tipografia em caixa alta
R("body { margin: 0; background: var(--ground); color: var(--ink); font: 16px/1.55 var(--body); transition: background-color .6s, color .6s; }",
  "body { margin: 0; background: var(--ground); color: var(--ink); font: 17px/1.5 var(--body); font-optical-sizing: auto; transition: background-color .6s, color .6s; }")
R(".mono { font-family: var(--mono); font-size: 12px; letter-spacing: .08em; text-transform: uppercase; }",
  ".mono { font-family: var(--mono); font-weight: 500; font-size: 12.5px; letter-spacing: .08em; text-transform: uppercase; }\n.nocaps { text-transform: none; }  /* para escrever turzin. sempre minúsculo dentro de etiquetas */")
R("h1, h2, h3 { margin: 0; font-family: var(--display); letter-spacing: -.035em; text-wrap: balance; }",
  """/* [GUIA: caixa-alta] todos os títulos em CAIXA ALTA, condensados (largura --largura) */
h1, h2, h3 { margin: 0; font-family: var(--display); text-transform: uppercase; letter-spacing: -.02em; text-wrap: balance; font-variation-settings: "wdth" var(--largura); }
/* ponto final quadrado (o mesmo do logo) no fim dos títulos */
.pt { display: inline-block; width: .16em; height: .16em; margin-left: .05em; background: var(--green); }""")

# ---------------- logo ----------------
R("""/* [GUIA: logo-css] visual da logo "turzin." (fonte, tamanho, cor do ponto) */
.logo { font-family: var(--display); font-weight: 800; font-size: 26px; letter-spacing: -.05em; line-height: 1; text-decoration: none; }
.logo span { color: var(--green); }   /* cor do ponto final da logo */""",
"""/* [GUIA: logo-css] logo da turzin. (arquivo img/marca/logotipo.svg colado no HTML)
   .t = letras · .d = ponto quadrado · .s = símbolo. width = tamanho */
.logo { display: block; width: 108px; line-height: 0; }
.marca .t, .marca .s { fill: var(--ink); transition: fill .3s; }
.marca .d { fill: var(--green); transition: fill .3s; }
html.no-verde .top .marca .d { fill: var(--green-ink); }   /* em cima do bloco verde do contato */""")
# botões: caixa alta + preenchimento em bloco
R(""".btn { display: inline-flex; align-items: center; gap: 10px; border-radius: 99px; padding: 13px 22px; font-weight: 600; font-size: 15px; text-decoration: none; border: 1px solid var(--line); background: transparent; cursor: pointer; transition: background .25s, color .25s, border-color .25s; will-change: transform; }
.btn.fill { background: var(--green); color: var(--green-ink); border-color: var(--green); }
.btn.fill:hover { background: var(--ink); color: var(--ground); border-color: var(--ink); }
.btn:not(.fill):hover { border-color: var(--ink); }""",
"""/* [GUIA: botoes] botões em caixa alta. No hover, um bloco verde preenche da esquerda pra direita */
.btn { position: relative; isolation: isolate; overflow: hidden; display: inline-flex; align-items: center; gap: 10px; border-radius: 0; padding: 13px 22px; font-weight: 700; font-size: 14px; letter-spacing: .06em; text-transform: uppercase; text-decoration: none; border: 1.5px solid var(--line); background: transparent; cursor: pointer; transition: color .2s steps(2), border-color .2s steps(2); will-change: transform; }
.btn::before { content: ""; position: absolute; inset: 0; z-index: -1; background: var(--green); transform: scaleX(0); transform-origin: left; transition: transform .22s cubic-bezier(.2,.9,.1,1); }
.btn:hover::before, .btn:focus-visible::before { transform: none; }
.btn:hover, .btn:focus-visible { color: var(--green-ink); border-color: var(--green); }
.btn.fill { background: var(--green); color: var(--green-ink); border-color: var(--green); }
.btn.fill::before { background: var(--ink); }
.btn.fill:hover { color: var(--ground); border-color: var(--ink); }""")
R(".top nav a.l { text-decoration: none; opacity: .75; }",".top nav a.l { text-decoration: none; opacity: .8; }")
R("@media (max-width: 760px) { .top nav a.l { display: none; } }  /* no celular só aparece o botão Orçamento */","@media (max-width: 760px) { .top nav a.l { display: none; } }  /* no celular só aparece o botão Contato */")

# ---------------- hero ----------------
R(".hero h1 { font-weight: 800; font-size: var(--titulo-hero); line-height: .9; letter-spacing: -.04em; max-width: 13ch; }",
  ".hero h1 { font-weight: 800; font-size: var(--titulo-hero); line-height: .92; letter-spacing: -.02em; max-width: 12ch; }")
R("""/* cada letra sobe ao abrir a página (animação "rise") */
.hero h1 .ch { display: inline-block; font-variation-settings: "wght" 800, "wdth" 100; animation: rise var(--t-letras) var(--curva) both; }
@keyframes rise { from { transform: translateY(110%) rotate(6deg); } }""",
"""/* título DIGITADO: cada letra aparece e um cursor verde anda junto. No fim o cursor fica piscando */
.hero h1 .ch { display: inline-block; font-variation-settings: "wght" 800, "wdth" var(--largura); }
html.anima .hero h1 .ch.tp { opacity: 0; }
.cur { display: inline-block; width: .16em; height: .16em; margin-left: .05em; background: var(--green); }
.cur.pisca { animation: pisca 1s steps(1) infinite; }
@keyframes pisca { 50% { opacity: 0; } }""")
R(".rot { display: inline-grid; vertical-align: bottom; height: 1.4em; overflow: hidden; color: var(--ink); font-weight: 600; }",
  ".rot { display: inline-grid; vertical-align: bottom; height: 1.4em; overflow: hidden; color: var(--ink); font-weight: 700; text-transform: uppercase; letter-spacing: .02em; }")
# seções
R(".sec h2 { font-weight: 800; font-size: var(--titulo-secao); line-height: .95; }",".sec h2 { font-weight: 800; font-size: var(--titulo-secao); line-height: .95; letter-spacing: -.02em; }")
R(""".ch-title { grid-column: 1 / -1; font-size: var(--titulo-projeto); line-height: .86; letter-spacing: -.045em; font-variation-settings: "wght" 800, "wdth" 100; white-space: nowrap; }""",
  """.ch-title { grid-column: 1 / -1; font-size: var(--titulo-projeto); line-height: .9; letter-spacing: -.02em; font-variation-settings: "wght" 800, "wdth" var(--largura); white-space: nowrap; }""")
R(".chips span { border: 1px solid rgba(255,255,255,.4); border-radius: 99px; padding: 4px 11px; font-size: 12.5px; }",
  ".chips span { border: 1px solid rgba(255,255,255,.4); padding: 4px 10px; font-size: 12px; font-weight: 500; letter-spacing: .06em; text-transform: uppercase; }")
R(".ch-info .btn:hover { background: #fff; color: #111; }",".ch-info .btn::before { background: #fff; } .ch-info .btn:hover { color: #111; border-color: #fff; }")
R(".htrack figure { margin: 0; flex: none; height: 100%; aspect-ratio: 4/5; border-radius: 8px;",".htrack figure { margin: 0; flex: none; height: 100%; aspect-ratio: 4/5; border-radius: 0;")
R(".htrack figcaption { position: absolute; left: 10px; bottom: 10px; background: rgba(12,12,11,.78); color: #fff; padding: 5px 9px; border-radius: 3px; font: 11px var(--mono);",
  ".htrack figcaption { position: absolute; left: 10px; bottom: 10px; background: rgba(33,33,33,.85); color: #fff; padding: 5px 9px; font: 500 11px var(--mono);")
R(".layer { position: absolute; border-radius: 6px;",".layer { position: absolute; border-radius: 0;")
R(".tilt .rev b { display: block; font-family: var(--display); font-size: 20px; }",".tilt .rev b { display: block; font-family: var(--display); font-weight: 800; font-size: 22px; text-transform: uppercase; font-variation-settings: \"wdth\" var(--largura); }")
R(".panel { background: var(--panel); border-radius: 10px;",".panel { background: var(--panel); border-radius: 0;")
R(".panel h3 { font-size: clamp(24px, 2.6vw, 34px); font-weight: 600; }",".panel h3 { font-size: clamp(26px, 2.8vw, 38px); font-weight: 800; }")
R(".seg-btns button { border: 1px solid var(--line); background: transparent; border-radius: 99px; padding: 8px 14px; cursor: pointer; font-size: 14px; }",
  ".seg-btns button { border: 1.5px solid var(--line); background: transparent; border-radius: 0; padding: 8px 14px; cursor: pointer; font-size: 13px; font-weight: 600; letter-spacing: .05em; text-transform: uppercase; }")
R(".svc h3 { font-size: clamp(24px, 2.6vw, 34px); font-weight: 600; }",".svc h3 { font-size: clamp(28px, 3vw, 40px); font-weight: 800; }")
R('.svc li::before { content: "+ "; color: var(--green); }','.svc li::before { content: ""; display: inline-block; width: 7px; height: 7px; margin: 0 10px 2px 0; background: var(--green); }')
R(".end h2 { font-size: clamp(44px, 9vw, 150px); max-width: 12ch; }",".end h2 { font-size: clamp(44px, 9vw, 150px); max-width: 13ch; }\n.end .pt, .end .cur { background: var(--green-ink); }")
R(".end .kick { color: rgba(6,43,8,.65); }",".end .kick { color: rgba(33,33,33,.7); }\n.end .lede { color: rgba(33,33,33,.8); }")
R(".end .btn.fill:hover { background: #fff; color: var(--green-ink); border-color: #fff; }",".end .btn.fill::before { background: var(--ink); } .end .btn.fill:hover { color: var(--green-ink); border-color: var(--ink); }")
R(".contacts strong { font-family: var(--display); font-weight: 500;",".contacts strong { font-family: var(--display); font-weight: 700;")
R(".copy { justify-self: start; border: 1px solid var(--green-ink); background: transparent; color: var(--green-ink); border-radius: 99px;",".copy { justify-self: start; border: 1.5px solid var(--green-ink); background: transparent; color: var(--green-ink); border-radius: 0; font-weight: 600; text-transform: uppercase; letter-spacing: .05em;")
R("footer.ft { display: flex; justify-content: space-between; flex-wrap: wrap; gap: 10px; padding: 24px var(--g) calc(24px + env(safe-area-inset-bottom, 0px)); color: var(--mute); }",
  "footer.ft { display: flex; justify-content: space-between; align-items: end; flex-wrap: wrap; gap: 16px; padding: 32px var(--g) calc(28px + env(safe-area-inset-bottom, 0px)); color: var(--mute); }\nfooter.ft .marca { width: 132px; }")

# ---------------- HTML: logo, menu ----------------
R("""  <!-- [GUIA: logo-html] Texto da logo. O <span> é o ponto verde. -->
  <a class="logo" href="#inicio" aria-label="Turzin Design, início">turzin<span>.</span></a>""",
"""  <!-- [GUIA: logo-html] logo (arquivo img/marca/logotipo.svg). Para trocar, cole o novo SVG aqui -->
  <a class="logo" href="#inicio" aria-label="turzin., início">{{SVG:logotipo:marca}}</a>""")
R("""    <!-- botão Orçamento: o link do WhatsApp é colocado pelo JS (CONFIG.whatsapp) -->
    <a class="btn fill sm mag js-whats" href="#contato" target="_blank" rel="noopener">Orçamento</a>""",
"""    <a class="btn fill sm mag" href="#contato">Contato</a>""")
open(p,'w').write(s); print('ok edit1')
