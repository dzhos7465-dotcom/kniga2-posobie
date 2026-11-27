import asyncio
exec(open("make2.py").read().split("\nD=[")[0])
base=open('make2.py').read()
# общий CSS desk из make2
dcss=base.split("desk=f'''<!doctype html><html><head><meta charset=utf-8><style>{CSS2}")[1].split("</style>")[0].replace("{{","{").replace("}}","}")
rail=''.join(f'<span class="rb {c}">{n}</span>' for n,c in [('٧٣','ok'),('٧٤','cur'),('٧٥','cur'),('٧٦',''),('٧٧',''),('٧٨',''),('٧٩',''),('٨٠',''),('٨١','ok'),('٨٢','')])
RR=[('khamis','khamis','ahad','a','#e8794a',1),('ahad','arbia','ahad','b','#555b66',1),('ithnayn','ithnayn','khamis','a','#22a6b3',0),('jumua','thulatha','jumua','b','#6c4ba3',2),
   ('sabt','ithnayn','sabt','b','#e58a9b',0),('layla','layla','wasat','a','#3fb4d8',1),('thulatha','sabt','thulatha','b','#2f80d1',0),('usbu','ithnayn','usbu','b','#ef6c00',0)]
NAME={'khamis':'الْخَمِيسُ','ahad':'الْأَحَدُ','ithnayn':'الْإِثْنَيْنِ','jumua':'الْجُمُعَةُ','sabt':'السَّبْتُ','layla':'لَيْلَةٌ','thulatha':'الثُّلَاثَاءُ','usbu':'الْأُسْبُوعُ'}
def ring(w,a,b,k,c,st):
    arc='M50 92 A38 38 0 0 0 50 16' if k=='a' else 'M50 92 A38 38 0 0 1 50 16'
    ok=st==1; bad=st==2
    return f'''<div class="rg {'done' if ok else ''}" style="--c:{c}"><svg viewBox="0 0 100 104"><circle cx="50" cy="54" r="38" fill="none" stroke="#ece4d6" stroke-width="4"/>{f'<path d="{arc}" fill="none" stroke="{c}" stroke-width="6" stroke-linecap="round"/>' if ok else ''}</svg>
<span class="rp a {'ok' if ok and k=='a' else ''} {'bad' if bad and k!='a' else ''}"><img src="{I('w_'+a+'.jpg')}"><b>أ</b></span><span class="rp b {'ok' if ok and k=='b' else ''} {'bad' if bad and k=='a' else ''}"><img src="{I('w_'+b+'.jpg')}"><b>ب</b></span><span class="rw ar">{NAME[w]}</span></div>'''
rings=''.join(ring(*r) for r in RR)
AB=[('arbia','khamis','a',1),('jumua','khala','b',1),('layla','yazur','a',0)]
ab=''.join(f'''<div class="abr"><span class="no">{"١٢٣"[i]}</span><span class="spk">▶</span><span class="abp {'ok' if s and k=='a' else ''}"><img src="{I('w_'+a+'.jpg')}"><i>{'✓' if s and k=='a' else ''}</i></span><span class="abp {'ok' if s and k=='b' else ''}"><img src="{I('w_'+b+'.jpg')}"><i>{'✓' if s and k=='b' else ''}</i></span></div>''' for i,(a,b,k,s) in enumerate(AB))
P4=[('أ','khamis','٣'),('ب','yazur',''),('ت','layla','١'),('ث','jumua',''),('ج','khala','٢'),('ح','wasat','')]
nums=''.join(f'<div class="np"><span class="lt">{l}</span><img src="{I("w_"+k+".jpg")}"><span class="bx {"f" if n else ""}">{n}</span></div>' for l,k,n in P4)
desk=f'''<!doctype html><html><head><meta charset=utf-8><style>{CSS2}{dcss}
.rings{{display:grid;grid-template-columns:repeat(4,1fr);gap:8px 14px;direction:rtl;margin-top:6px}}
.rg{{position:relative;aspect-ratio:1/1.04}}.rg svg{{position:absolute;inset:0;width:100%;height:100%}}
.rp{{position:absolute;top:0;width:44%;aspect-ratio:1;background:#fff;border:3px solid #e6dcc7;border-radius:14px;padding:2px}}.rp.a{{right:0}}.rp.b{{left:0}}.rp img{{width:100%;height:100%;object-fit:contain}}
.rp b{{position:absolute;bottom:-11px;left:50%;transform:translateX(-50%);width:24px;height:24px;border-radius:50%;background:#fff;border:2px solid var(--u);color:var(--u);font:700 13px Nas;display:grid;place-items:center}}
.rp.ok{{border-color:#22c55e;background:#effdf3}}.rp.ok b{{background:#22c55e;border-color:#22c55e;color:#fff}}.rp.bad{{border-color:#ef4444;background:#fef2f2}}
.rw{{position:absolute;bottom:0;left:50%;transform:translateX(-50%);width:54%;aspect-ratio:1;border-radius:50%;background:#fff;border:4px solid var(--c);display:grid;place-items:center;font-size:17px;text-align:center}}.rg.done .rw{{background:var(--c);color:#fff}}
.tip{{direction:ltr;font:800 13px Nu;color:#8a7f6a;text-align:right;margin:-4px 0 6px}}
.mini2{{display:flex;gap:8px;direction:rtl;margin-bottom:8px}}.mini2 span{{padding:7px 12px;border-radius:11px;background:#f1ebff;color:var(--u);font:900 13px Nu}}.mini2 span.on{{background:var(--u);color:#fff}}
.abr{{display:flex;align-items:center;gap:10px;direction:rtl;margin-bottom:8px}}.no{{width:30px;height:30px;border-radius:9px;background:var(--acc);display:grid;place-items:center;font:700 17px Nas}}
.spk{{width:38px;height:38px;border-radius:50%;background:var(--u);color:#fff;display:grid;place-items:center;font-size:14px}}
.abp{{width:96px;height:96px;background:#fff;border:3px solid #e6dcc7;border-radius:16px;position:relative;padding:3px}}.abp img{{width:100%;height:100%;object-fit:contain}}
.abp i{{position:absolute;left:-8px;top:-8px;width:26px;height:26px;border-radius:7px;background:#fff;border:3px solid #cfc3a8;display:grid;place-items:center;font:900 16px Nu;color:#fff;font-style:normal}}
.abp.ok{{border-color:#22c55e}}.abp.ok i{{background:#22c55e;border-color:#22c55e}}
.nums{{display:grid;grid-template-columns:repeat(6,1fr);gap:8px;direction:rtl}}.np{{background:#fff;border-radius:14px;padding:4px;position:relative;box-shadow:0 2px 0 #e6dcc7}}.np img{{width:100%;aspect-ratio:1;object-fit:contain}}
.lt{{position:absolute;top:4px;right:6px;font:700 15px Nas;color:var(--u)}}.np .bx{{display:block;margin:2px auto 2px;width:36px;height:36px;border:3px dashed #cfc3a8;border-radius:10px;font:700 20px Nas;text-align:center;line-height:30px}}.np .bx.f{{border:3px solid #22c55e;background:#effdf3;color:#15803d}}
.keyp{{display:flex;gap:6px;direction:rtl;margin-top:8px}}.keyp span{{width:38px;height:38px;border-radius:11px;background:#f1ebff;color:var(--u);display:grid;place-items:center;font:700 18px Nas}}.keyp span.use{{opacity:.35}}.keyp span.cur{{background:var(--acc);color:#3b2a00}}
.res{{margin-right:auto;font:900 13px Nu;color:#15803d;background:#dcfce7;padding:6px 10px;border-radius:10px;direction:ltr}}
.hh{{display:flex;align-items:center;gap:10px;direction:rtl;margin:12px 0 6px}}.hh .n{{width:32px;height:32px;border-radius:10px;background:var(--u);color:#fff;display:grid;place-items:center;font:700 18px Nas;transform:rotate(-6deg)}}.hh .ar{{font-size:23px;color:var(--u)}}
</style></head><body>
<div class="rail"><div class="lg">٨</div>{rail}</div>
<div class="book">
<div class="pgL"><div class="h"><span class="n">٣</span><span class="ar">اِسْتَمِعْ، وَضَعْ (✓)</span><span class="res">2 из 3 ✓</span></div>{ab}
<div class="hh"><span class="n">٤</span><span class="ar">اِسْتَمِعْ، وَضَعِ الرَّقْمَ الصَّحِيحَ</span></div><div class="tip">Нажмите ▶, потом на номер внизу и на картинку</div>
<div class="nums">{nums}</div><div class="keyp"><span class="spk">▶</span><span class="use">١</span><span class="use">٢</span><span class="use">٣</span><span class="cur">٤</span><span>٥</span><span>٦</span></div><span class="num">٧٥</span></div>
<div class="pgR"><div class="h"><span class="n">٢</span><span class="ar">صِلْ</span></div><div class="mini2"><span>Где мой…?</span><span>Правда или нет?</span><span class="on">Соедини</span><span>📖 Стрелки как в книге</span></div><div class="tip">Нажмите на слово — звучит диктор. Потом на картинку أ или ب</div>
<div class="rings">{rings}</div><span class="num">٧٤</span></div>
</div>
<div class="dock"><span class="dk y">▶ Слушать упражнение</span><span class="dk">Проверять: сразу</span><span class="dk">↺ Заново</span><span class="sp"></span><span class="pill">Перевод детям</span><span class="sw"></span><span class="dk">🎯 Закрепить</span><span class="dk gr">✓ Пройдено</span><span class="dk">‹</span><span class="dk">›</span></div>
</body></html>'''
# телефон: стр. 79 часы
import math
C=[('د','arbia',-90,''),('أ','khala',-45,'١'),('ب','ithnayn',0,''),('ت','thulatha',45,'٢'),('ث','sabt',90,''),('ج','khamis',135,''),('ح','jumua',180,''),('خ','ahad',225,'')]
cl=''.join(f'<div class="op" style="left:{50+38*math.cos(math.radians(a)):.1f}%;top:{50+38*math.sin(math.radians(a)):.1f}%"><img src="{I("w_"+k+".jpg")}"><span class="bx {"f" if n else ""}">{n}</span></div>' for l,k,a,n in C)
mcss=base.split("mob=f'''<!doctype html><html><head><meta charset=utf-8><style>{CSS2}")[1].split("</style>")[0].replace("{{","{").replace("}}","}")
mob=f'''<!doctype html><html><head><meta charset=utf-8><style>{CSS2}{mcss}
.clock{{position:relative;width:100%;aspect-ratio:1;margin:8px 0}}.dial{{position:absolute;inset:13%;border-radius:50%;border:12px solid #4db3e0;box-shadow:inset 0 0 0 5px #e5f4fb}}
.hand{{position:absolute;left:50%;top:50%;width:5%;height:26%;background:#c9c9c9;border-radius:8px;transform-origin:50% 0}}.hub{{position:absolute;left:50%;top:50%;width:18%;aspect-ratio:1;border-radius:50%;border:8px solid #2c93bf;background:#fff;transform:translate(-50%,-50%)}}
.op{{position:absolute;width:23%;margin:-11.5% 0 0 -11.5%;background:#fff;border-radius:14px;padding:2px;box-shadow:0 3px 10px #2b235022}}.op img{{width:100%;aspect-ratio:1;object-fit:contain}}
.op .bx{{position:absolute;bottom:-10px;left:50%;transform:translateX(-50%);width:28px;height:28px;border-radius:9px;background:#fff;border:3px dashed #cfc3a8;font:700 15px Nas;display:grid;place-items:center}}.op .bx.f{{border:3px solid #22c55e;background:#dcfce7;color:#15803d}}
.play{{display:flex;align-items:center;gap:10px;background:#f4f1fb;border-radius:16px;padding:8px 10px;margin-top:10px}}.pb{{width:46px;height:46px;border-radius:50%;background:var(--u);color:#fff;display:grid;place-items:center;font-size:16px}}.wave{{flex:1;height:26px;background:repeating-linear-gradient(90deg,#b9a8ef 0 3px,transparent 3px 7px);mask:linear-gradient(90deg,#000 45%,#0003 45%);-webkit-mask:linear-gradient(90deg,#000 45%,#0003 45%)}}.pt{{font:900 12px Nu;color:var(--u)}}
.nk{{display:flex;gap:6px;justify-content:center;margin-top:10px;direction:rtl}}.nk span{{width:36px;height:36px;border-radius:11px;background:#f1ebff;color:var(--u);display:grid;place-items:center;font:700 17px Nas}}.nk .u{{opacity:.3}}.nk .c{{background:var(--acc);color:#3b2a00}}
.hint2{{font:800 12px Nu;color:#8a83a3;text-align:center;margin-top:6px}}
</style></head><body>
<div class="hero"><div class="r1"><div class="lg">٨</div><span class="t">الْأَيَّامُ</span><span class="me">Амина ★★</span></div><div class="steps"><i class="d"></i><i class="d"></i><i class="d"></i><i class="c"></i><i></i><i></i><i></i><i></i></div><div class="st">Страница 79 · 4 из 8</div></div>
<div class="card"><div class="h"><span class="n">٢</span><span class="ar">اِسْتَمِعْ، وَضَعِ الرَّقْمَ الصَّحِيحَ</span></div>
<div class="play"><span class="pb">▶</span><span class="wave"></span><span class="pt">Фраза 3 из 8</span></div>
<div class="clock"><div class="dial"></div><div class="hand" style="transform:translateX(-50%) rotate(140deg)"></div><div class="hand" style="transform:translateX(-50%) rotate(220deg)"></div><div class="hub"></div>{cl}</div>
<div class="nk"><span class="u">١</span><span class="u">٢</span><span class="c">٣</span><span>٤</span><span>٥</span><span>٦</span><span>٧</span><span>٨</span></div>
<div class="hint2">Выбери номер ٣ и нажми на картинку, которую услышал</div></div>
<div class="nav"><span><b>📖</b>Книга</span><span class="c"><b>✏️</b>Задание</span><span><b>🎮</b>Игры</span><span><b>⭐</b>Звёзды</span></div>
</body></html>'''
open('desk3.html','w').write(desk);open('mob3.html','w').write(mob)
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        pg=await b.new_page(viewport={'width':1440,'height':900},device_scale_factor=1.5);await pg.goto('file:///home/claude/maket/desk3.html');await pg.wait_for_timeout(700);await pg.screenshot(path='d3.png')
        pg=await b.new_page(viewport={'width':390,'height':800},device_scale_factor=3);await pg.goto('file:///home/claude/maket/mob3.html');await pg.wait_for_timeout(700);await pg.screenshot(path='m3.png',full_page=True)
        await b.close()
asyncio.run(main())
