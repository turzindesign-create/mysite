p='/home/claude/site_v5/src/index.src.html'; s=open(p).read()
def R(a,b):
    global s
    assert a in s, 'NAO ACHEI: '+a[:100]
    s=s.replace(a,b,1)
# ---------- sem Uberaba ----------
R(" Tecnologia, design e planejamento no mesmo trampo. Uberaba, MG.\""," Tecnologia, design e planejamento no mesmo trampo.\"")
R('<span>Engenharia de design</span><span>Uberaba, MG</span><span class="hud"','<span>Engenharia de design</span><span>Identidade · Site · Movimento</span><span class="hud"')
R('<span>Engenharia de design · Uberaba, MG</span>','<span>Engenharia de design</span>')
# ---------- fontes do playground só carregam perto dele (site mais leve) ----------
R('&family=Bodoni+Moda:wght@500;700&family=Jost:wght@400;700&family=Fraunces:opsz,wght@9..144,400;9..144,600&display=swap">','&display=swap">')
# ---------- faixa de logos (links) ----------
R(".marquee img { height: clamp(140px, 20vw, 230px); width: auto; aspect-ratio: 4/5; object-fit: cover; border-radius: 4px; }",
""".marquee img { height: clamp(140px, 20vw, 230px); width: auto; aspect-ratio: 4/5; object-fit: cover; border-radius: 0; }
/* [GUIA: faixa-logos] cada logo é um link para o projeto na mesma página */
.marquee a { display: block; position: relative; transition: transform .25s var(--curva); }
.marquee a:hover, .marquee a:focus-visible { transform: translateY(-6px); }
.marquee:hover .row2, .marquee:focus-within .row2 { animation-play-state: paused; }""")
R('<div class="marquee" aria-hidden="true"><div class="row2" id="mq"></div></div>','<nav class="marquee" aria-label="Projetos"><div class="row2" id="mq"></div></nav>')
R("""  faixa: ["01-cartao-isabella.jpg","02-logo-margarett.jpg","03-logo-acai-yo.jpg","04-placa-isabella.jpg","05-sacola-margarett.jpg",
          "06-polo-acai-yo.jpg","07-post-isabella.jpg","08-post-margarett.jpg","09-embalagem-acai-yo.jpg","10-envelope-isabella.jpg"]""",
"""  // cada item: [imagem da pasta img/home/2-faixa, seção do projeto (âncora), nome]
  faixa: [["01-isabella.webp","#c-isa","Isabella Gutierres"],["02-margarett.webp","#c-mar","Margarett"],["03-acai-yo.webp","#c-acai","Açaí Yo"],
          ["04-reigotta.webp","#c-rei","Reigotta"],["05-kamisama.webp","#c-kami","Kamisama"]]""")
R("""document.getElementById('mq').innerHTML = [...CONFIG.faixa, ...CONFIG.faixa].map(p => `<img src="img/home/2-faixa/${p}" alt="" loading="lazy">`).join('');""",
"""// a lista aparece 4x seguidas para a faixa dar a volta sem emenda; só a primeira cópia é lida por leitores de tela e pelo teclado
document.getElementById('mq').innerHTML = [0,1,2,3].map(k => CONFIG.faixa.map(([f, link, nome]) =>
  `<a href="${link}" ${k ? 'tabindex="-1" aria-hidden="true"' : ''} data-cursor="Ver"><img src="img/home/2-faixa/${f}" alt="${k ? '' : 'Logo ' + nome}" width="400" height="500" decoding="async"></a>`).join('')).join('');""")
