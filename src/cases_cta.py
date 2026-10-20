"""Coloca nos estudos de caso um botão fixo de WhatsApp e, para quem veio da landing page,
um botão para voltar a ela. Rode depois de gerar os cases: python src/cases_cta.py
É seguro rodar várias vezes: o bloco entre <!-- lp-cta --> e <!-- /lp-cta --> é trocado inteiro."""
import os, re
from urllib.parse import quote
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/'
CASES = {'isabella': 'Isabella Gutierres', 'margarett': 'Margarett', 'acai-yo': 'Açaí Yo', 'reigotta': 'Reigotta', 'kamisama': 'Kamisama'}
for slug, nome in CASES.items():
    msg = quote(f'Olá, turzin. Vi o projeto {nome} e quero uma marca assim para o meu negócio.')
    bloco = f'''<!-- lp-cta -->
<style>
.lpc{{position:fixed;z-index:45;left:20px;bottom:20px;display:flex;gap:8px;transform:translateY(160%);transition:transform .45s cubic-bezier(.2,.8,.2,1)}}
.lpc.on{{transform:none}}
.lpc a{{display:inline-flex;align-items:center;gap:8px;padding:14px 20px;font:700 14px 'Bricolage Grotesque',system-ui,sans-serif;letter-spacing:.06em;text-transform:uppercase;text-decoration:none;border:1.5px solid #44D62D;box-shadow:0 10px 26px rgba(0,0,0,.3)}}
.lpc .zap{{background:#44D62D;color:#212121}}
.lpc .zap:hover{{background:#F7F7F7;border-color:#F7F7F7}}
.lpc .volta{{background:#212121;color:#F7F7F7;border-color:rgba(247,247,247,.3)}}
.lpc .volta:hover{{border-color:#F7F7F7}}
.lpc .volta[hidden]{{display:none}}
@media (max-width:760px){{.lpc{{left:12px;right:12px;bottom:calc(12px + env(safe-area-inset-bottom,0px))}}.lpc a{{flex:1;justify-content:center;padding:14px 12px;font-size:13px}}.lpc .volta{{flex:0 0 auto}}}}
@media (prefers-reduced-motion:reduce){{.lpc{{transition:none}}}}
</style>
<nav class="lpc" id="lpc" aria-label="Contato">
  <a class="volta" id="lpc-v" href="/identidade-visual#marcas" hidden>← Voltar</a>
  <a class="zap" href="https://wa.me/5534999599575?text={msg}" target="_blank" rel="noopener">Quero uma marca assim →</a>
</nav>
<script>
(function () {{
  var veio = /[?&]de=lp\\b/.test(location.search) || /identidade-visual/.test(document.referrer);
  try {{ veio = veio || sessionStorage.getItem('veio-lp') === '1'; }} catch (e) {{}}
  if (veio) {{ document.getElementById('lpc-v').hidden = false; var t = document.querySelector('.top .back'); if (t) t.href = '/identidade-visual#marcas'; }}
  var b = document.getElementById('lpc');
  function f() {{ b.classList.toggle('on', scrollY > 300); }}
  addEventListener('scroll', f, {{ passive: true }}); f();
}})();
</script>
<!-- /lp-cta -->'''
    p = R + slug + '.html'; s = open(p).read()
    s = re.sub(r'\n?<!-- lp-cta -->.*?<!-- /lp-cta -->', '', s, flags=re.S)
    s = s.replace('</body>', bloco + '\n</body>', 1)
    open(p, 'w').write(s); print('cta ok', slug)
