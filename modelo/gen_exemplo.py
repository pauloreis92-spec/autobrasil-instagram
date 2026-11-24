import re,sys
sys.path.insert(0,'/home/claude/terca')
F='/home/claude/marca/inter_pkg/files/'; I='/home/claude/marca/inter_pkg/icons/'
logo='<img src="../marca/logo.png" style="width:100%;display:block">'
def ic(n,size=40,color='#fff',sw=2):
    s=open(I+n+'.svg').read(); s=re.sub(r'<!--.*?-->','',s,flags=re.S)
    return s.replace('stroke="currentColor"',f'stroke="{color}"').replace('stroke-width="2"',f'stroke-width="{sw}"').replace('width="24"',f'width="{size}"').replace('height="24"',f'height="{size}"')
css=open('/home/claude/terca/gen.py').read().split("css=f'''")[1].split("'''")[0]
css=css.replace('{{','{').replace('}}','}').replace('{F}',F)
css+='''
.big{position:absolute;left:0;right:0;display:flex;justify-content:center}
.circ{width:300px;height:300px;border-radius:50%;background:radial-gradient(circle at 30% 30%,#3B8BFF,#2563EB 60%,#1E3A8A);display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 18px rgba(37,99,235,.15),0 30px 80px rgba(37,99,235,.45)}
.card{position:absolute;left:80px;right:80px;border-radius:28px;background:rgba(255,255,255,.05);border:2px solid rgba(59,139,255,.35);padding:34px 40px;display:flex;gap:30px;align-items:center}
.card .t{font-weight:800;font-size:40px;line-height:1.15}.card .d{font-weight:500;font-size:32px;color:#CBD5E1;margin-top:6px;line-height:1.3}
.num{position:absolute;white-space:nowrap;flex:none;font-weight:900;font-style:italic;color:#3B8BFF;line-height:1}
.vs{position:absolute;width:130px;height:130px;border-radius:50%;background:#0F172A;border:5px solid #2563EB;display:flex;align-items:center;justify-content:center;font-weight:900;font-style:italic;font-size:54px;z-index:3}
.lt{position:absolute;width:92px;height:92px;border-radius:50%;background:#2563EB;display:flex;align-items:center;justify-content:center;font-weight:900;font-size:50px;z-index:3;box-shadow:0 10px 30px rgba(0,0,0,.4)}
'''
def base(): return '<div class="glow"></div><div class="stripe" style="left:-500px;top:1700px"></div><div class="stripe t" style="left:-420px;top:1760px"></div><div class="stripe t" style="left:320px;top:120px;opacity:.35"></div>'
def basep(): return '<div class="glow"></div><div class="stripe" style="left:-560px;top:1230px"></div><div class="stripe t" style="left:320px;top:60px;opacity:.35"></div>'
def wm(y=1650): return f'<div class="wm" style="top:{y}px">{logo}</div>'
def wmp(): return f'<div class="wm" style="top:1180px;left:810px;width:200px">{logo}</div>'
S={}
def st(i,body): S[i]=f'<section class="a st" id="{i}">{base()}{body}{wm()}</section>'
def po(i,body): S[i]=f'<section class="a po" id="{i}">{basep()}{body}{wmp()}</section>'
def pill(icn,txt,x=80,y=260,fs=None): return f'<div class="pill" style="left:{x}px;top:{y}px{";font-size:%dpx"%fs if fs else ""}">{ic(icn,40)} {txt}</div>'
def duel(i,icn,sel,title,a,an,b,bn,foot,tf=84):
    st(i,f'''{pill(icn,sel)}<div class="h" style="top:370px;font-size:{tf}px">{title}</div>
<div class="ph" style="left:130px;top:640px;width:820px;height:470px;background-image:url({a})"></div><div class="lt" style="left:100px;top:610px">A</div><div class="tag" style="left:620px;top:1040px">{an}</div>
<div class="vs" style="left:475px;top:1080px">X</div>
<div class="ph" style="left:130px;top:1150px;width:820px;height:470px;background-image:url({b})"></div><div class="lt" style="left:100px;top:1120px">B</div><div class="tag" style="left:620px;top:1550px">{bn}</div>
''')
    # footer placed under title instead (safe area)
    S[i]=S[i].replace(f'<div class="ph" style="left:130px;top:640px',f'<div class="p" style="top:{370+ (2 if tf<90 else 2)*tf+30}px;font-size:36px">{foot}</div><div class="ph" style="left:130px;top:640px',1)
