p='/home/claude/site_v4/src/index.src.html'; s=open(p).read()
def R(a,b):
    global s
    assert a in s, 'NAO ACHEI: '+a[:100]
    s=s.replace(a,b,1)

# ================= CSS novo das animações de tecnologia =================
R("""/* blocos que sobem quando você rola até eles */""",
"""/* ================================================================
   ANIMAÇÕES DE TECNOLOGIA (novas)
   ================================================================ */
/* [GUIA: grade-hero] grade de engenharia no fundo da primeira tela (segue o mouse) e linha de varredura */
.hero { position: relative; isolation: isolate; }
.hero::before { content: ""; position: absolute; inset: -64px; z-index: -1; pointer-events: none; opacity: .55;
  background-image: linear-gradient(var(--line) 1px, transparent 1px), linear-gradient(90deg, var(--line) 1px, transparent 1px);
  background-size: 64px 64px; -webkit-mask-image: radial-gradient(ellipse 70% 60% at 70% 45%, #000, transparent 75%); mask-image: radial-gradient(ellipse 70% 60% at 70% 45%, #000, transparent 75%);
  transform: translate(var(--gx, 0px), var(--gy, 0px)); }
.hero::after { content: ""; position: absolute; left: 0; right: 0; top: 0; height: 1px; z-index: -1; pointer-events: none; background: var(--green); opacity: 0; }
html.anima .hero::after { animation: varre 7s 2.2s cubic-bezier(.6,0,.4,1) infinite; }
@keyframes varre { 0% { transform: translateY(0); opacity: 0; } 8% { opacity: .5; } 60% { opacity: .35; } 100% { transform: translateY(100vh); opacity: 0; } }
/* HUD: coordenadas do mouse (PC) ou porcentagem de rolagem (celular) */
.hud { font-variant-numeric: tabular-nums; color: var(--green); }
/* símbolo da marca que se monta bloco a bloco (pixels). --i = ordem do bloco, do maior pro menor */
.px rect { transform-box: fill-box; transform-origin: center; }
html.anima .px rect { opacity: 0; transform: scale(.4); }
html.anima .px.on rect { animation: pixel .26s steps(3, end) forwards; animation-delay: calc(var(--i) * 90ms); }
@keyframes pixel { to { opacity: 1; transform: none; } }
.hero-sym { width: 58px; margin-bottom: 22px; }
.kick-row { display: flex; align-items: center; justify-content: space-between; gap: 16px; }
.kick-row .px { width: 40px; flex: none; }
.end .marca .s { fill: var(--green-ink); }
.end-sym { width: clamp(70px, 9vw, 120px); margin-bottom: 26px; }
/* ponto final que CAI no fim dos títulos quando eles entram (batida no fim do verso) */
html.anima .split .pt { opacity: 0; transform: translateY(-1.2em); }
html.anima .split.in .pt { animation: batida .34s cubic-bezier(.55,0,.9,.4) .35s forwards; }
@keyframes batida { 0% { opacity: 1; transform: translateY(-1.2em); } 70% { opacity: 1; transform: none; } 82% { transform: translateY(.03em) scale(1.3, .65); } 100% { opacity: 1; transform: none; } }
/* revelação em pixels das imagens (canvas criado pelo JS por cima da imagem) */
canvas.pxr { position: absolute; inset: 0; width: 100%; height: 100%; z-index: 2; pointer-events: none; image-rendering: pixelated; }
.tilt { isolation: isolate; }
/* rastro de pixels do cursor (PC) */
.trail { position: fixed; left: 0; top: 0; width: 7px; height: 7px; margin: -3px 0 0 -3px; background: var(--green); pointer-events: none; z-index: 59; opacity: 0; }

/* blocos que sobem quando você rola até eles */""")
# cursor quadrado
R(".cursor { position: fixed; z-index: 60; left: 0; top: 0; width: 14px; height: 14px; margin: -7px 0 0 -7px; border-radius: 50%;",
  ".cursor { position: fixed; z-index: 60; left: 0; top: 0; width: 14px; height: 14px; margin: -7px 0 0 -7px; border-radius: 0;")
R(".cursor span { font: 600 11px var(--mono);",".cursor span { font: 700 11px var(--mono);")