# ---------- novos projetos ----------
R('  <a href="#c-acai" data-t="c-acai"><span>Açaí Yo</span><i></i></a>','  <a href="#c-acai" data-t="c-acai"><span>Açaí Yo</span><i></i></a>\n  <a href="#c-rei" data-t="c-rei"><span>Reigotta</span><i></i></a>\n  <a href="#c-kami" data-t="c-kami"><span>Kamisama</span><i></i></a>')
for a,b in [('01 / 03','01 / 05'),('02 / 03','02 / 05'),('03 / 03','03 / 05')]: R(a,b)
R("""<!-- ===== [GUIA: texto-criativos] CRIATIVOS =====""",
"""<section class="chapter" id="c-rei" data-set="rei" aria-labelledby="t-rei">
  <div class="stage">
    <h2 class="ch-title" id="t-rei">Reigotta</h2>
    <div class="ch-info">
      <span class="seg mono scr">04 · Moda fitness · E-commerce</span>
      <p>Roupa de treino pede energia. O símbolo é um batimento cardíaco que forma uma coroa, e o rosa com verde neon faz a marca aparecer no meio do feed.</p>
      <div class="chips"><span>Símbolo</span><span>Paleta</span><span>Etiquetas</span><span>Sacola</span><span>E-commerce</span></div>
      <button class="btn mag open" data-cursor="Ver">Ver estudo de caso <span class="arr">→</span></button>
    </div>
    <div class="layers"></div>
    <span class="ch-count mono">04 / 05</span>
  </div>
</section>

<section class="chapter" id="c-kami" data-set="kami" aria-labelledby="t-kami">
  <div class="stage">
    <h2 class="ch-title" id="t-kami">Kamisama</h2>
    <div class="ch-info">
      <span class="seg mono scr">05 · Delivery japonês</span>
      <p>Delivery com cara de restaurante. Um guerreiro envolvido por um dragão foge do clichê do hashi, e o laranja, o vinho e o salmão saem direto dos pratos.</p>
      <div class="chips"><span>Símbolo</span><span>Paleta</span><span>Ícones</span><span>Embalagem</span><span>Instagram</span></div>
      <button class="btn mag open" data-cursor="Ver">Ver estudo de caso <span class="arr">→</span></button>
    </div>
    <div class="layers"></div>
    <span class="ch-count mono">05 / 05</span>
  </div>
</section>

<!-- ===== [GUIA: texto-criativos] CRIATIVOS =====""")
R("""    camadas: ["logo-vertical.jpg","embalagem-acai.jpg","uniforme-polo.jpg"] }""",
"""    camadas: ["logo-vertical.jpg","embalagem-acai.jpg","uniforme-polo.jpg"] },
  rei: { nome: "Reigotta", cor: "#FF3EB5", pagina: "reigotta.html", pasta: "img/home/3-projetos/reigotta/",
    itens: [["post-novos-ciclos.png","Post “coleção novos ciclos”"],["etiqueta-verde.png","Etiqueta de coleção",1],["post-natural.png","Post “conecte-se ao natural”"],["cartaz-top.png","Cartaz “Top Boxeadora”",1],["sacola.png","Sacola",1],["post-nova-colecao.png","Post “nova coleção”",1],["cartoes.png","Cartões de visita",1],["etiqueta-rosa.png","Etiqueta de produto",1]],
    camadas: ["post-novos-ciclos.png","post-natural.png","sacola.png"] },
  kami: { nome: "Kamisama", cor: "#FF5C35", pagina: "kamisama.html", pasta: "img/home/3-projetos/kamisama/",
    itens: [["logo.png","Logo vertical",1],["sushi-simbolo.png","Símbolo e direção de imagem",1],["embalagem-larga.png","Embalagem de delivery",1],["posts.png","Posts para Instagram",1],["simbolo.png","Símbolo sobre o vinho",1],["logo-horizontal.png","Logo horizontal",1]],
    camadas: ["logo.png","embalagem-larga.png","posts.png"] }""")
# ---------- criativos: no celular, texto embaixo da imagem ----------
R("@media (max-width: 860px) { .cri { grid-template-columns: 1fr; } .tilt .rev { transform: none; } }",
"""/* [GUIA: criativos-celular] no celular o nome do post fica EMBAIXO da imagem, sem cobrir o post */
@media (max-width: 860px) { .cri { grid-template-columns: 1fr; } .tilt { overflow: visible; } .tilt .rev { position: static; transform: none; background: none; color: var(--ink); padding: 10px 0 0; } .tilt .rev .mono { color: var(--mute); } }""")
# ---------- playground ----------
R("""            <button data-s="elegante" aria-pressed="true">Elegante</button>
            <button data-s="energetico" aria-pressed="false">Energético</button>
            <button data-s="acolhedor" aria-pressed="false">Acolhedor</button>""","""            <!-- os botões são criados pelo JS a partir de ESTILOS -->""")