# ===== QUARTA: duelo
duel('q1','swords','Duelo de máquinas','Polo ou Gol: <b>qual vai</b> pra sua garagem?','polo.jpg','Polo 2020','gol20.jpg','Gol 2020','Mesma família VW. Responde A ou B.',tf=76)
duel('q2','swords','Duelo de máquinas','Strada 2012 ou 2017: <b>qual geração</b> você prefere?','strada12.jpg','Strada 2012','strada17.jpg','Strada 2017','Duas Adventure. Responde A ou B.',tf=72)
duel('q3','swords','Duelo de máquinas','Prisma ou Classic: <b>qual é o sedã</b> do seu coração?','prisma.jpg','Prisma','classic.jpg','Classic','Responde A ou B. Vale defender o seu.',tf=72)
st('q4',f'''{pill('swords','Duelo relâmpago')}
<div class="h" style="top:380px;font-size:110px">Câmbio <b>manual</b> ou <b>automático</b>?</div>
<div class="card" style="top:760px;height:200px"><div class="lt" style="position:static;flex:none">A</div><div><div class="t">Manual</div><div class="d">Quem gosta de trocar marcha e sentir o carro</div></div></div>
<div class="card" style="top:1000px;height:200px"><div class="lt" style="position:static;flex:none">B</div><div><div class="t">Automático</div><div class="d">Quem quer conforto no trânsito e na serra</div></div></div>
<div class="p" style="top:1270px;text-align:center">Responde A ou B. Sem briga, cada um tem seu motivo.</div>''')
po('qp',f'''{pill('swords','Duelo de máquinas',70,60)}
<div class="h" style="left:70px;top:160px;font-size:66px">O clássico ou <b>o moderno?</b></div>
<div class="ph" style="left:70px;top:330px;width:460px;height:400px;background-image:url(golf.jpg)"></div><div class="tag" style="left:90px;top:660px;font-size:26px">Golf 2003</div>
<div class="vs" style="left:475px;top:470px;width:110px;height:110px;font-size:44px">X</div>
<div class="ph" style="left:550px;top:330px;width:460px;height:400px;background-image:url(tcrossb.jpg)"></div><div class="tag" style="left:570px;top:660px;font-size:26px">T-Cross 2022</div>
<div class="p" style="left:70px;top:790px;font-size:36px">Dezenove anos separam esses dois VW. Um marcou época, o outro é o SUV do momento. Os dois estão aqui na loja.</div>
<div class="cta" style="left:70px;top:1010px;font-size:30px;padding:18px 36px">{ic('message-circle',36)} Comenta: Golf ou T-Cross?</div>''')
st('q5',f'''{pill('vote','Votação aberta')}
<div class="h" style="top:380px;font-size:96px">Hoje no feed: <b>Golf ou T-Cross?</b></div>
<div class="ph" style="left:80px;top:720px;width:450px;height:330px;background-image:url(golf.jpg)"></div>
<div class="ph" style="left:550px;top:720px;width:450px;height:330px;background-image:url(tcrossb.jpg)"></div>
<div class="p" style="top:1110px">O clássico ou o moderno. Corre lá no post e deixa seu voto nos comentários.</div>
<div class="cta" style="left:80px;top:1340px">{ic('message-circle',40)} Vota no post de hoje</div>''')
# ===== QUINTA: voce sabia
def tip(i,icn,sel,title,txt,tf=96,extra=''):
    st(i,f'''{pill(icn,sel)}<div class="h" style="top:380px;font-size:{tf}px">{title}</div>
<div class="big" style="top:850px"><div class="circ">{ic(icn,150,'#fff',1.6)}</div></div>
<div class="p" style="top:1220px;text-align:center">{txt}</div>{extra}''')
tip('k1','gauge','Você sabia?','Pneu calibrado <b>economiza</b> combustível.','Pneu murcho aumenta o atrito com o asfalto e o carro gasta mais. Vale conferir a pressão a cada 15 dias.')
st('k2',f'''{pill('lightbulb','Quiz rápido')}
<div class="h" style="top:380px;font-size:92px">Qual o jeito <b>certo</b> de calibrar o pneu?</div>
<div class="card" style="top:800px;height:190px"><div class="lt" style="position:static;flex:none">A</div><div class="t">Com o pneu frio, antes de rodar</div></div>
<div class="card" style="top:1030px;height:190px"><div class="lt" style="position:static;flex:none">B</div><div class="t">Depois de rodar bastante, com ele quente</div></div>
<div class="p" style="top:1290px;text-align:center">Responde A ou B. A resposta vem no próximo story.</div>''')
st('k3',f'''{pill('trophy','Resposta')}
<div class="h" style="top:380px;font-size:150px;line-height:1">Letra <b>A</b></div>
<div class="h" style="top:570px;font-size:66px">Com o pneu frio.</div>
<div class="big" style="top:740px"><div class="circ" style="width:240px;height:240px">{ic('thermometer',120,'#fff',1.6)}</div></div>
<div class="p" style="top:1060px">Rodando, o ar dentro do pneu esquenta e a pressão sobe. Aí a leitura engana e você acaba deixando o pneu mais vazio do que devia.</div>
<div class="p" style="top:1330px;color:#fff;font-weight:700">E não esquece do estepe.</div>''')
tip('k4','cloud-fog','Dica da serra','Neblina na estrada? <b>Farol baixo.</b>','O farol alto reflete nas gotículas da neblina e atrapalha a sua visão. Farol baixo, distância maior e velocidade menor.',tf=92)
items=[('disc','Pneus e estepe','Calibrados e em bom estado'),('droplet','Óleo e água','Nível do óleo e do radiador'),('cloud','Palhetas','E água no reservatório do limpador'),('sun','Faróis e lanternas','Tudo acendendo, inclusive o freio'),('shield-check','Documento e kit','Triângulo, macaco e chave de roda')]
rows=''.join(f'<div class="card" style="left:70px;right:70px;top:{300+k*150}px;height:130px;padding:20px 30px;gap:24px"><div class="lt" style="position:static;flex:none;width:80px;height:80px">{ic(n,40)}</div><div><div class="t" style="font-size:34px">{t}</div><div class="d" style="font-size:26px;margin-top:2px">{d}</div></div></div>' for k,(n,t,d) in enumerate(items))
po('kp',f'''{pill('list-checks','Você sabia?',70,60)}
<div class="h" style="left:70px;top:150px;font-size:58px">Vai pegar a estrada? <b>5 checagens</b></div>
{rows}<div class="cta" style="left:70px;top:1080px;font-size:30px;padding:18px 36px">{ic('bookmark',36)} Salva e manda pra quem vai viajar</div>''')
st('k5',f'''{pill('map-pin','Papo de fim de ano')}
<div class="h" style="top:380px;font-size:100px">Pra onde você vai nas <b>festas?</b></div>
<div class="card" style="top:780px;height:150px">{ic('mountain',60)}<div class="t">Serra</div></div>
<div class="card" style="top:960px;height:150px">{ic('waves',60)}<div class="t">Praia</div></div>
<div class="card" style="top:1140px;height:150px">{ic('heart',60)}<div class="t">Em casa com a família</div></div>
<div class="p" style="top:1360px;text-align:center">Responde aqui. A gente quer saber.</div>''')
# ===== DOMINGO: estrada
st('d1',f'''{pill('route','Paixão por estrada')}
<div class="h" style="top:380px;font-size:110px">Domingo pede <b>estrada.</b></div>
<div class="h" style="top:640px;font-size:70px">Hoje você iria pra onde?</div>
<div class="card" style="top:820px;height:220px"><div class="circ" style="width:150px;height:150px;flex:none">{ic('mountain',80)}</div><div><div class="t">Serra</div><div class="d">Mirante, café colonial e frio na medida</div></div></div>
<div class="card" style="top:1080px;height:220px"><div class="circ" style="width:150px;height:150px;flex:none">{ic('waves',80)}</div><div><div class="t">Praia</div><div class="d">Pé na areia e vidro aberto</div></div></div>
<div class="p" style="top:1370px;text-align:center">Responde: serra ou praia?</div>''')
st('d2',f'''{pill('history','Nostalgia')}
<div class="h" style="top:380px;font-size:92px">Quem é da época em que o <b>Golf</b> era sonho?</div>
<div class="ph" style="left:130px;top:760px;width:820px;height:486px;background-image:url(golf.jpg)"></div>
<div class="p" style="top:1290px">Fabricado no Brasil, virou objeto de desejo no começo dos anos 2000. Conta aí: você teve ou queria ter um?</div>''')
tip('d3','music','Trilha da estrada','Qual música <b>não pode faltar</b> na viagem?','Manda o nome aqui. Vale tudo, do sertanejo ao rock.',tf=96)
tip('d4','star','Carro dos sonhos','Se pudesse ter <b>qualquer carro</b>, qual seria?','Sem limite de orçamento. Responde aqui com o seu.',tf=96)
po('dp',f'''{pill('route','Papo de estrada',70,60)}
<div class="h" style="left:70px;top:160px;font-size:72px">Serra do <b>Rio do Rastro</b></div>
<div class="p" style="left:70px;top:260px;font-size:34px">A estrada mais famosa de SC fica pertinho da gente.</div>
<div class="card" style="left:70px;right:70px;top:370px;height:190px"><div class="num" style="position:static;font-size:110px">284</div><div class="t">curvas na SC-390</div></div>
<div class="card" style="left:70px;right:70px;top:590px;height:190px"><div class="num" style="position:static;font-size:96px">+1.400 m</div><div class="t">de altitude no mirante</div></div>
<div class="card" style="left:70px;right:70px;top:810px;height:190px"><div class="num" style="position:static;font-size:96px">+100 km</div><div class="t">de vista: em dia limpo, dá pra ver o mar</div></div>
<div class="cta" style="left:70px;top:1060px;font-size:30px;padding:18px 36px">{ic('message-circle',36)} Já subiu? Qual carro te levou?</div>''')
st('d5',f'''{pill('navigation','Fim de domingo')}
<div class="h" style="top:380px;font-size:100px">Qual foi o <b>melhor passeio</b> de carro da sua vida?</div>
<div class="big" style="top:930px"><div class="circ">{ic('car-front',150,'#fff',1.6)}</div></div>
<div class="p" style="top:1300px;text-align:center">Pra onde, com quem e em qual carro. Conta pra gente.</div>''')
html=f'<!DOCTYPE html><html><head><meta charset="utf-8"><style>{css}</style></head><body>'+''.join(S.values())+'</body></html>'
open('semana.html','w').write(html); print(list(S))