# ================= HTML =================
R("""  <div class="eyebrow mono"><span>Turzin Design</span><span>Identidade visual · Sites · Movimento</span><span>Uberaba, MG</span></div>
  <!-- título principal: cada <span class="ln"> é uma linha. class="ln alt" = linha verde -->
  <h1 id="ht"><span class="ln">Seu negócio é bom.</span><span class="ln alt">Faça ele parecer</span><span class="ln alt">bom também.</span></h1>
  <div class="row">
    <!-- as palavras dentro de id="rot" ficam trocando sozinhas. Pode adicionar mais <span> -->
    <p class="say">Turzin junta <span class="rot" id="rot"><span class="on">design</span><span>tecnologia</span><span>experiência</span></span><br>para criar marcas que as pessoas lembram.</p>""",
"""  <!-- símbolo da marca: se monta bloco a bloco ao abrir a página -->
  {{SVG:simbolo:marca px hero-sym}}
  <div class="eyebrow mono"><span class="nocaps">turzin.</span><span>Engenharia de design</span><span>Uberaba, MG</span><span class="hud" id="hud" aria-hidden="true">X 0000 · Y 0000</span></div>
  <!-- título principal (é DIGITADO ao abrir). Cada <span class="ln"> é uma linha.
       data-pt = linha termina com o ponto verde · data-cur = linha termina com o cursor piscando
       Se mudar o texto, mude também o aria-label (é o que leitores de tela leem) -->
  <h1 id="ht" aria-label="Do rascunho ao deploy. Sem template."><span class="ln">Do rascunho</span><span class="ln" data-pt>ao deploy</span><span class="ln" data-cur>Sem template</span></h1>
  <div class="row">
    <!-- as palavras dentro de id="rot" ficam trocando sozinhas. Pode adicionar mais <span> -->
    <p class="say"><span class="nocaps">turzin.</span> é <span class="rot" id="rot"><span class="on">tecnologia</span><span>design</span><span>engenharia</span></span><br>Com atitude, do tamanho da fonte até o outdoor.</p>""")
R("""      <span class="seg mono">01 · Psicóloga · Sorocaba, SP</span>
      <p>Duas letras B, de Isabella, se encontram e viram uma borboleta, símbolo da psicologia e da transformação. Vinho, pêssego e amarelo passam acolhimento e fogem do azul frio da saúde.</p>""",
"""      <span class="seg mono scr">01 · Psicóloga · Sorocaba, SP</span>
      <p>O segmento inteiro fala frio: azul, cérebro, folha. A Isabella atende relacionamento, então a marca tinha que acolher. Duas letras B espelhadas viram uma borboleta. Vinho, pêssego e amarelo no lugar do azul de consultório.</p>""")
R("""      <span class="seg mono">02 · Hambúrguer artesanal</span>
      <p>A hamburgueria como experiência, não como lanchonete. Serifa elegante, preto e marrom café, e um hambúrguer desenhado só com linhas. Na sacola, o recado vai junto: “Aproveite cada momento”.</p>""",
"""      <span class="seg mono scr">02 · Hambúrguer artesanal</span>
      <p>Hamburgueria artesanal não é lanchonete, e a marca precisava mostrar isso antes da primeira mordida. Serifa elegante, preto e marrom café, e um hambúrguer desenhado só com linhas. Na sacola, o recado vai junto: “Aproveite cada momento”.</p>""")
R("""      <span class="seg mono">03 · Açaíteria</span>
      <p>Açaí é energia. O “Y” virou um raio e a marca inteira fala de recarga: bateria, “recarregue-se” e “Já tomou sua dose diária de energia?”.</p>""",
"""      <span class="seg mono scr">03 · Açaiteria</span>
      <p>Açaí é energia, tá ligado? O Y virou um raio e a marca inteira fala de recarga: bateria, “recarregue-se” e “Já tomou sua dose diária de energia?”.</p>""")
