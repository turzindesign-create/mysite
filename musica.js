/* ================================================================
   MÚSICA DE FUNDO (só no PC) + BOTÃO DE SOM
   Usado em todas as páginas do site.
   - A música é um vídeo do YouTube tocando escondido (só o áudio importa).
   - Navegadores não deixam tocar som sozinho: a música começa sem som
     e liga no primeiro clique ou tecla da pessoa na página.
   - O botão no canto liga e desliga. A escolha e o ponto da música
     ficam salvos, então ao trocar de página ela continua de onde parou.
   ================================================================ */
(function () {
  // [GUIA: musica-config] troque o ID para usar outra música (é o código depois de "watch?v=" no link do YouTube)
  const VIDEO = 'Vle8y4Ntrp0';
  const VOLUME = 35;            // volume de 0 a 100
  const SO_NO_PC = true;        // true = não toca no celular

  const pc = matchMedia('(pointer: fine)').matches && innerWidth >= 1024;
  if (SO_NO_PC && !pc) return;

  const guarda = { get(k, d) { try { const v = localStorage.getItem(k); return v === null ? d : v; } catch (e) { return d; } },
                   set(k, v) { try { localStorage.setItem(k, v); } catch (e) {} } };
  let querSom = guarda.get('turzin-som', 'on') === 'on';   // escolha da pessoa
  let liberado = false;                                    // já houve clique/tecla na página?
  let inicio = Math.floor(+guarda.get('turzin-som-t', 0)) || 0;
  let tempo = inicio;

  // player escondido. Para o site abrir rápido, o YouTube só é carregado no primeiro
  // clique/tecla da pessoa ou 4 segundos depois que a página terminou de carregar.
  let fr = null;
  function criarPlayer() {
    if (fr) return;
    fr = document.createElement('iframe');
    fr.title = 'Música de fundo'; fr.setAttribute('aria-hidden', 'true'); fr.tabIndex = -1;
    fr.allow = 'autoplay; encrypted-media'; fr.referrerPolicy = 'strict-origin-when-cross-origin';
    fr.src = `https://www.youtube-nocookie.com/embed/${VIDEO}?enablejsapi=1&autoplay=1&mute=1&loop=1&playlist=${VIDEO}&controls=0&start=${inicio}&playsinline=1&origin=${encodeURIComponent(location.origin)}`;
    fr.style.cssText = 'position:fixed;width:1px;height:1px;left:-10px;bottom:-10px;opacity:0;pointer-events:none;border:0';
    // pede ao YouTube para mandar o tempo atual (para continuar na próxima página)
    fr.addEventListener('load', () => { let n = 0; const t = setInterval(() => { try { fr.contentWindow.postMessage(JSON.stringify({ event: 'listening', id: 1 }), 'https://www.youtube-nocookie.com'); } catch (e) {} if (++n > 10) clearInterval(t); }, 500); aplicar(); });
    document.body.appendChild(fr);
  }
  const cmd = (func, args = []) => { if (!fr) return; try { fr.contentWindow.postMessage(JSON.stringify({ event: 'command', func, args }), 'https://www.youtube-nocookie.com'); } catch (e) {} };
  const depois = () => setTimeout(() => (window.requestIdleCallback || setTimeout)(criarPlayer), 4000);
  if (document.readyState === 'complete') depois(); else addEventListener('load', depois);
  addEventListener('message', e => {
    if (e.origin !== 'https://www.youtube-nocookie.com' && e.origin !== 'https://www.youtube.com') return;   // só o player do YouTube
    try { const d = JSON.parse(e.data); if (d.info && typeof d.info.currentTime === 'number') { tempo = d.info.currentTime; } } catch (er) {}
  });
  setInterval(() => guarda.set('turzin-som-t', Math.floor(tempo)), 2000);
  addEventListener('pagehide', () => guarda.set('turzin-som-t', Math.floor(tempo)));

  // botão de som
  const css = document.createElement('style');
  css.textContent = `
  .som{position:fixed;right:20px;bottom:20px;z-index:70;display:inline-flex;align-items:center;gap:10px;padding:10px 14px;border:1.5px solid rgba(247,247,247,.35);background:rgba(33,33,33,.82);color:#F7F7F7;
       font:700 12px/1 'Bricolage Grotesque',system-ui,sans-serif;letter-spacing:.08em;text-transform:uppercase;cursor:pointer;backdrop-filter:blur(6px)}
  .som:hover{border-color:#44D62D}
  .som:focus-visible{outline:2px solid #44D62D;outline-offset:3px}
  .som .eq{display:inline-flex;align-items:flex-end;gap:2px;height:12px}
  .som .eq i{width:3px;height:3px;background:#44D62D}
  .som.on .eq i{animation:somEq .9s steps(4) infinite}
  .som.on .eq i:nth-child(2){animation-delay:.2s}.som.on .eq i:nth-child(3){animation-delay:.45s}.som.on .eq i:nth-child(4){animation-delay:.1s}
  @keyframes somEq{0%{height:3px}50%{height:12px}100%{height:5px}}`;
  document.head.appendChild(css);
  const b = document.createElement('button');
  b.type = 'button'; b.className = 'som';
  b.innerHTML = '<span class="eq" aria-hidden="true"><i></i><i></i><i></i><i></i></span><span class="tx"></span>';
  document.body.appendChild(b);
  const tx = b.querySelector('.tx');

  function aplicar() {
    const tocando = querSom && liberado;
    if (tocando) { cmd('unMute'); cmd('setVolume', [VOLUME]); cmd('playVideo'); } else cmd('mute');
    b.classList.toggle('on', tocando);
    tx.textContent = !querSom ? 'Som desligado' : liberado ? 'Som ligado' : 'Ativar som';
    b.setAttribute('aria-pressed', tocando);
    b.setAttribute('aria-label', tocando ? 'Desligar a música' : 'Ligar a música');
  }
  b.addEventListener('click', e => {
    e.stopPropagation();
    if (!liberado) { liberado = true; querSom = true; } else querSom = !querSom;
    criarPlayer();
    guarda.set('turzin-som', querSom ? 'on' : 'off'); aplicar();
  });
  // primeiro clique ou tecla em qualquer lugar libera o som (se a pessoa não desligou)
  const libera = e => { if (liberado || (e && b.contains(e.target))) return; liberado = true; criarPlayer(); aplicar(); removeEventListener('pointerdown', libera, true); removeEventListener('keydown', libera, true); };
  addEventListener('pointerdown', libera, true); addEventListener('keydown', libera, true);
  aplicar();
})();