R("""        <div><span class="mono" style="color:var(--mute)">Cores</span>""",
"""        <!-- [GUIA: playground-subtitulo] subtítulo do cartão: a pessoa escreve o que quiser. Vazio = frase da personalidade -->
        <label><span class="mono" style="color:var(--mute)">Subtítulo do cartão</span><input type="text" id="pg-sub" maxlength="34" autocomplete="off" placeholder="Desde 2026"></label>
        <div><span class="mono" style="color:var(--mute)">Cores</span>""")
R("""        <span class="flip-hint mono">Toca ou arrasta o cartão pra virar</span>""",
"""        <span class="flip-hint mono">Toca ou arrasta o cartão pra virar</span>
        <!-- [GUIA: playground-compartilhar] gera uma imagem do cartão para compartilhar (ou baixar no PC) -->
        <div class="share-row"><button class="btn fill" type="button" id="pg-share">Compartilhar cartão <span class="arr">↗</span></button><span class="mono share-msg" id="pg-msg" role="status"></span></div>""")
R(".flip-hint { grid-column: 1 / -1; color: var(--mute); }",".flip-hint { grid-column: 1 / -1; color: var(--mute); }\n.share-row { grid-column: 1 / -1; display: flex; flex-wrap: wrap; gap: 12px; align-items: center; justify-content: center; }\n.share-msg { color: var(--mute); }\n.seg-btns { max-width: 100%; }")
# ESTILOS: mais personalidades
R("""                cores: [["#b44a2f","#fbeee0"],["#f3e3cf","#7a3b2e"],["#3d5a40","#f4ead8"],["#a3122b","#ffe08a"]] }
};""","""                cores: [["#b44a2f","#fbeee0"],["#f3e3cf","#7a3b2e"],["#3d5a40","#f4ead8"],["#a3122b","#ffe08a"]] },
  minimalista:{ nome: 'Minimalista', fonte: "'Jost', system-ui, sans-serif", peso: 400, caixa: 'lowercase', espaco: '.02em', frase: 'menos, só que melhor',
                cores: [["#f4f4f2","#1a1a1a"],["#1a1a1a","#f4f4f2"],["#e9e6df","#5b5a55"],["#dfe6e9","#22313f"]] },
  urbano:     { nome: 'Urbano', fonte: "'Anton', Impact, sans-serif", peso: 400, caixa: 'uppercase', espaco: '.01em', frase: 'Da rua pro mundo',
                cores: [["#111111","#ffd400"],["#ffd400","#111111"],["#e63b2e","#ffffff"],["#2b2b2b","#9cff57"]] },
  tecnologico:{ nome: 'Tecnológico', fonte: "'Space Grotesk', system-ui, sans-serif", peso: 600, caixa: 'none', espaco: '-.03em', frase: 'Feito pra escalar',
                cores: [["#0b1020","#5cf2ff"],["#f2f5ff","#2a35ff"],["#101010","#c6ff3d"],["#2a35ff","#ffffff"]] },
  divertido:  { nome: 'Divertido', fonte: "'Pacifico', cursive", peso: 400, caixa: 'none', espaco: '0', frase: 'Feito com alegria',
                cores: [["#ff6fae","#fff4c2"],["#7c4dff","#fff1fb"],["#ffd23f","#e8336b"],["#2ec4b6","#ffffff"]] }
};
// [GUIA: playground-fontes] fontes das marcas de teste: só carregam quando o Playground chega perto (deixa o site mais rápido)
const FONTES_PLAYGROUND = 'https://fonts.googleapis.com/css2?family=Bodoni+Moda:wght@500;700&family=Jost:wght@400;700&family=Fraunces:opsz,wght@9..144,400;9..144,600&family=Anton&family=Space+Grotesk:wght@600&family=Pacifico&display=swap';""")
# JS playground
R("""let pg = { s: 'elegante', i: 0 };
const pgName = document.getElementById('pg-name'), swBox = document.getElementById('pg-sw');""",
"""let pg = { s: 'elegante', i: 0 };
const pgName = document.getElementById('pg-name'), pgSub = document.getElementById('pg-sub'), swBox = document.getElementById('pg-sw');
// carrega as fontes do playground só quando ele está perto da tela
const pgSec = document.getElementById('playground'); let fontesOk = false;
new IntersectionObserver((es, o) => { if (es[0].isIntersecting && !fontesOk) { fontesOk = true; const l = document.createElement('link'); l.rel = 'stylesheet'; l.href = FONTES_PLAYGROUND; document.head.appendChild(l); o.disconnect(); } }, { rootMargin: '900px 0px' }).observe(pgSec);
// botões de personalidade a partir de ESTILOS
const styleBox = document.getElementById('pg-style');
styleBox.innerHTML = Object.entries(ESTILOS).map(([k, v]) => `<button data-s="${k}" aria-pressed="${k === pg.s}">${v.nome || k[0].toUpperCase() + k.slice(1)}</button>`).join('');""")
R("""  document.querySelectorAll('#pg-stage [data-t]').forEach(n => n.textContent = st.frase);""",
"""  const frase = pgSub.value.trim() || st.frase; pgSub.placeholder = st.frase;
  document.querySelectorAll('#pg-stage [data-t]').forEach(n => n.textContent = frase);""")