R("""      <span class="kick mono">Criativos</span>
      <h2 id="t-cri" class="split">Posts que param o dedo.</h2>
      <p class="lede">Além da marca, a Turzin cria as peças do dia a dia: posts e anúncios com conceito, hierarquia clara e acabamento de campanha.</p>
      <p class="note">Estudos autorais, não oficiais e sem vínculo com as marcas retratadas, feitos para mostrar composição e manipulação de produto.</p>""",
"""      <span class="kick mono scr">Criativos</span>
      <h2 id="t-cri" class="split" data-pt>Posts que param o dedo</h2>
      <p class="lede">Além da marca, eu crio as peças do dia a dia: post e anúncio com conceito, hierarquia clara e acabamento de campanha.</p>
      <p class="note">Estudos autorais, não oficiais e sem vínculo com as marcas retratadas. Feitos pra mostrar composição e manipulação de produto.</p>""")
R("""  <span class="kick mono">Playground</span>
  <h2 id="t-play" class="split">Brinque um pouco.</h2>
  <p class="lede rv">Digite o nome do seu negócio e veja como ele ficaria com cara de marca.</p>""",
"""  <div class="kick-row"><span class="kick mono scr">Playground</span>{{SVG:simbolo:marca px}}</div>
  <h2 id="t-play" class="split" data-pt>Brinca um pouco</h2>
  <p class="lede rv">Digita o nome de um negócio e vê como ele fica com cara de marca.</p>""")
R("<h3>Teste a sua marca</h3>","<h3>Testa a sua marca</h3>")
R("""        <h3>Vire o jogo</h3>
        <p class="lede">Uma marca forte funciona no escuro e no claro. Mude o visual da página inteira e veja.</p>""",
"""        <h3>Vire o jogo</h3>
        <p class="lede">Marca forte funciona no escuro e no claro. Troca a página inteira e confere.</p>""")
R('<span class="flip-hint mono">Toque ou arraste o cartão para virar</span>','<span class="flip-hint mono">Toca ou arrasta o cartão pra virar</span>')
R("""  <span class="kick mono">Serviços</span>
  <h2 id="t-svc" class="split">Marca, site e movimento.</h2>""",
"""  <div class="kick-row"><span class="kick mono scr">Serviços</span>{{SVG:simbolo:marca px}}</div>
  <h2 id="t-svc" class="split" data-pt>Marca, site e movimento</h2>
  <p class="lede rv">Um logotipo é uma pequena parte de um todo. Sozinho, ele quase não tem força. Identidade visual é projeto completo: trabalho de engenharia, do tamanho da fonte até o outdoor.</p>""")
R("<p>A marca pensada a partir do seu negócio e do seu cliente.</p>","<p>A marca pensada a partir do negócio e do cliente. Não é só logo, é sistema.</p>")
R("<p>Sua marca nova já no ar, pronta para receber clientes.</p>","<p>A marca nova já no ar, com o mesmo cuidado em cada tela.</p>")
R("""  <span class="kick mono">Vamos conversar</span>
  <h2 id="t-end" class="split">Seu negócio merece parecer tão bom quanto ele é.</h2>
  <div class="contacts">
    <a class="btn fill mag js-whats" href="#contato" target="_blank" rel="noopener">Chamar no WhatsApp <span class="arr">→</span></a>""",
"""  {{SVG:simbolo:marca px end-sym}}
  <span class="kick mono scr">Contato</span>
  <h2 id="t-end" class="split">Quer trocar uma ideia?</h2>
  <p class="lede rv">Sobre um projeto, sobre design ou só pra falar de marca. Tô por aqui.</p>
  <div class="contacts">
    <a class="btn fill mag js-whats" href="#contato" target="_blank" rel="noopener">WhatsApp <span class="arr">→</span></a>""")
R("""<footer class="ft mono"><span class="logo" style="font-size:20px;text-transform:none">turzin<span>.</span></span><span>Identidade visual · Sites · Movimento</span><span>2026</span></footer>""",
"""<footer class="ft mono">{{SVG:assinatura-ponto:marca}}<span>Engenharia de design · Uberaba, MG</span><span class="nocaps">turzin. 2026</span></footer>""")

