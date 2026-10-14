# Monta o index.html final colando os SVGs da marca (img/marca/*.svg) no lugar de {{SVG:arquivo:classes}}
import re
src=open('/home/claude/site_v5/src/index.src.html').read()
def svg(m):
    nome,cls=m.group(1),m.group(2)
    s=open(f'/home/claude/site_v5/img/marca/{nome}.svg').read()
    s=s.replace(' xmlns="http://www.w3.org/2000/svg"','')
    return s.replace('<svg ',f'<svg class="{cls}" aria-hidden="true" focusable="false" ',1)
out=re.sub(r'\{\{SVG:([\w-]+):([^}]*)\}\}',svg,src)
open('/home/claude/site_v5/index.html','w').write(out); print(len(out))
