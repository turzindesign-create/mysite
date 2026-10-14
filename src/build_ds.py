# Monta o design-system.html a partir do index.src.html (CSS e JS originais, sem mudar nada)
# + design-system.body.html (as seções) + uma camada de documentação (.ds-*).
import re
B = '/home/claude/site_v5/'
src = open(B + 'src/index.src.html').read()
body = open(B + 'src/design-system.body.html').read()

head = src[:src.index('</head>')]
head = head.replace('<meta name="description" content="turzin. é engenharia de design e tecnologia. Do papel à tela: design como função.">',
                    '<meta name="description" content="Design system da turzin.: marca, tipografia, cores, componentes, layout, movimento e voz.">\n<meta name="robots" content="noindex">')
i = src.index('<script src="js/lenis.min.js"></script>')
scripts = src[i:src.index('</body>')]
# a faixa de logos aponta para os capítulos da página inicial
scripts = scripts.replace('["01-isabella.webp","#c-isa"', '["01-isabella.webp","#c-isa"').replace('"#c-mar"', '"index.html#c-mar"').replace('"#c-acai"', '"index.html#c-acai"').replace('"#c-rei"', '"index.html#c-rei"').replace('"#c-kami"', '"index.html#c-kami"')

DOC_CSS = r'''
<!-- ================================================================
     CAMADA DE DOCUMENTAÇÃO DO DESIGN SYSTEM (.ds-*)
     Só organiza a página de documentação. Não muda nenhuma classe original:
     as classes .ds-hover / .ds-focus repetem as regras originais de :hover e :focus
     para mostrar esses estados parados, e .ds-ctx tira só o posicionamento de página
     de um componente quando ele aparece como amostra.
     ================================================================ -->
<style>
.ds-index { display: flex; flex-wrap: wrap; gap: 8px; padding: 26px var(--g) 0; }
.ds-index a { text-decoration: none; border: 1.5px solid var(--line); padding: 8px 12px; transition: border-color .2s; }
.ds-index a:hover { border-color: var(--green); }
.ds-h3 { font-weight: 800; font-size: clamp(22px, 2.2vw, 30px); margin: 64px 0 14px; }
.ds-p { color: var(--mute); max-width: 62ch; margin: 0 0 22px; }
.ds-p code, .lede code { font: 500 .88em var(--body); color: var(--ink); background: var(--panel); padding: 1px 5px; }
.ds-tag { display: inline-block; color: var(--green); border: 1.5px solid var(--green); padding: 7px 12px; margin-top: 36px; }
.ds-tag + .ds-tag { margin-left: 8px; }
.sec .ds-tag:first-child { margin: 0 0 30px; }

/* marca */
.ds-marks { margin-top: 44px; display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px; }
.ds-mark { margin: 0; display: grid; gap: 10px; }
.ds-mark figcaption { color: var(--mute); }
.ds-mk { aspect-ratio: 16 / 10; display: grid; place-items: center; padding: 18% 16%; border: 1px solid var(--line); }
.ds-mk svg { width: 100%; max-height: 100%; }
.ds-mk .ds-mk-sym, .ds-fundo .ds-mk:nth-child(2) svg { width: 46%; }
.ds-mk-escuro { background: #212121; } .ds-mk-escuro .t, .ds-mk-escuro .s { fill: #F7F7F7; } .ds-mk-escuro .d { fill: #44D62D; }
.ds-mk-verde { background: #44D62D; } .ds-mk-verde .t, .ds-mk-verde .s { fill: #F7F7F7; } .ds-mk-verde .d { fill: #212121; }
.ds-mk-claro { background: #F7F7F7; } .ds-mk-claro .t, .ds-mk-claro .s { fill: #212121; } .ds-mk-claro .d { fill: #44D62D; }
.ds-mk-clarov { background: #F7F7F7; } .ds-mk-clarov .t, .ds-mk-clarov .s { fill: #44D62D; } .ds-mk-clarov .d { fill: #212121; }
.ds-fundos { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 14px; }
.ds-fundo { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; align-content: start; }
.ds-fundo .ds-mk { aspect-ratio: 1; padding: 16%; }
.ds-fundo p { grid-column: 1 / -1; margin: 4px 0 0; font-size: 14px; color: var(--mute); }
.ds-fundo p b { display: block; color: var(--ink); margin-bottom: 4px; }
.ds-rules { margin-top: 40px; display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); border-top: 1px solid var(--line); }
.ds-rules > div { padding: 18px 18px 0 0; }
.ds-rules .mono { color: var(--green); }
.ds-rules p { margin: 6px 0 0; }

/* tipografia */
.ds-pesos { margin-top: 40px; display: flex; flex-wrap: wrap; gap: 8px 28px; }
.ds-pesos div { display: grid; gap: 4px; }
.ds-pesos .mono { color: var(--mute); }
.ds-ag { font-size: clamp(40px, 5vw, 64px); line-height: 1; }
.ds-w2 { font-weight: 200; } .ds-w3 { font-weight: 300; } .ds-w4 { font-weight: 400; } .ds-w5 { font-weight: 500; } .ds-w6 { font-weight: 600; } .ds-w7 { font-weight: 700; } .ds-w8 { font-weight: 800; }
.ds-medida { margin-top: 48px; }
.ds-medida b { color: var(--green); }
.ds-specs { border-top: 1px solid var(--line); }
.ds-row { display: grid; grid-template-columns: 200px minmax(0, 1fr) 190px; gap: 24px; align-items: center; padding: 22px 0; border-bottom: 1px solid var(--line); }
.ds-nome { color: var(--ink); display: grid; gap: 4px; }
.ds-nome small { font-size: 11px; color: var(--mute); letter-spacing: .02em; text-transform: none; }
.ds-prev { min-width: 0; overflow: hidden; }
.ds-val { text-align: right; color: var(--mute); font-variant-numeric: tabular-nums; display: grid; gap: 3px; }
.ds-val b { color: var(--ink); font-weight: 600; font-size: 14px; }
.ds-corpo { margin: 0; max-width: 60ch; }
/* .ds-ctx: amostra de um componente sem o posicionamento de página */
.hero.ds-ctx { padding: 0; min-height: 0; display: block; }
.hero.ds-ctx::before, .hero.ds-ctx::after { display: none; }
.hero.ds-ctx h1 { max-width: none; }
.sec.ds-ctx { padding: 0; }
.sec.end.ds-ctx { padding: 18px 20px; }
.svc.ds-ctx { margin: 0; display: block; border: 0; }
.contacts.ds-ctx { margin: 0; }
.lede.ds-ctx, .note.ds-ctx { margin: 0; }
.ch-title.ds-ctx { white-space: normal; }
.tilt.ds-ctx { overflow: visible; }
.tilt.ds-ctx .rev { position: static; transform: none; background: none; color: inherit; padding: 0; }
.stage.ds-ctx { position: relative; top: auto; height: auto; min-height: 0; display: block; overflow: visible; padding: 18px 20px; }
.htrack.ds-ctx { position: relative; display: block; }
.htrack.ds-ctx figure { height: auto; aspect-ratio: auto; }
.htrack.ds-ctx figcaption { position: static; display: inline-block; opacity: 1; transform: none; }
.rail.ds-ctx { position: static; transform: none; display: grid; justify-items: end; }
.rail.ds-ctx a { cursor: default; }

/* cores e superfícies */
.ds-swatches { display: grid; grid-template-columns: repeat(auto-fill, minmax(190px, 1fr)); gap: 12px; }
.ds-sw { border: 1px solid var(--line); display: grid; grid-template-rows: 96px auto; min-width: 0; }
.ds-sw > i { display: block; border-bottom: 1px solid var(--line); }
.ds-sw > div { padding: 12px; display: grid; gap: 3px; min-width: 0; }
.ds-sw span { font-size: 14px; color: var(--mute); }
.ds-sw code { font: 500 12px var(--body); color: var(--ink); overflow-wrap: anywhere; }
.ds-mode { margin-top: 22px; display: flex; flex-wrap: wrap; gap: 16px 28px; align-items: center; }
.ds-mode .ds-p { margin: 0; }
.ds-contraste { margin-top: 16px; display: grid; grid-template-columns: repeat(auto-fit, minmax(170px, 1fr)); border-top: 1px solid var(--line); }
.ds-contraste div { padding: 14px 14px 0 0; display: grid; gap: 4px; }
.ds-contraste b { font: 800 28px var(--display); font-variation-settings: "wdth" var(--largura); }
.ds-contraste .mono { color: var(--mute); }
.ds-surfs { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 12px; }
.ds-surfs > figure { margin: 0; display: grid; gap: 8px; align-content: start; }
.ds-surfs > figure > div { min-height: 130px; display: grid; place-items: center; }
.ds-surfs figcaption { color: var(--mute); }
.ds-surf-ground { background: var(--ground); border: 1px solid var(--line); }
.ds-surf { display: grid; place-items: center; }
.ds-ctx-img img { width: 100%; aspect-ratio: 4 / 3; object-fit: cover; }
.ds-ctx-img .rev { transform: none; }
.ds-surf-over { background: url(img/home/3-projetos/isabella/placa.webp) center / cover; }

/* componentes */
.ds-states { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px; margin-bottom: 14px; }
.ds-state { border: 1px solid var(--line); padding: 18px; display: grid; gap: 14px; align-content: start; justify-items: start; min-width: 0; }
.ds-state > .mono:first-child { color: var(--mute); }
.ds-state > .ds-surf, .ds-state > .stage, .ds-state > .sec { justify-self: stretch; }
.ds-pair { display: grid; gap: 12px; }
.ds-state.ctl { margin: 0; gap: 14px; }
.ds-state.ctl label { justify-self: stretch; }
/* estados parados: cópia das regras :hover / :focus-visible originais */
.btn.ds-hover::before { transform: none; }
.btn.ds-hover { color: var(--green-ink); border-color: var(--green); }
.btn.fill.ds-hover { color: var(--ground); border-color: var(--ink); }
.btn.ds-hover .arr { transform: translateX(4px); }
.ds-focus { outline: 2px solid var(--green); outline-offset: 3px; }
.copy.ds-hover { background: var(--green-ink); color: var(--green); }
.ctl input.ds-focus-in { border-bottom-color: var(--green); }

/* layout */
.ds-bar { height: 22px; background: var(--green); }
.ds-bar-g { width: var(--g); }
.ds-bar-sec { width: clamp(80px, 11vw, 150px); }
.ds-cols { display: grid; height: 54px; }
.ds-cols i { background: var(--panel); border: 1px dashed var(--line); }
.ds-c-hero { grid-template-columns: 1.3fr .7fr; column-gap: 3vw; }
.ds-c-stage { grid-template-columns: 1fr 1.05fr; column-gap: 4vw; }
.ds-c-cri { grid-template-columns: .9fr 1.3fr; column-gap: 64px; }
.ds-c-play { grid-template-columns: 1fr 1.5fr; column-gap: 16px; }
.ds-c-svc { grid-template-columns: 1fr 1fr; }
.ds-cantos { display: flex; gap: 14px; }
.ds-cantos i { width: 56px; height: 56px; border: 1.5px solid var(--ink); }
.ds-r0 { border-radius: 0; } .ds-r6 { border-radius: 6px; } .ds-r10 { border-radius: 10px; }

/* movimento */
.ds-motion { margin-top: 44px; display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 14px; }
.ds-mcard { border: 1px solid var(--line); padding: 18px; display: grid; gap: 14px; align-content: start; justify-items: start; min-width: 0; }
.ds-mcard p { margin: 6px 0 0; font-size: 14px; color: var(--mute); }
.ds-stagearea { justify-self: stretch; min-height: 170px; display: grid; place-items: center; overflow: hidden; background: var(--panel); padding: 14px; }
.ds-demo-px { width: 90px; }
.ds-demo-pxr { width: 150px; }
.ds-demo-pxr img { aspect-ratio: 4 / 5; }
.ds-demo-split { font-size: clamp(30px, 3vw, 40px); }
.ds-demo-rv { padding: 22px; }
.ds-live { color: var(--green); }
.ds-cards3d { perspective: 1000px; }
.ds-cards3d .c { width: 110px; aspect-ratio: 4 / 5; border-radius: 10px; overflow: hidden; box-shadow: 0 30px 60px -24px rgba(0,0,0,.7); --r: -6deg; --z: 0px; transform: rotate(var(--r)); }
@media (min-width: 1000px) { .ds-cards3d .c { animation: deal var(--t-cartoes) var(--curva) both, bob var(--t-flutuar) ease-in-out infinite alternate; } }
.ds-cards3d .c img { width: 100%; height: 100%; object-fit: cover; }
.ds-hud-demo { font-size: 16px; }

/* voz */
.ds-voz { margin-top: 44px; display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 14px; }
.ds-voz .panel { display: grid; gap: 12px; align-content: start; }
.ds-voz .mono { color: var(--mute); }
.ds-voz .ds-ok { color: var(--green); }
.ds-fala { margin: 0; font: 800 clamp(22px, 2.2vw, 30px)/1.05 var(--display); text-transform: uppercase; font-variation-settings: "wdth" var(--largura); }
.ds-lista { margin: 0; padding: 0; list-style: none; display: grid; gap: 10px; }
.ds-lista li::before { content: ""; display: inline-block; width: 7px; height: 7px; margin: 0 10px 2px 0; background: var(--green); }
.ds-proibidas span { text-decoration: line-through; border-color: var(--line); }

@media (max-width: 860px) {
  .ds-row { grid-template-columns: 1fr; gap: 12px; }
  .ds-val { text-align: left; }
  .ds-tag + .ds-tag { margin-left: 0; }
}
</style>
'''