# ================= JS =================
R("mensagem: 'Olá, vi o portfólio da Turzin e quero conversar sobre a minha marca.',","mensagem: 'Fala, turzin. Vi o site e quis trocar uma ideia.',")
R("""  atrasoLetras: 0.008,    // atraso entre uma letra e outra ao abrir a página (segundos). 0 = todas juntas""",
"""  digitacao: 45,          // ms entre uma letra e outra no título digitado (menor = mais rápido)
  atrasoDigitacao: 300,   // ms antes de começar a digitar
  embaralhar: 650,        // ms do efeito de "decodificar" as etiquetas (letras aleatórias até formar a palavra)
  pixelImagem: 650,       // ms da revelação em pixels das imagens
  rastroCursor: true,     // rastro de pixels verdes atrás do cursor (PC). false = desliga""")
R("""const reduce = CONFIG.respeitarSistema && sistemaSemAnimacao;      // true = desliga as animações do site
const calmo = sistemaSemAnimacao;                                   // só acalma a onda contínua do título
if (reduce) document.documentElement.classList.add('parado');""",
"""const reduce = CONFIG.respeitarSistema && sistemaSemAnimacao;      // true = desliga as animações do site
const calmo = sistemaSemAnimacao;                                   // só acalma a onda contínua do título
if (reduce) document.documentElement.classList.add('parado'); else document.documentElement.classList.add('anima');""")
# título digitado
R("""const chars = [...ht.querySelectorAll('.ch')];
chars.forEach((c, i) => c.style.animationDelay = (i * CONFIG.atrasoLetras) + 's'); // cada letra sobe um pouquinho depois da anterior""",
"""const chars = [...ht.querySelectorAll('.ch')];
// ponto verde (data-pt) e cursor (data-cur) no fim das linhas
ht.querySelectorAll('.ln').forEach(ln => {
  if (ln.hasAttribute('data-pt')) { const d = document.createElement('span'); d.className = 'pt'; ln.lastElementChild.appendChild(d); }
  if (ln.hasAttribute('data-cur')) { const d = document.createElement('span'); d.className = 'cur'; ln.lastElementChild.appendChild(d); }
});
ht.querySelectorAll('.ln').forEach(l => l.setAttribute('aria-hidden', 'true'));
const fimCursor = ht.querySelector('.cur');
let fimDigitacao = 0;   // quando a digitação termina (a onda só começa depois)
(function digitar() {
  const seq = [...ht.querySelectorAll('.ch, .pt, .cur')];
  if (reduce) { fimCursor && fimCursor.classList.add('pisca'); return; }
  seq.forEach(e => { e.classList.add('tp'); if (!e.classList.contains('ch')) e.style.opacity = 0; });
  const anda = document.createElement('span'); anda.className = 'cur';           // cursor que anda com as letras
  seq.forEach((e, i) => setTimeout(() => {
    e.classList.remove('tp'); e.style.opacity = '';
    if (e === fimCursor) { anda.remove(); e.classList.add('pisca'); }
    else if (e.classList.contains('ch')) e.after(anda);
  }, CONFIG.atrasoDigitacao + i * CONFIG.digitacao));
  fimDigitacao = CONFIG.atrasoDigitacao + seq.length * CONFIG.digitacao + 300;
})();""")
R("if (on && ts > 900 && ts - last > 33) { last = ts; chars.forEach((c, i) => {","if (on && ts > Math.max(900, fimDigitacao) && ts - last > 33) { last = ts; chars.forEach((c, i) => {")
R("const wg = Math.round(800 - 600*k), wd = Math.round(100 - 22*kc);       // 800 = grossa, 200 = fina",
  "const wg = Math.round(800 - 600*k), wd = Math.round(78 + 22*kc);        // peso: 800 = grossa, 200 = fina · largura: 78 normal, abre perto do mouse")
R("setTimeout(measure, 900); addEventListener('resize', measure);","setTimeout(measure, 900); setTimeout(measure, 2600); addEventListener('resize', measure);")
# título dos projetos: largura condensada
R("""    title.style.fontVariationSettings = `"wght" ${800 - 450*ease(p*1.5)}, "wdth" 100`;
    title.style.letterSpacing = `${-0.045 + 0.03*ease(p*1.5)}em`;""",
"""    title.style.fontVariationSettings = `"wght" ${800 - 450*ease(p*1.5)}, "wdth" ${78 + 22*ease(p*1.5)}`;
    title.style.letterSpacing = `${-0.02 + 0.03*ease(p*1.5)}em`;""")
