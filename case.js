/* ================================================================
   ANIMAÇÕES DAS PÁGINAS DE PROJETO (compartilhado pelas 3 páginas)
   Não precisa mexer. Cada parte está explicada.
   ================================================================ */
(function () {
  /* --- A página sempre abre no topo (capa), mesmo vindo de outro lugar do site --- */
  if ('scrollRestoration' in history) history.scrollRestoration = 'manual';
  if (location.hash) history.replaceState(null, '', location.pathname + location.search); // tira #capitulo do endereço
  const topo = () => scrollTo(0, 0);
  topo(); addEventListener('DOMContentLoaded', topo); addEventListener('load', topo); addEventListener('pageshow', topo);

  const cl = (v, a = 0, b = 1) => Math.max(a, Math.min(b, v));

  /* --- Título da capa: separa as palavras para elas subirem uma a uma --- */
  document.querySelectorAll('.capa h1').forEach(h => {
    const pt = h.querySelector('.pt'); if (pt) pt.remove();          // ponto final quadrado volta no fim da última palavra
    h.innerHTML = h.textContent.trim().split(/\s+/).map((w, i) => `<span class="w"><span style="animation-delay:${0.08 + i * 0.09}s">${w}</span></span>`).join(' ');
    if (pt) h.querySelector('.w:last-child > span').appendChild(pt);
  });

  /* --- Coisas que animam quando aparecem na tela (desenhos, cores, proporção) --- */
  const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); e.target.classList.remove('pre'); io.unobserve(e.target); } }), { rootMargin: '0px 0px -12% 0px' });
  document.querySelectorAll('.cor, .proporcao').forEach(el => io.observe(el));
  // blocos que sobem: só os que começam fora da tela
  document.querySelectorAll('.rv').forEach(el => { if (el.getBoundingClientRect().top > innerHeight) { el.classList.add('pre'); io.observe(el); } });
  // atraso em cascata nos quadros de cor
  document.querySelectorAll('.cor').forEach((c, i) => c.querySelector('.amostra').style.transitionDelay = (i * 0.12) + 's');

  /* --- Barra de leitura, topo sólido, sumário ativo e zoom da imagem da capa --- */
  const read = document.querySelector('.read'), top = document.querySelector('.top'), capaImg = document.querySelector('.capa-img img');
  const links = [...document.querySelectorAll('.sumario a')];
  const caps = links.map(a => document.querySelector(a.getAttribute('href')));
  function onScroll() {
    const h = document.documentElement.scrollHeight - innerHeight;
    read.style.width = (h > 0 ? scrollY / h * 100 : 0) + '%';
    top.classList.toggle('solid', scrollY > innerHeight * .6);
    let cur = 0; caps.forEach((c, i) => { if (c && c.getBoundingClientRect().top < innerHeight * .35) cur = i; });
    links.forEach((a, i) => a.classList.toggle('on', i === cur));
    if (capaImg) { const r = capaImg.parentElement.getBoundingClientRect(); const p = cl(1 - r.bottom / (innerHeight + r.height)); capaImg.style.transform = `translateY(${-p * 12}%) scale(${1.04 - p * .04})`; }
  }
  addEventListener('scroll', () => requestAnimationFrame(onScroll), { passive: true });
  addEventListener('resize', onScroll); onScroll();
})();
