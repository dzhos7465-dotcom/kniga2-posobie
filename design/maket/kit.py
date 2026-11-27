import asyncio
exec(open("make.py").read().split("\nD=[")[0])
html=f'''<!doctype html><html><head><meta charset=utf-8><style>{CSS}
:root{{
 --ink:#221b3d;--mut:#8b84a6;--bg:#f6f3fc;
 --vi:#5b3fb0;--vi2:#7a5ce0;--vi-d:#3d2884;
 --go:#ffc531;--go2:#ffb000;--go-d:#c98500;
 --ok:#16a34a;--ok2:#34d399;--no:#e11d48;
 --r1:12px;--r2:18px;--r3:28px;
 --sh1:0 1px 2px rgba(34,27,61,.06),0 2px 6px rgba(34,27,61,.06);
 --sh2:0 2px 4px rgba(34,27,61,.05),0 10px 24px -6px rgba(34,27,61,.16);
 --sh3:0 4px 8px rgba(34,27,61,.06),0 24px 48px -12px rgba(61,40,132,.30);
}}
body{{width:1440px;background:linear-gradient(180deg,#fbf9ff,#f1ecfb);padding:40px 48px;color:var(--ink)}}
h1{{font:900 30px Nu;letter-spacing:-.01em}}h1 small{{font:800 15px Nu;color:var(--mut);margin-left:12px}}
h2{{font:900 13px Nu;letter-spacing:.12em;text-transform:uppercase;color:var(--mut);margin:0 0 14px}}
.grid{{display:grid;grid-template-columns:1fr 1fr 1fr;gap:22px;margin-top:26px}}
.panel{{background:#fff;border-radius:var(--r3);padding:22px 24px;box-shadow:var(--sh2);position:relative;overflow:hidden}}
.panel::before{{content:'';position:absolute;inset:0;border-radius:inherit;padding:1px;background:linear-gradient(180deg,rgba(255,255,255,.9),rgba(91,63,176,.10));-webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);-webkit-mask-composite:xor;mask-composite:exclude;pointer-events:none}}
.row{{display:flex;gap:14px;align-items:center;flex-wrap:wrap}}.cap{{font:800 12px Nu;color:var(--mut);margin-top:8px;text-align:center}}
/* палитра */
.sw{{width:74px}}.chip{{height:64px;border-radius:var(--r2);box-shadow:inset 0 1px 0 rgba(255,255,255,.35),var(--sh1)}}
/* кнопки */
.btn{{position:relative;border-radius:16px;padding:15px 26px;font:900 17px Nu;display:inline-flex;align-items:center;gap:10px;isolation:isolate}}
.b-gold{{color:#3a2600;background:linear-gradient(180deg,#ffd75e 0%,#ffc531 55%,#ffb000 100%);box-shadow:inset 0 1px 0 rgba(255,255,255,.7),inset 0 -2px 0 rgba(160,100,0,.25),0 4px 0 #d99200,0 10px 22px -6px rgba(217,146,0,.55)}}
.b-vi{{color:#fff;background:linear-gradient(180deg,#7a5ce0,#5b3fb0 60%,#4b32a0);box-shadow:inset 0 1px 0 rgba(255,255,255,.28),0 4px 0 #3d2884,0 10px 22px -6px rgba(61,40,132,.55)}}
.b-ok{{color:#fff;background:linear-gradient(180deg,#34d399,#16a34a);box-shadow:inset 0 1px 0 rgba(255,255,255,.35),0 4px 0 #0f7a37,0 10px 22px -6px rgba(22,163,74,.5)}}
.b-soft{{color:var(--vi);background:linear-gradient(180deg,#fff,#f4f0ff);box-shadow:inset 0 0 0 1px rgba(91,63,176,.14),0 2px 0 rgba(91,63,176,.12),var(--sh1)}}
.press{{transform:translateY(3px);box-shadow:inset 0 1px 0 rgba(255,255,255,.6),0 1px 0 #d99200,0 4px 10px -4px rgba(217,146,0,.5)}}
.dis{{color:#b3acc8;background:#efecf6;box-shadow:inset 0 0 0 1px #e6e1f2}}
/* круглые */
.play{{width:64px;height:64px;border-radius:50%;display:grid;place-items:center;color:#fff;font-size:22px;background:radial-gradient(circle at 35% 30%,#8f72f0,#5b3fb0 60%,#3d2884);box-shadow:inset 0 1px 0 rgba(255,255,255,.35),0 8px 18px -4px rgba(61,40,132,.6),0 0 0 6px rgba(122,92,224,.12)}}
.play.on{{box-shadow:inset 0 1px 0 rgba(255,255,255,.35),0 8px 18px -4px rgba(61,40,132,.6),0 0 0 8px rgba(255,197,49,.35),0 0 0 16px rgba(255,197,49,.12)}}
.ru{{height:38px;padding:0 14px;border-radius:999px;display:grid;place-items:center;font:900 14px Nu;color:var(--vi);background:#fff;box-shadow:inset 0 0 0 1px rgba(91,63,176,.18),var(--sh1)}}
.ru.on{{color:#fff;background:linear-gradient(180deg,#3a2f63,#221b3d);box-shadow:0 6px 14px -4px rgba(34,27,61,.5)}}
.tg{{width:56px;height:32px;border-radius:999px;background:linear-gradient(180deg,#7a5ce0,#5b3fb0);position:relative;box-shadow:inset 0 2px 4px rgba(0,0,0,.18)}}.tg::after{{content:'';position:absolute;right:4px;top:4px;width:24px;height:24px;border-radius:50%;background:linear-gradient(#fff,#f1eefb);box-shadow:0 2px 4px rgba(0,0,0,.25)}}
.tg.off{{background:#e3def0}}.tg.off::after{{right:auto;left:4px}}
/* ответы */
.ans{{display:grid;grid-template-columns:1fr 1fr;gap:12px}}
.opt{{position:relative;border-radius:var(--r2);padding:18px 10px;text-align:center;font:900 18px Nu;background:linear-gradient(180deg,#fff,#faf8ff);box-shadow:inset 0 0 0 1px rgba(91,63,176,.10),0 2px 0 rgba(91,63,176,.10),var(--sh1)}}
.opt.sel{{background:linear-gradient(180deg,#f7f3ff,#efe8ff);box-shadow:inset 0 0 0 1.5px rgba(122,92,224,.55),0 0 0 5px rgba(122,92,224,.12),var(--sh1);color:var(--vi-d)}}
.opt.good{{color:#0c6b31;background:linear-gradient(180deg,#f0fdf5,#d9f8e6);box-shadow:inset 0 0 0 1px rgba(22,163,74,.35),0 0 0 6px rgba(52,211,153,.16),0 12px 24px -10px rgba(22,163,74,.55)}}
.opt.bad{{color:#9f1239;background:linear-gradient(180deg,#fff5f7,#ffe4ea);box-shadow:inset 0 0 0 1px rgba(225,29,72,.28),0 8px 18px -10px rgba(225,29,72,.45)}}
.badge{{position:absolute;top:-10px;right:-10px;width:28px;height:28px;border-radius:50%;display:grid;place-items:center;color:#fff;font:900 14px Nu}}
.badge.g{{background:linear-gradient(180deg,#34d399,#16a34a);box-shadow:0 0 0 3px #fff,0 4px 10px rgba(22,163,74,.5)}}.badge.r{{background:linear-gradient(180deg,#fb7185,#e11d48);box-shadow:0 0 0 3px #fff,0 4px 10px rgba(225,29,72,.45)}}
/* карточки слов */
.wc{{width:132px;border-radius:22px;padding:10px 10px 8px;background:linear-gradient(180deg,#fff,#fbf9ff);box-shadow:0 1px 0 rgba(255,255,255,.9) inset,var(--sh2);text-align:center;position:relative}}
.wc img{{width:100%;aspect-ratio:1;object-fit:contain;border-radius:14px;background:radial-gradient(circle,#fff 60%,#f4f1fb)}}.wc .ar{{font-size:22px;display:block;line-height:1.6}}
.wc.on{{background:linear-gradient(180deg,#fff7dc,#ffe9a6);box-shadow:0 0 0 1.5px rgba(255,176,0,.55),0 0 0 7px rgba(255,197,49,.22),0 18px 30px -12px rgba(217,146,0,.55);transform:translateY(-4px)}}
.wc .tr{{font:800 12px Nu;color:#8a5a00}}
/* пузыри */
.bub{{border-radius:22px;padding:10px 18px;font:700 24px/1.55 Nas;direction:rtl;max-width:100%}}
.bub.g{{color:#0f5c33;background:linear-gradient(180deg,#effcf4,#dcf5e6);border-top-right-radius:8px;box-shadow:inset 0 1px 0 #fff,0 6px 14px -8px rgba(22,163,74,.45)}}
.bub.b{{color:#16408a;background:linear-gradient(180deg,#f1f6ff,#dde9ff);border-top-left-radius:8px;box-shadow:inset 0 1px 0 #fff,0 6px 14px -8px rgba(31,111,209,.45)}}
.bub.now{{box-shadow:inset 0 1px 0 #fff,0 0 0 2px rgba(255,197,49,.9),0 0 0 8px rgba(255,197,49,.18),0 12px 24px -10px rgba(217,146,0,.5)}}
/* прогресс и навигация */
.prog{{height:12px;border-radius:999px;background:#ece7f7;box-shadow:inset 0 1px 2px rgba(34,27,61,.12);overflow:hidden;width:100%}}.prog i{{display:block;height:100%;width:62%;border-radius:inherit;background:linear-gradient(90deg,#34d399,#16a34a);box-shadow:inset 0 1px 0 rgba(255,255,255,.5)}}
.nav{{display:flex;justify-content:space-around;background:rgba(255,255,255,.85);backdrop-filter:blur(10px);border-radius:24px;padding:10px;box-shadow:var(--sh3)}}.nav span{{display:flex;flex-direction:column;align-items:center;font:900 12px Nu;color:var(--mut);gap:2px;padding:6px 12px;border-radius:14px}}.nav b{{font-size:20px}}.nav .c{{color:var(--vi);background:linear-gradient(180deg,#f4f0ff,#ebe3ff)}}
.num{{width:46px;height:46px;border-radius:14px;display:grid;place-items:center;font:700 20px Nas;color:var(--vi);background:linear-gradient(180deg,#fff,#f4f0ff);box-shadow:inset 0 0 0 1px rgba(91,63,176,.14),0 2px 0 rgba(91,63,176,.12)}}
.num.cur{{color:#3a2600;background:linear-gradient(180deg,#ffd75e,#ffb000);box-shadow:inset 0 1px 0 rgba(255,255,255,.7),0 3px 0 #d99200,0 8px 16px -6px rgba(217,146,0,.6)}}.num.used{{opacity:.35;box-shadow:none;background:#efecf6}}
/* было / стало */
.vs{{display:grid;grid-template-columns:1fr 1fr;gap:16px}}.old .opt{{background:#fff;box-shadow:none;border:3px solid #22c55e;border-radius:12px}}.old .opt.bad{{border-color:#ef4444}}
.tag2{{font:900 12px Nu;color:var(--mut);margin-bottom:8px}}
</style></head><body>
<h1>Оформление · единые правила <small>кнопки, обводки, тени, цвета — одинаково на компьютере, телефоне и в домашке</small></h1>
<div class="grid">
<div class="panel"><h2>Цвета</h2><div class="row">
<div class="sw"><div class="chip" style="background:linear-gradient(160deg,#7a5ce0,#3d2884)"></div><div class="cap">Фиолетовый<br>основной</div></div>
<div class="sw"><div class="chip" style="background:linear-gradient(160deg,#ffd75e,#ffb000)"></div><div class="cap">Золото<br>главное действие</div></div>
<div class="sw"><div class="chip" style="background:linear-gradient(160deg,#34d399,#16a34a)"></div><div class="cap">Верно</div></div>
<div class="sw"><div class="chip" style="background:linear-gradient(160deg,#fb7185,#e11d48)"></div><div class="cap">Ошибка</div></div>
<div class="sw"><div class="chip" style="background:linear-gradient(160deg,#dcf5e6,#9fdcb8)"></div><div class="cap">Фадль</div></div>
<div class="sw"><div class="chip" style="background:linear-gradient(160deg,#dde9ff,#a9c6f5)"></div><div class="cap">Мухаммад</div></div>
<div class="sw"><div class="chip" style="background:#f6f3fc;box-shadow:inset 0 0 0 1px #e6e1f2"></div><div class="cap">Фон страницы</div></div>
<div class="sw"><div class="chip" style="background:#221b3d"></div><div class="cap">Текст</div></div></div>
<h2 style="margin-top:18px">Шрифты</h2><div class="ar" style="font-size:34px">مَتَى تَزُورُ عَمَّكَ؟</div><div style="font:900 20px Nu;margin-top:4px">Заголовок · Nunito 900</div><div style="font:800 15px Nu;color:var(--mut)">Подсказка и перевод · Nunito 800, серый</div></div>

<div class="panel"><h2>Кнопки · обычная · нажата · недоступна</h2>
<div class="row"><span class="btn b-gold">▶ Начать</span><span class="btn b-gold press">▶ Начать</span><span class="btn dis">▶ Начать</span></div>
<div class="row" style="margin-top:16px"><span class="btn b-vi">Дальше ›</span><span class="btn b-ok">✓ Пройдено</span><span class="btn b-soft">↺ Заново</span></div>
<h2 style="margin-top:22px">Звук · перевод · переключатель</h2>
<div class="row"><span class="play">▶</span><span class="play on">❚❚</span><span class="ru">Ру</span><span class="ru on">Ру</span><span class="tg"></span><span class="tg off"></span></div>
<div class="cap" style="text-align:left">Кнопка ▶ звучит — вокруг неё мягкое золотое свечение</div></div>

<div class="panel"><h2>Варианты ответа · четыре состояния</h2>
<div class="ans"><span class="opt">среда</span><span class="opt sel">пятница</span><span class="opt good">четверг<span class="badge g">✓</span></span><span class="opt bad">суббота<span class="badge r">✕</span></span></div>
<div class="cap" style="text-align:left">обычный · выбран · верно · ошибка — не рамкой, а мягкой заливкой, свечением и значком в углу</div>
<h2 style="margin-top:18px">Номера</h2><div class="row"><span class="num used">١</span><span class="num used">٢</span><span class="num cur">٣</span><span class="num">٤</span><span class="num">٥</span></div></div>

<div class="panel"><h2>Карточки слов</h2><div class="row" style="gap:18px;align-items:flex-end">
<div class="wc"><img src="{I('w_sabt.jpg')}"><span class="ar">السَّبْتُ</span></div>
<div class="wc on"><img src="{I('w_khala.jpg')}"><span class="ar">خَالَةٌ</span><span class="tr">тётя по маме</span></div></div>
<div class="cap" style="text-align:left">Нажатая карточка приподнимается и светится золотом</div></div>

<div class="panel"><h2>Реплики диалога</h2>
<div style="display:flex;flex-direction:column;gap:10px"><span class="bub g">مَتَى تَزُورُ عَمَّكَ؟</span><span class="bub b now" style="align-self:flex-start">يَوْمَ السَّبْتِ، وَيَوْمَ الْإِثْنَيْنِ.</span></div>
<div class="cap" style="text-align:left">Звучащая реплика — тонкая золотая кайма с ореолом</div></div>

<div class="panel"><h2>Прогресс и меню телефона</h2><div class="prog"><i></i></div><div class="cap" style="text-align:left">16 из 25</div>
<div class="nav" style="margin-top:14px"><span><b>📖</b>Книга</span><span class="c"><b>✏️</b>Задание</span><span><b>🎮</b>Игры</span><span><b>⭐</b>Звёзды</span></div></div>
</div>
<div class="panel" style="margin-top:22px"><h2>Было → стало</h2><div class="vs">
<div class="old"><div class="tag2">БЫЛО · просто цветная рамка</div><div class="ans"><span class="opt">среда</span><span class="opt">четверг ✓</span><span class="opt bad">суббота</span><span class="opt">пятница</span></div></div>
<div><div class="tag2">СТАЛО · заливка, глубина, свечение, значок</div><div class="ans"><span class="opt">среда</span><span class="opt good">четверг<span class="badge g">✓</span></span><span class="opt bad">суббота<span class="badge r">✕</span></span><span class="opt">пятница</span></div></div></div></div>
</body></html>'''
open('kit.html','w').write(html)
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch();pg=await b.new_page(viewport={'width':1440,'height':900},device_scale_factor=1.5);await pg.goto('file:///home/claude/maket/kit.html');await pg.wait_for_timeout(700);await pg.screenshot(path='kit.png',full_page=True);await b.close()
asyncio.run(main())
