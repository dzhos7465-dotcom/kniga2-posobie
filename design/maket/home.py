import asyncio,base64
exec(open("kit.py").read().split("html=f'''")[0])
css=open('kit.py').read().split("<style>{CSS}")[1].split("</style>")[0].replace("{{","{").replace("}}","}")
J=lambda p:'data:image/jpeg;base64,'+base64.b64encode(open('/home/claude/kniga2-posobie/lessons/'+p,'rb').read()).decode()
L=[('١','تَعَارُفٌ «١»','Знакомство','1–10','#2f8fd0',None,'soon'),('٢','مَنِ الْأَوَّلُ؟','Кто первый?','11–20','#3fa34d',None,'soon'),
('٣','مَنِ الْأُولَى؟','Кто первая?','21–30','#ef8a2c',None,'soon'),('٤','تَعَارُفٌ «٢»','Знакомство 2','31–40','#6a3d9a',None,'soon'),
('٥','أُسْرَةُ مُحَمَّدٍ','Семья Мухаммада','43–52','#b23a72','urok5/img/scene.jpg','done'),('٦','حِذَائِي','Мои ботинки','53–62','#8a5a3c','urok6/img/scene.jpg','done'),
('٧','أُسْرَةُ بَتُولَ','Семья Батуль','63–72','#1f9c8f','urok7/img/scene.jpg','done'),('٨','الْأَيَّامُ','Дни недели','73–82','#8f9a2f','urok8/img/scene.jpg','now')]
def card(n,t,ru,p,c,img,st):
    pr={'done':'10/10','now':'3/10','soon':''}[st]
    pc={'done':100,'now':30,'soon':0}[st]
    pic=f'<img src="{J(img)}">' if img else f'<div class="ph2" style="background:linear-gradient(135deg,{c}22,{c}55)"><span>{n}</span></div>'
    badge={'done':'<span class="st ok">✓ Пройден</span>','now':'<span class="st now">● Идём сейчас</span>','soon':'<span class="st soon">Скоро</span>'}[st]
    return f'''<div class="lc {st}" style="--c:{c}"><div class="pic">{pic}<span class="isl">{n}</span>{badge}</div>
<div class="body"><div class="ar t">{t}</div><div class="sub">{ru} · стр. {p}</div>{f'<div class="pb"><i style="width:{pc}%"></i></div><div class="pt">{pr} страниц</div>' if st!='soon' else ''}</div></div>'''
cards=''.join(card(*x) for x in L)
html=f'''<!doctype html><html><head><meta charset=utf-8><style>{CSS}{css}
body{{padding:0;background:#f6f3fc}}
.hero{{background:radial-gradient(circle at 80% -20%,#8f72f0,#3d2884 55%,#2b2350);color:#fff;padding:36px 56px 110px;position:relative;overflow:hidden}}
.hero::after{{content:'';position:absolute;right:-80px;top:-80px;width:420px;height:420px;border-radius:50%;background:radial-gradient(circle,rgba(255,197,49,.25),transparent 65%)}}
.top{{display:flex;align-items:center;gap:16px;direction:rtl}}
.logo{{width:64px;height:64px;border-radius:20px;background:linear-gradient(180deg,#ffd75e,#ffb000);display:grid;place-items:center;font:44px Lal;color:#3a2600;box-shadow:0 4px 0 #d99200,0 12px 24px -8px rgba(217,146,0,.6)}}
.bt{{font:44px Lal}}.bs{{font:800 16px Nu;opacity:.8;direction:ltr;text-align:right}}
.tools{{margin-right:auto;display:flex;gap:10px;direction:ltr}}.tools span{{padding:10px 16px;border-radius:14px;background:rgba(255,255,255,.12);font:900 14px Nu;box-shadow:inset 0 0 0 1px rgba(255,255,255,.15)}}
.cont{{margin-top:34px;display:flex;gap:28px;align-items:center;direction:rtl;position:relative;z-index:2}}
.cont img{{width:300px;height:170px;object-fit:cover;border-radius:22px;border:6px solid rgba(255,255,255,.95);box-shadow:0 20px 40px -12px rgba(0,0,0,.5);transform:rotate(-2deg)}}
.cont .k{{font:900 13px Nu;letter-spacing:.12em;color:#ffd75e;direction:ltr;text-align:right}}.cont .h{{font:58px/1.1 Lal}}.cont .r{{font:800 18px Nu;opacity:.85;direction:ltr;text-align:right}}
.cont .act{{display:flex;gap:12px;margin-top:16px;direction:ltr;justify-content:flex-end}}
.wrap{{margin:-84px 56px 40px;position:relative;z-index:3}}
.sec{{display:flex;align-items:baseline;gap:12px;margin:28px 4px 14px;direction:ltr}}.sec b{{font:900 22px Nu}}.sec span{{font:800 14px Nu;color:var(--mut)}}.sec[style] span{{color:#d9d0ff}}
.lessons{{display:grid;grid-template-columns:repeat(4,1fr);gap:20px;direction:rtl}}
.lc{{background:#fff;border-radius:24px;overflow:hidden;box-shadow:var(--sh2);position:relative}}
.lc .pic{{height:150px;position:relative}}.lc .pic img{{width:100%;height:100%;object-fit:cover}}
.ph2{{width:100%;height:100%;display:grid;place-items:center}}.ph2 span{{font:96px Lal;color:var(--c);opacity:.35}}
.isl{{position:absolute;right:14px;bottom:-22px;width:52px;height:52px;border-radius:16px;background:var(--c);color:#fff;display:grid;place-items:center;font:34px Lal;box-shadow:0 0 0 4px #fff,0 8px 16px -6px rgba(0,0,0,.4)}}
.st{{position:absolute;left:12px;top:12px;font:900 12px Nu;padding:6px 10px;border-radius:999px;backdrop-filter:blur(6px)}}
.st.ok{{background:rgba(236,253,243,.92);color:#15803d}}.st.now{{background:linear-gradient(180deg,#ffd75e,#ffb000);color:#3a2600;box-shadow:0 4px 10px -2px rgba(217,146,0,.6)}}.st.soon{{background:rgba(255,255,255,.85);color:var(--mut)}}
.body{{padding:28px 18px 18px;direction:rtl}}.t{{font-size:24px;line-height:1.4}}.lc .sub{{font:800 13px Nu;color:var(--mut);direction:ltr;text-align:right;background:none;box-shadow:none;height:auto;padding:0;display:block}}
.pb{{height:8px;border-radius:99px;background:#ece7f7;margin-top:12px;overflow:hidden}}.pb i{{display:block;height:100%;border-radius:inherit;background:linear-gradient(90deg,#34d399,#16a34a)}}
.pt{{font:800 12px Nu;color:var(--mut);margin-top:6px;direction:ltr;text-align:right}}
.lc.now{{box-shadow:0 0 0 2px rgba(255,176,0,.7),0 0 0 8px rgba(255,197,49,.2),0 24px 40px -16px rgba(217,146,0,.5);transform:translateY(-4px)}}
.lc.now .pb i{{background:linear-gradient(90deg,#ffd75e,#ffb000)}}
.lc.soon .pic{{filter:saturate(.6)}}.lc.soon .t{{color:#6f6888}}
.extra{{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}}
.ex{{background:#fff;border-radius:22px;padding:18px 20px;box-shadow:var(--sh1);display:flex;align-items:center;gap:16px;direction:rtl}}
.ex .ic{{width:54px;height:54px;border-radius:16px;display:grid;place-items:center;font-size:26px;background:linear-gradient(180deg,#f4f0ff,#e9e1ff)}}
.ex b{{font:700 21px Nas;display:block}}.ex span{{font:800 13px Nu;color:var(--mut);direction:ltr;display:block;text-align:right}}
</style></head><body>
<div class="hero"><div class="top"><div class="logo">٢</div><div><div class="bt">الْعَرَبِيَّةُ بَيْنَ يَدَيْ أَوْلَادِنَا</div><div class="bs">Книга 2 · пособие по урокам</div></div>
<div class="tools"><span>👥 Дети и звёзды</span><span>🔗 Домашки</span><span>📊 Результаты</span></div></div>
<div class="cont"><img src="{J('urok8/img/scene.jpg')}"><div><div class="k">ПРОДОЛЖИТЬ</div><div class="h">الْأَيَّامُ</div><div class="r">Урок 8 · остановились на странице 75</div>
<div class="act"><span class="btn b-soft">🔗 Домашка урока</span><span class="btn b-gold">▶ Открыть стр. 75</span></div></div></div></div>
<div class="wrap"><div class="sec" style="color:#fff;margin-top:0"><b>Уроки</b><span>8 уроков · 82 страницы</span></div><div class="lessons">{cards}</div>
<div class="sec"><b>Повторение и проверка</b><span>после каждых четырёх уроков</span></div>
<div class="extra"><div class="ex"><span class="ic">🔁</span><div><b>هَلْ تَذْكُرُونَ؟ ١–٤</b><span>Повторение · стр. 41–42</span></div></div><div class="ex"><span class="ic">🔁</span><div><b>هَلْ تَذْكُرُونَ؟ ٥–٨</b><span>Повторение · стр. 83–84</span></div></div><div class="ex"><span class="ic">🏆</span><div><b>اِخْتِبَارٌ</b><span>Экзамен по книге</span></div></div></div></div>
</body></html>'''
open('home.html','w').write(html)
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch();pg=await b.new_page(viewport={'width':1440,'height':900},device_scale_factor=1.5);await pg.goto('file:///home/claude/maket/home.html');await pg.wait_for_timeout(800);await pg.screenshot(path='home.png',full_page=True)
        pg=await b.new_page(viewport={'width':390,'height':800},device_scale_factor=3);await pg.add_style_tag if False else None
        await b.close()
asyncio.run(main())