R("""pgName.addEventListener('input', paintBrand);""","""pgName.addEventListener('input', paintBrand); pgSub.addEventListener('input', paintBrand);""")
R("""/* --- Botão "Modo papel" (troca as cores para as de :root[data-mode="papel"]) --- */""",
"""/* --- Compartilhar o cartão: desenha a frente do cartão numa imagem e abre o compartilhar do celular (no PC, baixa a imagem) --- */
async function imagemDoCartao() {
  const st = ESTILOS[pg.s], [bg, fg] = st.cores[pg.i];
  const nome = pgName.value.trim() || 'Sua Marca', frase = pgSub.value.trim() || st.frase;
  const W = 1200, H = 686, c = document.createElement('canvas'); c.width = W; c.height = H; const g = c.getContext('2d');
  const caixa = t => st.caixa === 'uppercase' ? t.toUpperCase() : st.caixa === 'lowercase' ? t.toLowerCase() : t;
  try { await document.fonts.load(`${st.peso} 100px ${st.fonte}`); } catch (e) {}
  g.fillStyle = bg; g.fillRect(0, 0, W, H); g.fillStyle = fg; g.textAlign = 'center'; g.textBaseline = 'middle';
  let tam = 130; g.font = `${st.peso} ${tam}px ${st.fonte}`;
  if ('letterSpacing' in g) g.letterSpacing = st.espaco.replace('em', '') * tam + 'px';
  while (g.measureText(caixa(nome)).width > W * .82 && tam > 40) { tam -= 4; g.font = `${st.peso} ${tam}px ${st.fonte}`; }
  g.fillText(caixa(nome), W / 2, H / 2 - 20);
  g.font = `600 26px 'Bricolage Grotesque', sans-serif`; if ('letterSpacing' in g) g.letterSpacing = '6px'; g.globalAlpha = .8;
  g.fillText(frase.toUpperCase(), W / 2, H / 2 + tam * .55 + 10);
  g.globalAlpha = .5; g.font = `500 20px 'Bricolage Grotesque', sans-serif`; if ('letterSpacing' in g) g.letterSpacing = '2px';
  g.fillText('feito no playground da turzin.', W / 2, H - 40);
  return new Promise(r => c.toBlob(r, 'image/png'));
}
const shareBtn = document.getElementById('pg-share'), shareMsg = document.getElementById('pg-msg');
shareBtn.onclick = async () => {
  const blob = await imagemDoCartao(); const nomeArq = (pgName.value.trim() || 'minha-marca').toLowerCase().replace(/[^a-z0-9]+/g, '-') + '.png';
  const file = new File([blob], nomeArq, { type: 'image/png' });
  try {
    if (navigator.canShare && navigator.canShare({ files: [file] })) { await navigator.share({ files: [file], title: 'Minha marca', text: 'Fiz no playground da turzin.' }); shareMsg.textContent = 'Compartilhado'; return; }
  } catch (e) { if (e.name === 'AbortError') return; }
  const a = document.createElement('a'); a.href = URL.createObjectURL(blob); a.download = nomeArq; document.body.appendChild(a); a.click(); a.remove();
  shareMsg.textContent = 'Imagem baixada';
  setTimeout(() => shareMsg.textContent = '', 2500);
};

/* --- Botão "Modo papel" (troca as cores para as de :root[data-mode="papel"]) --- */""")
open(p,'w').write(s); print('ok edit3')
