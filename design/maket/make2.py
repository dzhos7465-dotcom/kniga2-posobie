import asyncio
exec(open('make.py').read().split("D=[")[0])
CSS2=CSS+'''
:root{--u:#5a3fa0;--acc:#ffb703;--g:#1b9e5a;--b:#1f6fd1;--bg:#2b2350}
'''
D=[('fadl','فَضْل','مَتَى تَزُورُ عَمَّكَ؟'),('muh','مُحَمَّد','يَوْمَ السَّبْتِ، وَيَوْمَ الْإِثْنَيْنِ.'),('fadl','فَضْل','وَمَتَى تَزُورُ جَدَّكَ؟'),('muh','مُحَمَّد','يَوْمَ الْجُمُعَةِ، وَيَوْمَ الْأَحَدِ، وَلَيْلَةَ الثُّلَاثَاءِ.'),('fadl','فَضْل','وَمَتَى تَزُورُ خَالَتَكَ؟'),('muh','مُحَمَّد','يَوْمَ الْخَمِيسِ، وَلَيْلَةَ الْأَرْبِعَاءِ.'),('fadl','فَضْل','وَمَتَى تَزُورُ خَالَكَ؟'),('muh','مُحَمَّد','أَزُورُهُ وَسَطَ الْأُسْبُوعِ.')]
bub=''.join(f'''<div class="bb {s} {'on' if i==3 else ''}"><span class="av">{n[0]}</span><div class="bx"><span class="ar">{t}</span>{'<div class="tr">В пятницу, в воскресенье и в ночь на вторник.</div>' if i==3 else ''}</div><span class="mini">▶</span>{'<span class="mini ru">Ру</span>' if i!=3 else '<span class="mini ru on">Ру</span>'}</div>''' for i,(s,n,t) in enumerate(D))
W=[('sabt','السَّبْتُ'),('ahad','الْأَحَدُ'),('ithnayn','الْإِثْنَيْنِ'),('thulatha','الثُّلَاثَاءُ'),('arbia','الْأَرْبِعَاءُ'),('khamis','الْخَمِيسُ'),('jumua','الْجُمُعَةُ'),('yazur','يَزُورُ'),('khala','خَالَةٌ'),('layla','لَيْلَةٌ'),('wasat','وَسَطٌ'),('usbu','الْأُسْبُوعُ')]
cards=''.join(f'<div class="fc {"flip" if k=="khala" else ""}"><img src="{I("w_"+k+".jpg")}"><span class="ar">{w}</span>{"<i>тётя по маме</i>" if k=="khala" else ""}</div>' for k,w in W)
desk=f'''<!doctype html><html><head><meta charset=utf-8><style>{CSS2}
body{{width:1440px;height:900px;overflow:hidden;background:radial-gradient(circle at 20% 0,#3d3170,#211a3f 70%)}}
.rail{{position:absolute;left:0;top:0;bottom:0;width:86px;display:flex;flex-direction:column;align-items:center;gap:10px;padding:18px 0}}
.lg{{width:58px;height:58px;border-radius:18px;background:var(--acc);color:#3b2a00;display:grid;place-items:center;font:40px Lal;margin-bottom:8px}}
.rb{{width:56px;height:46px;border-radius:14px;color:#cfc6f2;display:grid;place-items:center;font:700 18px Nas;background:#ffffff14;position:relative}}.rb.cur{{background:#fff;color:var(--u)}}.rb.ok::after{{content:'';position:absolute;right:4px;top:4px;width:9px;height:9px;border-radius:50%;background:#4ade80}}
.book{{position:absolute;left:110px;right:24px;top:22px;bottom:96px;display:flex;filter:drop-shadow(0 25px 40px #0007)}}
.pgL,.pgR{{flex:1;background:#fffaf0;padding:22px 30px;position:relative}}
.pgL{{border-radius:26px 6px 6px 26px;background:linear-gradient(90deg,#fffaf0 92%,#efe4cf)}}.pgR{{border-radius:6px 26px 26px 6px;background:linear-gradient(270deg,#fffaf0 92%,#efe4cf)}}
.num{{position:absolute;bottom:14px;font:700 22px Nas;color:#b5a88f}}.pgL .num{{left:30px}}.pgR .num{{right:30px}}
.h{{display:flex;align-items:center;gap:12px;direction:rtl;margin-bottom:12px}}.h .n{{width:40px;height:40px;border-radius:12px;background:var(--u);color:#fff;display:grid;place-items:center;font:700 22px Nas;transform:rotate(-6deg)}}.h .ar{{font-size:30px;color:var(--u)}}
.sc{{width:100%;border-radius:20px;border:8px solid #fff;box-shadow:0 6px 18px #0002;transform:rotate(-1.2deg)}}
.chat{{display:flex;flex-direction:column;gap:5px}}
.bb{{display:flex;align-items:center;gap:8px}}.bb.fadl{{direction:rtl}}.bb.muh{{direction:ltr}}
.av{{width:36px;height:36px;border-radius:50%;display:grid;place-items:center;color:#fff;font:700 20px Nas;flex:none}}.fadl .av{{background:var(--g)}}.muh .av{{background:var(--b)}}
.bx{{max-width:72%;padding:8px 18px;border-radius:22px;direction:rtl;box-shadow:0 2px 0 #0000000f}}.fadl .bx{{background:#e3f5ea;border-top-right-radius:6px}}.muh .bx{{background:#e4efff;border-top-left-radius:6px}}
.bx .ar{{font-size:21px;line-height:1.5}}.fadl .ar{{color:#126b3d}}.muh .ar{{color:#174f9a}}
.bb.on .bx{{box-shadow:0 0 0 4px var(--acc);}}.tr{{font:800 14px Nu;color:#6b6478;direction:ltr;text-align:right}}
.mini{{width:30px;height:30px;border-radius:50%;background:#fff;border:2px solid #e6dcc7;display:grid;place-items:center;font:900 11px Nu;color:var(--u);flex:none}}.mini.ru.on{{background:var(--u);color:#fff;border-color:var(--u)}}
.cards{{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;direction:rtl}}
.fc{{background:#fff;border-radius:18px;padding:8px 6px 6px;text-align:center;box-shadow:0 3px 0 #e6dcc7;position:relative}}.fc img{{width:100%;aspect-ratio:1;object-fit:contain}}.fc .ar{{font-size:19px;display:block}}
.fc.flip{{background:var(--acc);box-shadow:0 3px 0 #c98f00}}.fc i{{position:absolute;inset:auto 6px 34px;background:#fff;border-radius:10px;font:900 12px Nu;padding:3px;font-style:normal}}
.dock{{position:absolute;left:110px;right:24px;bottom:18px;height:62px;border-radius:20px;background:#ffffff12;display:flex;align-items:center;gap:10px;padding:0 12px;direction:ltr}}
.dk{{height:44px;padding:0 16px;border-radius:13px;display:flex;align-items:center;gap:8px;font:900 15px Nu;color:#e9e4ff;background:#ffffff14}}.dk.y{{background:var(--acc);color:#3b2a00}}.dk.gr{{background:#22c55e;color:#fff}}
.sp{{flex:1}}.pill{{font:900 13px Nu;color:#cfc6f2}}
.sw{{width:40px;height:24px;border-radius:12px;background:#ffffff33;position:relative}}.sw::after{{content:'';position:absolute;left:3px;top:3px;width:18px;height:18px;border-radius:50%;background:#fff}}
.tch{{position:absolute;left:60px;bottom:50px;width:330px;background:#fff6d6;border-radius:4px 18px 18px 18px;padding:12px 14px;font:800 13px/1.45 Nu;box-shadow:0 8px 20px #0003;transform:rotate(1.5deg);z-index:3}}.tch b{{font:700 16px Nas}}.tch h5{{font:900 11px Nu;color:#a07b00;letter-spacing:.08em;margin-bottom:4px}}
</style></head><body>
<div class="rail"><div class="lg">٨</div>{''.join(f'<span class="rb {c}">{n}</span>' for n,c in [('٧٣','cur'),('٧٤','ok'),('٧٥',''),('٧٦',''),('٧٧',''),('٧٨',''),('٧٩',''),('٨٠',''),('٨١','ok'),('٨٢','')])}</div>
<div class="book">
<div class="pgL"><div class="h"><span class="n">٢</span><span class="ar">كَلِمَاتٌ جَدِيدَةٌ</span></div><div class="cards">{cards}</div><span class="num">٧٣</span></div>
<div class="pgR"><div class="h"><span class="n">١</span><span class="ar">اُنْظُرْ وَاسْتَمِعْ وَأَعِدْ</span></div><img class="sc" src="{I('scene.jpg')}" style="height:150px;object-fit:cover;margin-bottom:8px"><div class="chat">{bub}</div><span class="num">٧٣</span></div>
<div class="tch"><h5>📌 ЗАМЕТКА УЧИТЕЛЮ</h5>Жест <b>لَيْلَةَ</b> — ладонь у щеки. <b>لَيْلَةَ الثُّلَاثَاءِ</b> = понедельник вечером.<br><br>Счётчик: <b>يَزُورُ</b> 18/40 · <b>لَيْلَة</b> 11/40</div>
</div>
<div class="dock"><span class="dk y">▶ Весь диалог</span><span class="dk">🙈 Только слушать</span><span class="dk">⏸ Пауза</span><span class="sp"></span><span class="pill">Перевод детям</span><span class="sw"></span><span class="dk">🎯 Закрепить</span><span class="dk gr">✓ Пройдено</span><span class="dk">‹</span><span class="dk">›</span></div>
</body></html>'''
T=['اِسْمِي هِنْدٌ،','أَزُورُ جَدَّتِي فِي بَيْتِهَا يَوْمَ الْخَمِيسِ.','أَذْهَبُ أَنَا وَوَالِدِي وَوَالِدَتِي بِالسَّيَّارَةِ.','اِسْمُ جَدَّتِي لَيْلَى.']
mob=f'''<!doctype html><html><head><meta charset=utf-8><style>{CSS2}
body{{width:390px;background:#f4f1fb}}
.hero{{background:linear-gradient(160deg,#5a3fa0,#2b2350);color:#fff;padding:16px 16px 54px;border-radius:0 0 30px 30px;direction:rtl}}
.r1{{display:flex;align-items:center;gap:10px}}.lg{{width:40px;height:40px;border-radius:13px;background:var(--acc);color:#3b2a00;display:grid;place-items:center;font:28px Lal}}.t{{font:26px Lal}}.me{{margin-right:auto;font:900 12px Nu;background:#ffffff22;padding:6px 10px;border-radius:10px;direction:ltr}}
.steps{{display:flex;gap:5px;margin-top:14px;direction:rtl}}.steps i{{flex:1;height:6px;border-radius:3px;background:#ffffff33}}.steps i.d{{background:#4ade80}}.steps i.c{{background:var(--acc)}}
.st{{font:900 12px Nu;color:#d9d0ff;margin-top:8px;direction:ltr;text-align:right}}
.card{{margin:-38px 12px 0;background:#fff;border-radius:24px;padding:14px;box-shadow:0 10px 30px #2b235022}}
.h{{display:flex;align-items:center;gap:8px;direction:rtl}}.h .n{{width:30px;height:30px;border-radius:10px;background:var(--u);color:#fff;display:grid;place-items:center;font:700 16px Nas;transform:rotate(-6deg)}}.h .ar{{font-size:20px;color:var(--u)}}
.story{{position:relative;margin-top:10px}}.story img{{width:100%;border-radius:18px;display:block}}
.big{{position:absolute;left:10px;bottom:10px;background:var(--acc);color:#3b2a00;font:900 13px Nu;padding:8px 12px;border-radius:12px;box-shadow:0 4px 10px #0003}}
.sent{{display:flex;gap:6px;flex-wrap:wrap;direction:rtl;margin-top:12px}}
.sent span{{background:#f4f1fb;border-radius:12px;padding:4px 10px;font:700 19px/1.7 Nas;color:#2b2350}}.sent span.on{{background:var(--acc)}}
.trb{{margin-top:8px;background:#2b2350;color:#fff;border-radius:14px;padding:8px 12px;font:800 13px Nu;display:flex;gap:8px;align-items:center}}.trb b{{background:#ffffff22;border-radius:8px;padding:2px 7px;font-size:11px}}
.q{{margin:12px 12px 0;background:#fff;border-radius:22px;padding:16px;box-shadow:0 6px 20px #2b235014;text-align:center}}
.qn{{font:900 12px Nu;color:#8a83a3}}.qq{{font:700 23px/1.6 Nas;margin:6px 0 12px;direction:rtl}}
.ans{{display:flex;gap:12px}}.ans span{{flex:1;height:64px;border-radius:18px;display:grid;place-items:center;font:900 30px Nu}}.ok{{background:#dcfce7;color:#15803d;box-shadow:inset 0 0 0 3px #22c55e}}.no{{background:#f4f1fb;color:#8a83a3}}
.fb{{margin-top:10px;font:800 13px Nu;color:#15803d}}
.nav{{display:flex;justify-content:space-around;margin:14px 12px 16px;background:#fff;border-radius:20px;padding:10px;box-shadow:0 6px 20px #2b235014}}.nav span{{display:flex;flex-direction:column;align-items:center;font:900 11px Nu;color:#8a83a3;gap:2px}}.nav b{{font-size:20px}}.nav .c{{color:var(--u)}}
</style></head><body>
<div class="hero"><div class="r1"><div class="lg">٨</div><span class="t">الْأَيَّامُ</span><span class="me">Амина ★★</span></div><div class="steps"><i class="d"></i><i class="d"></i><i class="d"></i><i class="d"></i><i class="c"></i><i></i><i></i><i></i></div><div class="st">Страница 81 · 5 из 8</div></div>
<div class="card"><div class="h"><span class="n">٣</span><span class="ar">اِقْرَأْ</span></div><div class="story"><img src="{I('b_chtenie.jpg')}"><span class="big">▶ Слушать текст</span></div>
<div class="sent">{''.join(f'<span class="{"on" if i==1 else ""}">{t}</span>' for i,t in enumerate(T))}</div>
<div class="trb"><b>Ру</b>Я навещаю бабушку у неё дома в четверг.</div></div>
<div class="q"><div class="qn">Вопрос 2 из 4 · верно или нет?</div><div class="qq">تَزُورُ هِنْدٌ جَدَّتَهَا يَوْمَ السَّبْتِ.</div><div class="ans"><span class="no">✓</span><span class="ok">✗</span></div><div class="fb">Верно! Хинд навещает бабушку в четверг — يَوْمَ الْخَمِيسِ</div></div>
<div class="nav"><span><b>📖</b>Книга</span><span class="c"><b>✏️</b>Задание</span><span><b>🎮</b>Игры</span><span><b>⭐</b>Звёзды</span></div>
</body></html>'''
open('desk2.html','w').write(desk);open('mob2.html','w').write(mob)
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        pg=await b.new_page(viewport={'width':1440,'height':900},device_scale_factor=1.5);await pg.goto('file:///home/claude/maket/desk2.html');await pg.wait_for_timeout(700);await pg.screenshot(path='d2.png')
        pg=await b.new_page(viewport={'width':390,'height':800},device_scale_factor=3);await pg.goto('file:///home/claude/maket/mob2.html');await pg.wait_for_timeout(700);await pg.screenshot(path='m2.png',full_page=True)
        await b.close()
asyncio.run(main())
