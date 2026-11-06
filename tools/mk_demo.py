"""Rebrandea el sistema de SebaChavez Car Service como demo genérica.
Uso: python3 tools/mk_demo.py <index.html de Sebachavezcarervice> index.html
"""
import re,base64,sys
src,dst=sys.argv[1],sys.argv[2]
s=open(src,encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    c=s.count(a)
    assert c==n,(c,a[:90])
    s=s.replace(a,b)
svg='''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 360">
<circle cx="180" cy="150" r="112" fill="none" stroke="#e53935" stroke-width="16" stroke-dasharray="360 344" transform="rotate(-200 180 150)"/>
<circle cx="180" cy="150" r="112" fill="none" stroke="#1e6fd0" stroke-width="16" stroke-dasharray="330 374" transform="rotate(-10 180 150)"/>
<g fill="#3a3d43">
<path d="M112 168 l16-44 q4-10 16-10 h72 q12 0 16 10 l16 44 q14 2 14 16 v28 h-14 a20 20 0 0 1-40 0 h-56 a20 20 0 0 1-40 0 h-14 v-28 q0-14 14-16z M134 166 h92 l-11-34 q-2-5-8-5 h-54 q-6 0-8 5z"/>
<circle cx="140" cy="212" r="11" fill="#fff"/><circle cx="220" cy="212" r="11" fill="#fff"/>
</g>
<path d="M248 64 a26 26 0 0 0-34 32 l-28 28 12 12 28-28 a26 26 0 0 0 32-34 l-14 14-12-4-4-12z" fill="#1e6fd0"/>
<text x="180" y="304" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-weight="800" font-size="40" fill="#e53935">TU TALLER</text>
<text x="180" y="342" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-weight="700" font-size="21" fill="#3a3d43" letter-spacing="1">CAR CENTER · SISTEMA VB</text>
</svg>'''
uri='data:image/svg+xml;base64,'+base64.b64encode(svg.encode()).decode()
s,n=re.subn(r'const LOGO="data:image/jpeg;base64,[^"]+";','const LOGO="'+uri+'";',s);assert n==1
pass
rep('<title>SebaChavez Car Service · Sistema VB</title>','<title>Tu Taller Car Center · Sistema VB (demo)</title>')
rep('<b>SebaChavez Car Service</b></div>','<b>Tu Taller Car Center</b></div>')
rep("cfg:{nombre:'SebaChavez Car Service',dir:'Jujuy 251 - Salta',tel:'3875971922',mail:'schavezcarservice@gmail.com',fb:'sebachavezcarservice',ig:'sebachavez_carservice',",
    "cfg:{nombre:'Tu Taller Car Center',dir:'Av. Ejemplo 123 - Salta',tel:'3870000000',mail:'contacto@tutaller.example',fb:'tutaller',ig:'tutaller',")
rep("{id:'u1',n:'Seba Chavez',rol:'dueno'","{id:'u1',n:'Martín Gómez',rol:'dueno'")
s=s.replace("u:'Seba Chavez'","u:'Martín Gómez'").replace("por:'Seba Chavez'","por:'Martín Gómez'")
rep('<input id="su_n" value="Seba Chavez"','<input id="su_n" value=""')
rep('alt="Logo SebaChavez Car Service"','alt="Logo del taller"')
rep('alt="SebaChavez Car Service"','alt="Logo del taller"')
rep("const VBMSG='Hola, vi el sistema de '+'SebaChavez Car Service (Sistema VB) y quiero más información.';","const VBMSG='Hola, vi la demo del Sistema VB para talleres y car centers (mecánica, audio y alarmas) y quiero más información.';")
rep("encodeURIComponent('Sistema VB · SebaChavez Car Service')","encodeURIComponent('Sistema VB · Demo taller y car center')")
# modo: la demo abre con datos de ejemplo; #real = sistema vacío
rep("const MODO=/practica/i.test(location.hash)?'practica':'real';","const MODO=/real/i.test(location.hash)?'real':'practica';")
rep("const LS=MODO==='practica'?'sbcs_vb26_practica_v2':'sbcs_vb26_real_v1', SS='sbcs_vb26_user_'+MODO;","const LS=MODO==='practica'?'tmvb_demo_practica_v1':'tmvb_demo_real_v1', SS='tmvb_demo_user_'+MODO;")
rep("ACT.modopractica=()=>{location.hash='#practica'};","ACT.modopractica=()=>{history.replaceState(null,'',location.pathname+location.search);location.reload()};")
rep("ACT.modoreal=()=>{history.replaceState(null,'',location.pathname+location.search);location.reload()};","ACT.modoreal=()=>{location.hash='#real'};")
s=s.replace('href="#practica" data-act="modopractica"','href="#" data-act="modopractica"')
rep("""<b>MODO PRÁCTICA.</b> Datos de ejemplo, guardados aparte; no tocan los datos reales del taller. Sin clave: elegí un perfil para ver los permisos de cada rol. <a href="#" data-act="modoreal">Ir al sistema real</a>""",
    """<b>DEMO.</b> Sistema de gestión para talleres y car centers (mecánica, car audio, alarmas y accesorios) con datos de ejemplo. Elegí un perfil (sin clave) para ver qué puede hacer cada rol. Los cambios quedan sólo en este navegador. <a href="#" data-act="modoreal">Probar el sistema vacío (con claves)</a>""")
rep("""pb.innerHTML='MODO PRÁCTICA · datos de ejemplo, no son los del taller · <a href="#" data-act="modoreal">Ir al sistema real</a>'""",
    """pb.innerHTML='DEMO · datos de ejemplo · <a href="#" data-act="modoreal">Probar el sistema vacío</a>'""")
left=[m for m in re.findall(r'.{30}(?:Seba|Chavez|Jujuy 251|5971922|schavez|sebachavez).{30}',s,re.I)]
print('restos:',left)
open(dst,'w',encoding='utf-8').write(s)
s=open(dst,encoding='utf-8').read()
s=s.replace('<a href="#" data-act="modopractica">Entrá al modo práctica</a> con datos de ejemplo.','<a href="#" data-act="modopractica">Volvé a la demo</a> con datos de ejemplo.')
s=s.replace('data-act="modopractica">Modo práctica</a>','data-act="modopractica">Volver a la demo</a>')
s=s.replace("'Restablecer datos de práctica'","'Restablecer datos de ejemplo'")
open(dst,'w',encoding='utf-8').write(s)
