from playwright.sync_api import sync_playwright
import pathlib,sys
from PIL import Image
ids=['q1','q2','q3','q4','qp','q5','k1','k2','k3','k4','kp','k5','d1','d2','d3','d4','dp','d5']
with sync_playwright() as pw:
    b=pw.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
    pg=b.new_page(viewport={'width':1080,'height':1920})
    pg.goto(pathlib.Path('semana.html').resolve().as_uri()); pg.wait_for_timeout(1500)
    for i in ids:
        pg.locator('#'+i).screenshot(path=f'{i}.png')
        Image.open(f'{i}.png').convert('RGB').save(f'{i}.jpg',quality=90)
    b.close()
for day in ['q','k','d']:
    d=[i for i in ids if i[0]==day]
    o=Image.new('RGB',(5*324+6*10+400,600),'#555'); x=10
    for i in d:
        im=Image.open(f'{i}.png')
        im=im.resize((324,576)) if im.size[1]==1920 else im.resize((380,475))
        o.paste(im,(x,12)); x+=im.size[0]+10
    o.save(f'prev_{day}.jpg',quality=88)
