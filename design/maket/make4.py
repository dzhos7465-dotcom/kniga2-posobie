import asyncio
exec(open("make2.py").read().split("\nD=[")[0])
base=open('make2.py').read()
mcss=base.split("mob=f'''<!doctype html><html><head><meta charset=utf-8><style>{CSS2}")[1].split("</style>")[0].replace("{{","{").replace("}}","}")
W=['sabt','ahad','ithnayn','thulatha','arbia','khamis','jumua','yazur','khala','layla','wasat','usbu']
strip=''.join(f'<img src="{I("w_"+k+".jpg")}">' for k in W[:6])
start=f'''<div class="ph"><div class="hero big2"><div class="r1"><div class="lg">٨</div><span class="t">الْأَيَّامُ</span></div><div class="ttl2">Домашка · часть 1</div><div class="st2">Слова и диалог · стр. 73</div><div class="strip">{strip}</div></div>
<div class="card c2"><div class="row3"><div><b>25</b><span>вопросов</span></div><div><b>10</b><span>минут</span></div><div><b>🎧</b><span>со звуком</span></div></div>
<input class="nm" value="Амина"><div class="go">Начать ▶</div>
<div class="small">Ошибки вернутся в конце — второй шанс</div></div>
<div class="lbl">1 · Начало</div></div>'''
q=f'''<div class="ph"><div class="hero"><div class="r1"><div class="lg">٨</div><span class="t">الْأَيَّامُ</span><span class="me">7 / 25</span></div>
<div class="dots2">{''.join('<i class="d"></i>' for _ in range(6))}<i class="c"></i>{''.join('<i></i>' for _ in range(18))}</div></div>
<div class="card qc"><div class="qn">Послушай и выбери перевод</div><div class="spkbig">▶</div><div class="opt2"><span>среда</span><span class="ok2">четверг ✓</span><span>пятница</span><span>ночь, вечер</span></div>
<div class="after"><img src="{I('w_khamis.jpg')}"><div><span class="ar">الْخَمِيسُ</span><small><bdi class="ar">خَمْسَة</bdi> = 5 · 5-й день у арабов → четверг</small></div></div>
<div class="next">Дальше ›</div></div><div class="lbl">2 · Вопрос</div></div>'''
end=f'''<div class="ph"><div class="hero big3"><div class="conf">🎉</div><div class="t3">مُمْتَازٌ!</div><div class="sc3">23 / 25</div><div class="stars3">★★★</div></div>
<div class="card c2"><div class="who3">Амина · урок 8 · часть 1 · 27.11</div>
<div class="wl"><div class="wt">Повтори эти слова:</div><span class="ar">لَيْلَةٌ</span><span class="ar">وَسَطٌ</span></div>
<div class="go wa">📲 Отправить учителю</div><div class="go2">↺ Пройти ещё раз</div></div><div class="lbl">3 · Итог</div></div>'''
html=f'''<!doctype html><html><head><meta charset=utf-8><style>{CSS2}{mcss}
body{{width:1230px;background:#2b2350;display:flex;gap:30px;padding:30px}}
.ph{{width:390px;background:#f4f1fb;border-radius:42px;overflow:hidden;position:relative;padding-bottom:58px;box-shadow:0 0 0 10px #15112b}}
.lbl{{position:absolute;bottom:14px;left:0;right:0;text-align:center;font:900 15px Nu;color:#8a83a3}}
.big2{{padding-bottom:70px}}.ttl2{{font:900 24px Nu;margin-top:16px;direction:ltr;text-align:right}}.st2{{font:800 14px Nu;color:#d9d0ff;direction:ltr;text-align:right}}
.strip{{display:flex;gap:6px;margin-top:14px}}.strip img{{width:48px;height:48px;background:#fff;border-radius:12px;object-fit:contain;padding:2px}}
.c2{{margin-top:-44px;display:flex;flex-direction:column;gap:12px}}.row3{{display:flex;gap:8px}}.row3 div{{flex:1;background:#f4f1fb;border-radius:16px;padding:10px 4px;text-align:center}}.row3 b{{display:block;font:900 24px Nu;color:var(--u)}}.row3 span{{font:800 12px Nu;color:#8a83a3}}
.nm{{border:3px solid #e5ddff;border-radius:16px;padding:12px;font:900 18px Nu;text-align:center;color:var(--u)}}
.go{{background:var(--acc);color:#3b2a00;border-radius:18px;padding:16px;text-align:center;font:900 20px Nu;box-shadow:0 5px 0 #c98f00}}.go.wa{{background:#22c55e;color:#fff;box-shadow:0 5px 0 #15803d}}
.go2{{text-align:center;font:900 15px Nu;color:var(--u);padding:8px}}.small{{text-align:center;font:800 12px Nu;color:#8a83a3}}
.dots2{{display:flex;gap:3px;margin-top:14px}}.dots2 i{{flex:1;height:6px;border-radius:3px;background:#ffffff33}}.dots2 i.d{{background:#4ade80}}.dots2 i.c{{background:var(--acc)}}
.qc{{margin-top:-30px;display:flex;flex-direction:column;gap:14px;align-items:center}}.qn{{font:900 15px Nu;color:#8a83a3}}
.spkbig{{width:110px;height:110px;border-radius:50%;background:var(--u);color:#fff;display:grid;place-items:center;font-size:40px;box-shadow:0 0 0 12px #ece6ff}}
.opt2{{display:grid;grid-template-columns:1fr 1fr;gap:10px;width:100%}}.opt2 span{{background:#f4f1fb;border-radius:16px;padding:16px 6px;text-align:center;font:900 17px Nu;color:#2b2350}}.opt2 .ok2{{background:#dcfce7;color:#15803d;box-shadow:inset 0 0 0 3px #22c55e}}
.after{{display:flex;gap:10px;align-items:center;background:#fff8e1;border-radius:16px;padding:8px 12px;width:100%;direction:rtl}}.after img{{width:58px;height:58px;object-fit:contain;background:#fff;border-radius:12px}}.after .ar{{font-size:24px;display:block}}.after small{{font:800 12px Nu;color:#8a6d00;direction:ltr;display:block;text-align:right}}
.next{{align-self:stretch;text-align:center;background:var(--u);color:#fff;border-radius:16px;padding:14px;font:900 17px Nu}}
.big3{{text-align:center;padding:30px 16px 70px}}.conf{{font-size:40px}}.t3{{font:44px Lal;color:var(--acc)}}.sc3{{font:900 54px Nu;direction:ltr}}.stars3{{font-size:40px;color:var(--acc);letter-spacing:6px}}
.who3{{text-align:center;font:900 14px Nu;color:#8a83a3}}.wl{{background:#f4f1fb;border-radius:16px;padding:12px;display:flex;gap:10px;align-items:center;justify-content:center;flex-wrap:wrap}}.wt{{width:100%;text-align:center;font:900 13px Nu;color:#8a83a3}}.wl .ar{{background:#fff;border-radius:12px;padding:4px 12px;font-size:22px}}
</style></head><body>{start}{q}{end}</body></html>'''
open('hw.html','w').write(html)
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch();pg=await b.new_page(viewport={'width':1290,'height':800},device_scale_factor=2);await pg.goto('file:///home/claude/maket/hw.html');await pg.wait_for_timeout(700);await pg.screenshot(path='hw.png',full_page=True);await b.close()
asyncio.run(main())