# títulos com ponto que cai
R("""document.querySelectorAll('.split').forEach(h => {
  h.innerHTML = h.textContent.trim().split(/\\s+/).map((w, i) => `<span class="w"><span style="transition-delay:${i*60}ms">${w}</span></span>`).join(' ');
  if (!reduce && h.getBoundingClientRect().top > innerHeight) {
    h.classList.add('split-pre');
    const o = new IntersectionObserver(es => { if (es[0].isIntersecting) { h.classList.remove('split-pre'); o.disconnect(); } }, { rootMargin: '0px 0px -10% 0px' }); o.observe(h);
  }
});""",
"""document.querySelectorAll('.split').forEach(h => {
  h.innerHTML = h.textContent.trim().split(/\\s+/).map((w, i) => `<span class="w"><span style="transition-delay:${i*60}ms">${w}</span></span>`).join(' ');
  if (h.hasAttribute('data-pt')) { const d = document.createElement('span'); d.className = 'pt'; h.lastElementChild.firstElementChild.appendChild(d); }  // ponto final quadrado
  if (!reduce && h.getBoundingClientRect().top > innerHeight) {
    h.classList.add('split-pre');
    const o = new IntersectionObserver(es => { if (es[0].isIntersecting) { h.classList.remove('split-pre'); h.classList.add('in'); o.disconnect(); } }, { rootMargin: '0px 0px -10% 0px' }); o.observe(h);
  } else h.classList.add('in');
});""")
# ================= JS: animações de tecnologia =================
R("""/* --- Abrir projeto: vai para a página de estudo de caso (campo pagina em PROJETOS) --- */""",
"""/* ================================================================
   ANIMAÇÕES DE TECNOLOGIA
   ================================================================ */
/* --- Símbolo que se monta em pixels: ordem dos blocos (maior primeiro) e disparo --- */
document.querySelectorAll('.px').forEach(svg => {
  [...svg.querySelectorAll('rect')].sort((a, b) => b.width.baseVal.value * b.height.baseVal.value - a.width.baseVal.value * a.height.baseVal.value)
    .forEach((r, i) => r.style.setProperty('--i', i));
});
if (!reduce) {
  const ioPx = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('on'); ioPx.unobserve(e.target); } }), { rootMargin: '0px 0px -12% 0px' });
  document.querySelectorAll('.px').forEach(el => ioPx.observe(el));
}

/* --- Decodificar texto: letras aleatórias até formar a palavra (etiquetas com class="scr") --- */
const GLIFOS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789#/<>_+=';
function embaralhar(el) {
  const alvo = el.dataset.txt || (el.dataset.txt = el.textContent); const t0 = performance.now();
  (function passo(t) {
    const k = Math.min(1, (t - t0) / CONFIG.embaralhar);
    el.textContent = [...alvo].map((c, i) => c === ' ' || c === '·' || i / alvo.length < k ? c : GLIFOS[(Math.random() * GLIFOS.length) | 0]).join('');
    if (k < 1) requestAnimationFrame(passo);
  })(t0);
}
if (!reduce) {
  const ioScr = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { embaralhar(e.target); ioScr.unobserve(e.target); } }), { rootMargin: '0px 0px -10% 0px' });
  document.querySelectorAll('.scr').forEach(el => ioScr.observe(el));
  // links do menu também "decodificam" ao passar o mouse
  document.querySelectorAll('.top nav a.l, .rail a span').forEach(a => a.addEventListener('pointerenter', () => embaralhar(a)));
}

/* --- Revelação em pixels: blocos na cor do fundo somem em ordem aleatória por cima da imagem --- */
function revelarPixels(el, cor, atraso = 0) {
  if (reduce || el.dataset.pxr) return; el.dataset.pxr = 1;
  const r = el.getBoundingClientRect(); if (!r.width) return;
  const c = document.createElement('canvas'); c.className = 'pxr';
  const cel = Math.max(14, Math.round(r.width / 18));                      // tamanho do "pixel"
  const cols = Math.ceil(r.width / cel), rows = Math.ceil(r.height / cel);
  c.width = cols; c.height = rows;                                          // 1 pixel do canvas = 1 bloco (fica leve)
  const g = c.getContext('2d'); g.fillStyle = cor; g.fillRect(0, 0, cols, rows);
  el.appendChild(c);
  const ordem = [...Array(cols * rows).keys()].sort(() => Math.random() - .5);
  let feitos = 0, t0 = 0;
  setTimeout(() => requestAnimationFrame(function passo(t) {
    if (!t0) t0 = t;
    const alvo = Math.floor(ordem.length * Math.min(1, (t - t0) / CONFIG.pixelImagem));
    for (; feitos < alvo; feitos++) { const k = ordem[feitos]; g.clearRect(k % cols, (k / cols) | 0, 1, 1); }
    if (feitos < ordem.length) requestAnimationFrame(passo); else c.remove();
  }), atraso);
}
if (!reduce) {
  const ioImg = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { revelarPixels(e.target, getComputedStyle(document.body).backgroundColor); ioImg.unobserve(e.target); } }), { threshold: .25 });
  document.querySelectorAll('.tilt').forEach(el => ioImg.observe(el));
}
// esteira do PC: as imagens de cada projeto se revelam em pixels quando o projeto entra
function revelarProjeto(c) { if (c.revelado || !c.figs) return; c.revelado = true; c.figs.forEach((f, i) => revelarPixels(f, getComputedStyle(c.sec).getPropertyValue('--b').trim() || '#333', 120 + i * 110)); }
addEventListener('scroll', () => chapters.forEach(c => { const r = c.sec.getBoundingClientRect(); if (r.top < innerHeight * .4 && r.bottom > 0) revelarProjeto(c); }), { passive: true });
chapters.forEach(c => { const sc = c.sec.querySelector('.scr'); });

/* --- HUD da primeira tela: coordenadas do mouse (PC) ou rolagem em % (celular) + grade que segue o mouse --- */
const hud = document.getElementById('hud'), heroEl = document.querySelector('.hero');
const pad = n => String(Math.max(0, Math.round(n))).padStart(4, '0');
if (fine) {
  let px = 0, py = 0, pend = false;
  addEventListener('pointermove', e => { px = e.clientX; py = e.clientY; if (!pend) { pend = true; requestAnimationFrame(() => {
    pend = false; hud.textContent = `X ${pad(px)} · Y ${pad(py + scrollY)}`;
    if (!reduce) { heroEl.style.setProperty('--gx', ((px / innerWidth - .5) * -24).toFixed(1) + 'px'); heroEl.style.setProperty('--gy', ((py / innerHeight - .5) * -24).toFixed(1) + 'px'); }
  }); } }, { passive: true });
} else {
  addEventListener('scroll', () => { const h = document.documentElement.scrollHeight - innerHeight; hud.textContent = `Scroll ${pad(h > 0 ? scrollY / h * 100 : 0).slice(1)}%`; }, { passive: true });
  hud.textContent = 'Scroll 000%';
}

/* --- Rastro de pixels atrás do cursor (PC) --- */
if (fine && !reduce && CONFIG.rastroCursor) {
  const pool = [...Array(16)].map(() => { const d = document.createElement('i'); d.className = 'trail'; document.body.appendChild(d); return d; });
  let k = 0, lx = 0, ly = 0;
  addEventListener('pointermove', e => {
    if (Math.hypot(e.clientX - lx, e.clientY - ly) < 22) return; lx = e.clientX; ly = e.clientY;
    const d = pool[k++ % pool.length], x = Math.round(e.clientX / 8) * 8, y = Math.round(e.clientY / 8) * 8;   // encaixa numa grade de 8px
    d.animate([{ opacity: .9, transform: `translate(${x}px, ${y}px) scale(1)` }, { opacity: 0, transform: `translate(${x}px, ${y + 10}px) scale(.4)` }], { duration: 520, easing: 'steps(4, end)' });
  }, { passive: true });
}

/* --- Abrir projeto: vai para a página de estudo de caso (campo pagina em PROJETOS) --- */""")
open(p,'w').write(s); print('ok edit2')
