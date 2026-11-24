import re,pathlib
F='/home/claude/marca/inter_pkg/files/'
I='/home/claude/marca/inter_pkg/icons/'
logo='<img src="../marca/logo.png" style="width:100%;display:block">'
def ic(n,size=40,color='#fff',sw=2):
    s=open(I+n+'.svg').read(); s=re.sub(r'<!--.*?-->','',s,flags=re.S)
    return s.replace('stroke="currentColor"',f'stroke="{color}"').replace('stroke-width="2"',f'stroke-width="{sw}"').replace('width="24"',f'width="{size}"').replace('height="24"',f'height="{size}"')
css=f'''
@font-face{{font-family:Inter;font-weight:400;src:url({F}inter-latin-400-normal.woff2)}}
@font-face{{font-family:Inter;font-weight:500;src:url({F}inter-latin-500-normal.woff2)}}
@font-face{{font-family:Inter;font-weight:700;src:url({F}inter-latin-700-normal.woff2)}}
@font-face{{font-family:Inter;font-weight:800;src:url({F}inter-latin-800-normal.woff2)}}
@font-face{{font-family:Inter;font-weight:800;font-style:italic;src:url({F}inter-latin-800-italic.woff2)}}
@font-face{{font-family:Inter;font-weight:900;font-style:italic;src:url({F}inter-latin-900-italic.woff2)}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{background:#333}}
.a{{position:relative;overflow:hidden;font-family:Inter;color:#fff;background:#0F172A;margin-bottom:30px}}
.st{{width:1080px;height:1920px}} .po{{width:1080px;height:1350px}}
.glow{{position:absolute;inset:0;background:radial-gradient(900px 700px at 100% 0%,rgba(37,99,235,.38),transparent 60%),radial-gradient(800px 600px at 0% 100%,rgba(37,99,235,.22),transparent 60%)}}
.stripe{{position:absolute;width:1400px;height:18px;background:linear-gradient(90deg,transparent,#2563EB 40%,#1A7CF2 60%,transparent);transform:rotate(-38deg);opacity:.85}}
.stripe.t{{height:6px;opacity:.6}}
.pill{{position:absolute;display:flex;align-items:center;gap:16px;background:#2563EB;border-radius:999px;padding:14px 34px 14px 22px;font-weight:800;font-style:italic;font-size:30px;letter-spacing:.02em;text-transform:uppercase;box-shadow:0 10px 30px rgba(37,99,235,.35)}}
.h{{position:absolute;left:80px;right:80px;font-weight:900;font-style:italic;line-height:1.02;letter-spacing:-.01em}}
.h b{{color:#3B8BFF}}
.p{{position:absolute;left:80px;right:80px;font-weight:500;font-size:40px;line-height:1.35;color:#CBD5E1}}
.ph{{position:absolute;border-radius:28px;background-size:cover;background-position:center;border:3px solid rgba(37,99,235,.55);box-shadow:0 24px 60px rgba(0,0,0,.45)}}
.tag{{position:absolute;background:rgba(15,23,42,.82);border:2px solid #2563EB;border-radius:999px;padding:10px 26px;font-weight:800;font-style:italic;font-size:30px;text-transform:uppercase}}
.cta{{position:absolute;display:flex;align-items:center;gap:16px;background:#2563EB;border-radius:999px;padding:20px 40px;font-weight:700;font-size:34px}}
.wm{{position:absolute;width:270px;left:405px}}
.wm svg{{width:250px;height:auto;display:block}}
.opt{{position:absolute;left:120px;right:120px;height:120px;border-radius:24px;border:3px solid rgba(255,255,255,.18);background:rgba(255,255,255,.04);display:flex;align-items:center;padding:0 40px;font-weight:700;font-size:44px}}
'''
def base(cls): return f'<div class="glow"></div><div class="stripe" style="left:-500px;top:1700px"></div><div class="stripe t" style="left:-420px;top:1760px"></div><div class="stripe t" style="left:320px;top:120px;opacity:.35"></div>'
def wm(y): return f'<div class="wm" style="top:{y}px">{logo}</div>'
S={}
# 1 salario x coracao
S['s1']=f'''<section class="a st" id="s1">{base('st')}
<div class="pill" style="left:80px;top:260px">{ic('laugh',40)} Auto Brasil sem filtro</div>
<div class="h" style="top:370px;font-size:72px;right:40px">Seu salário escolhe um.<br><b>Seu coração</b> escolhe outro.</div>
<div class="ph" style="left:130px;top:630px;width:820px;height:486px;background-image:url(celta.jpg)"></div><div class="tag" style="left:160px;top:660px">Salário</div>
<div class="ph" style="left:130px;top:1140px;width:820px;height:486px;background-image:url(tcrossb.jpg)"></div><div class="tag" style="left:160px;top:1170px">Coração</div>
{wm(1650)}</section>'''
# 2 quiz gol
S['s2']=f'''<section class="a st" id="s2">{base('st')}
<div class="pill" style="left:80px;top:260px">{ic('lightbulb',40)} Curiosidade automotiva</div>
<div class="h" style="top:380px;font-size:96px">Por quantos anos seguidos o Gol foi o <b>mais vendido</b> do Brasil?</div>
<div class="ph" style="left:130px;top:850px;width:820px;height:486px;background-image:url(gol20.jpg)"></div>
<div class="p" style="top:1380px;text-align:center">Chuta aí. A resposta vem no próximo story.</div>
{wm(1650)}</section>'''
# 3 resposta gol
S['s3']=f'''<section class="a st" id="s3">{base('st')}
<div class="pill" style="left:80px;top:260px">{ic('trophy',40)} Resposta</div>
<div class="h" style="top:380px;font-size:200px;line-height:1">27 <span style="font-size:90px">anos</span></div>
<div class="h" style="top:600px;font-size:64px">seguidos no topo, de <b>1987 a 2013</b>. Recorde no Brasil.</div>
<div class="ph" style="left:80px;top:860px;width:450px;height:267px;background-image:url(gol12.jpg)"></div>
<div class="ph" style="left:550px;top:860px;width:450px;height:267px;background-image:url(gol20.jpg)"></div>
<div class="p" style="top:1170px">E o campeão continua aqui na loja: temos <b style="color:#fff">Gol 2012</b> e <b style="color:#fff">Gol 2020</b> esperando dono.</div>
<div class="cta" style="left:80px;top:1400px">{ic('message-circle',40)} Responde "quero ver"</div>
{wm(1650)}</section>'''
# 4 teaser renegade
S['s4']=f'''<section class="a st" id="s4">{base('st')}
<div class="pill" style="left:80px;top:260px">{ic('car-front',40)} Chegou na loja!</div>
<div class="h" style="top:380px;font-size:84px">Acabou de chegar um <b>SUV</b> que ainda nem tem foto no site.</div>
<div class="p" style="top:800px">Uma dica: a grade dele tem <b style="color:#fff">7 fendas</b>.</div>
<div class="h" style="top:900px;font-size:72px">Qual é?</div>
<div class="opt" style="top:1030px">A &nbsp;·&nbsp; Jeep Renegade</div>
<div class="opt" style="top:1170px">B &nbsp;·&nbsp; Nissan Kicks</div>
<div class="opt" style="top:1310px">C &nbsp;·&nbsp; Honda HR-V</div>
<div class="p" style="top:1470px;text-align:center;font-size:34px">Responde com a letra. Quem vem na loja vê antes de todo mundo.</div>
{wm(1650)}</section>'''
# 5 primeiro carro
S['s5']=f'''<section class="a st" id="s5">{base('st')}
<div class="pill" style="left:80px;top:260px">{ic('route',40)} Papo de estrada</div>
<div class="h" style="top:380px;font-size:100px">Qual foi o <b>primeiro carro</b> da sua vida?</div>
<div class="ph" style="left:130px;top:740px;width:820px;height:486px;background-image:url(golf.jpg)"></div>
<div class="p" style="top:1270px">Aquele que a gente nunca esquece. Conta pra gente aqui.</div>
{wm(1650)}</section>'''
# post feed
P=f'''<section class="a po" id="p1">{base('po')}
<div class="pill" style="left:70px;top:70px">{ic('laugh',40)} Auto Brasil sem filtro</div>
<div class="h" style="left:70px;top:170px;font-size:64px;right:40px">Seu salário escolhe um.<br><b>Seu coração</b> escolhe outro.</div>
<div class="ph" style="left:70px;top:420px;width:460px;height:273px;background-image:url(celta.jpg)"></div><div class="tag" style="left:90px;top:440px;font-size:24px">Salário</div>
<div class="ph" style="left:550px;top:420px;width:460px;height:273px;background-image:url(tcrossb.jpg)"></div><div class="tag" style="left:570px;top:440px;font-size:24px">Coração</div>
<div class="h" style="left:70px;top:760px;font-size:54px">E na sua casa, <b>quem ganha?</b></div>
<div class="p" style="left:70px;top:850px;font-size:34px">Aqui tem opção para os dois. E a gente ainda aceita seu usado na troca.</div>
<div class="cta" style="left:70px;top:1010px;font-size:30px;padding:18px 36px">{ic('message-circle',36)} Comenta: salário ou coração?</div>
<div class="wm" style="top:1170px;left:780px;width:230px">{logo}</div>
</section>'''
html=f'<!DOCTYPE html><html><head><meta charset="utf-8"><style>{css}</style></head><body>'+''.join(S.values())+P+'</body></html>'
open('terca.html','w').write(html)