DOC_JS = r'''
<script>
/* ================================================================
   CAMADA DE DOCUMENTAÇÃO (JS): mede os estilos ao vivo e liga os botões "Repetir"
   aos efeitos ORIGINAIS do site (funções e animações do script acima).
   ================================================================ */
(function () {
  const px = v => Math.round(parseFloat(v) * 10) / 10;
  function medir() {
    document.getElementById('ds-largura').textContent = innerWidth + 'px';
    document.querySelectorAll('[data-ds-spec]').forEach(el => {
      const cs = getComputedStyle(el), row = el.closest('.ds-row'), out = row && row.querySelector('.ds-val');
      if (!out) return;
      const lh = cs.lineHeight === 'normal' ? 'normal' : px(cs.lineHeight) + 'px';
      const fvs = cs.fontVariationSettings && cs.fontVariationSettings !== 'normal' ? cs.fontVariationSettings.replace(/"/g, '') : 'peso ' + cs.fontWeight;
      const ls = cs.letterSpacing === 'normal' ? '0' : px(parseFloat(cs.letterSpacing) / parseFloat(cs.fontSize) * 100) / 100 + 'em';
      out.innerHTML = `<b>${px(cs.fontSize)}px / ${lh}</b><span>${fvs}</span><span>espaço ${ls}${cs.textTransform === 'uppercase' ? ' · caixa alta' : ''}</span>`;
    });
    document.querySelectorAll('[data-token]').forEach(c => c.textContent = getComputedStyle(document.documentElement).getPropertyValue(c.dataset.token).trim());
    const g = document.querySelector('[data-ds-px="--g"]'); if (g) g.innerHTML = `<b>${px(getComputedStyle(document.querySelector('.ds-bar-g')).width)}px</b><span>nesta tela</span>`;
    const s = document.querySelector('[data-ds-pad=".sec"]'); if (s) s.innerHTML = `<b>${px(getComputedStyle(document.querySelector('#ds-tipo')).paddingTop)}px</b><span>em cima e embaixo</span>`;
  }
  // cores dos projetos, lidas de PROJETOS (o mesmo objeto do site)
  document.getElementById('ds-projetos').innerHTML = Object.values(PROJETOS).map(p =>
    `<div class="ds-sw"><i style="background:${p.cor}"></i><div><b class="mono">${p.nome}</b><span>Fundo do capítulo</span><code>${p.cor}</code></div></div>`).join('');
  medir(); addEventListener('resize', medir);
  if (document.fonts) document.fonts.ready.then(medir);
  new MutationObserver(medir).observe(document.documentElement, { attributes: true, attributeFilter: ['data-mode'] });

  // reinicia uma animação CSS original
  const reinicia = (el, cls) => { el.classList.remove(cls); void el.offsetWidth; el.classList.add(cls); };
  const acoes = {
    px: () => reinicia(document.querySelector('.ds-demo-px'), 'on'),
    scr: () => embaralhar(document.querySelector('.ds-demo-scr')),
    pxr: () => { const el = document.querySelector('.ds-demo-pxr'); el.querySelectorAll('canvas.pxr').forEach(c => c.remove()); delete el.dataset.pxr; revelarPixels(el, getComputedStyle(document.body).backgroundColor); },
    split: () => { const h = document.querySelector('.ds-demo-split'); h.classList.remove('in'); h.classList.add('split-pre'); void h.offsetWidth; requestAnimationFrame(() => requestAnimationFrame(() => { h.classList.remove('split-pre'); h.classList.add('in'); })); },
    rv: () => { const b = document.querySelector('.ds-demo-rv'); b.classList.add('pre'); void b.offsetWidth; requestAnimationFrame(() => requestAnimationFrame(() => b.classList.remove('pre'))); },
    deal: () => { const c = document.querySelector('.ds-cards3d .c'); c.style.animation = 'none'; void c.offsetWidth; c.style.animation = ''; },
    hero: () => { scrollTo(0, 0); location.reload(); },
  };
  document.querySelectorAll('[data-replay]').forEach(b => b.addEventListener('click', () => acoes[b.dataset.replay]()));
})();
</script>
'''
out = head + DOC_CSS + '</head>\n' + body + '\n' + scripts.replace('<script src="musica.js" defer></script>', DOC_JS + '<script src="musica.js" defer></script>') + '</body>\n</html>\n'

def svg(m):
    nome, cls = m.group(1), m.group(2)
    s = open(f'{B}img/marca/{nome}.svg').read().replace(' xmlns="http://www.w3.org/2000/svg"', '')
    return s.replace('<svg ', f'<svg class="{cls}" aria-hidden="true" focusable="false" ', 1)
out = re.sub(r'\{\{SVG:([\w-]+):([^}]*)\}\}', svg, out)
open(B + 'design-system.html', 'w').write(out); print(len(out))
