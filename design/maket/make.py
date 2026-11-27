import base64,asyncio
from playwright.async_api import async_playwright
R='/home/claude/kniga2-posobie/'
F=lambda f:'data:font/woff2;base64,'+base64.b64encode(open(R+'tools/fonts/'+f,'rb').read()).decode()
I=lambda f:'data:image/jpeg;base64,'+base64.b64encode(open(R+'lessons/urok8/img/'+f,'rb').read()).decode()
CSS=f'''
@font-face{{font-family:Lal;src:url({F('lalezar-arabic-400-normal.woff2')})}}
@font-face{{font-family:Nas;font-weight:700;src:url({F('noto-naskh-arabic-arabic-700-normal.woff2')})}}
@font-face{{font-family:Nu;font-weight:900;src:url({F('nunito-cyrillic-900-normal.woff2')});unicode-range:U+0400-04FF}}
@font-face{{font-family:Nu;font-weight:900;src:url({F('nunito-latin-900-normal.woff2')});unicode-range:U+0000-03FF,U+2000-27FF}}
@font-face{{font-family:Nu;font-weight:800;src:url({F('nunito-cyrillic-800-normal.woff2')});unicode-range:U+0400-04FF}}
@font-face{{font-family:Nu;font-weight:800;src:url({F('nunito-latin-800-normal.woff2')});unicode-range:U+0000-03FF,U+2000-27FF}}
*{{box-sizing:border-box;margin:0;padding:0}}
:root{{--u:#8f9a2f;--uL:#f3f5df;--ink:#24211f;--mut:#8a837c;--line:#ece7df;--paper:#fffdf8;--bg:#f1eee8;--g:#2e8b57;--b:#1f6fb5}}
body{{background:var(--bg);font-family:Nu;font-weight:800;color:var(--ink)}}
.ar{{font-family:Nas;font-weight:700;direction:rtl}}
.ic{{width:40px;height:40px;border-radius:50%;display:inline-grid;place-items:center;flex:none}}
.play{{background:var(--u);color:#fff;font-size:15px}}
.ru{{border:2px solid var(--line);background:#fff;color:var(--mut);font:900 13px Nu}}
'''
D=[('فَضْل','g','مَتَى تَزُورُ عَمَّكَ؟',None),('مُحَمَّد','b','يَوْمَ السَّبْتِ، وَيَوْمَ الْإِثْنَيْنِ.',None),
('فَضْل','g','وَمَتَى تَزُورُ جَدَّكَ؟','А когда ты навещаешь дедушку?'),('مُحَمَّد','b','يَوْمَ الْجُمُعَةِ، وَيَوْمَ الْأَحَدِ، وَلَيْلَةَ الثُّلَاثَاءِ.',None),
('فَضْل','g','وَمَتَى تَزُورُ خَالَتَكَ؟',None),('مُحَمَّد','b','يَوْمَ الْخَمِيسِ، وَلَيْلَةَ الْأَرْبِعَاءِ.',None),
('فَضْل','g','وَمَتَى تَزُورُ خَالَكَ؟',None),('مُحَمَّد','b','أَزُورُهُ وَسَطَ الْأُسْبُوعِ.',None)]
lines=''.join(f'''<div class="ln {'on' if i==3 else ''}"><span class="ic play">▶</span><span class="who {c}">{w}</span><span class="ar t {c}">{t}</span><span class="ic ru {'act' if r else ''}">Ру</span>{f'<div class="tr">{r}</div>' if r else ''}</div>''' for i,(w,c,t,r) in enumerate(D))
W=[('sabt','السَّبْتُ'),('ahad','الْأَحَدُ'),('ithnayn','الْإِثْنَيْنِ'),('thulatha','الثُّلَاثَاءُ'),('arbia','الْأَرْبِعَاءُ'),('khamis','الْخَمِيسُ'),('jumua','الْجُمُعَةُ'),('yazur','يَزُورُ'),('khala','خَالَةٌ'),('layla','لَيْلَةٌ'),('wasat','وَسَطٌ'),('usbu','الْأُسْبُوعُ')]
words=''.join(f'<div class="wc {"pl" if k=="khamis" else ""}"><img src="{I("w_"+k+".jpg")}"><span class="ar">{w}</span></div>' for k,w in W)
pages=''.join(f'<span class="pg {c}">{n}</span>' for n,c in [('٧٣','cur'),('٧٤','done'),('٧٥',''),('٧٦',''),('٧٧',''),('٧٨',''),('٧٩',''),('٨٠',''),('٨١','done'),('٨٢','')])
desk=f'''<!doctype html><html><head><meta charset=utf-8><style>{CSS}
body{{width:1440px;height:900px;overflow:hidden}}
.top{{height:64px;background:#fff;border-bottom:1px solid var(--line);display:flex;align-items:center;padding:0 24px;gap:18px;direction:rtl}}
.isl{{width:44px;height:44px;border-radius:14px;background:var(--u);color:#fff;display:grid;place-items:center;font:30px Lal}}
.ttl{{font:32px Lal;color:var(--ink)}}.sub{{font:800 14px Nu;color:var(--mut);direction:ltr}}
.pages{{display:flex;gap:6px;margin-right:auto;direction:rtl}}
.pg{{width:38px;height:38px;border-radius:12px;display:grid;place-items:center;font:700 18px Nas;color:var(--mut);background:var(--bg);position:relative}}
.pg.cur{{background:var(--u);color:#fff}}.pg.done::after{{content:'✓';position:absolute;top:-6px;left:-4px;width:16px;height:16px;border-radius:50%;background:var(--g);color:#fff;font:900 10px Nu;display:grid;place-items:center}}
.mode{{display:flex;background:var(--bg);border-radius:12px;padding:4px;direction:ltr;font:900 14px Nu}}.mode span{{padding:7px 14px;border-radius:9px;color:var(--mut)}}.mode .on{{background:#fff;color:var(--ink);box-shadow:0 1px 3px #0002}}
.tg{{font:900 13px Nu;color:var(--mut);display:flex;align-items:center;gap:8px;direction:ltr}}.sw{{width:38px;height:22px;border-radius:11px;background:#d9d4cc;position:relative}}.sw::after{{content:'';position:absolute;left:3px;top:3px;width:16px;height:16px;border-radius:50%;background:#fff}}
.wrap{{display:flex;gap:22px;padding:22px 28px;height:836px}}
.sheet{{flex:1;background:var(--paper);border-radius:28px;box-shadow:0 2px 0 var(--line),0 12px 30px #0000000d;padding:20px 30px;display:flex;flex-direction:column;gap:10px;position:relative}}
.ex{{display:flex;align-items:center;gap:12px;direction:rtl}}.n{{width:34px;height:34px;border-radius:50%;background:var(--u);color:#fff;display:grid;place-items:center;font:700 19px Nas}}
.ex .ar{{font-size:28px;color:var(--u)}}.ex .hint{{font:800 14px Nu;color:var(--mut);margin-right:auto;direction:ltr}}
.body{{display:flex;gap:24px;direction:rtl}}
.dlg{{flex:1.15;display:flex;flex-direction:column;gap:6px}}
.ln{{display:flex;align-items:center;gap:12px;padding:4px 12px;border-radius:16px;flex-wrap:wrap;direction:rtl}}
.ln.on{{background:var(--uL);box-shadow:inset 0 0 0 2px var(--u)}}
.who{{font:700 17px Nas;width:58px;text-align:center;border-radius:10px;padding:2px 0}}.who.g{{color:var(--g);background:#e8f4ec}}.who.b{{color:var(--b);background:#e6f0fa}}
.t{{font-size:25px;line-height:1.45;flex:1;min-width:0}}.t.g{{color:var(--g)}}.t.b{{color:var(--b)}}
.ln .ru{{margin-right:auto;width:34px;height:34px;opacity:.7}}.ln .ru.act{{background:var(--ink);color:#fff;border-color:var(--ink);opacity:1}}
.tr{{flex-basis:100%;padding-right:110px;font:800 16px Nu;color:var(--mut);direction:ltr;text-align:right}}
.pic{{flex:1;display:flex;flex-direction:column;gap:12px}}
.pic img{{width:100%;border-radius:22px;border:6px solid #fff;box-shadow:0 2px 10px #0001}}
.btns{{display:flex;gap:10px;direction:ltr}}.bt{{flex:1;padding:12px;border-radius:14px;background:#fff;border:2px solid var(--line);font:900 15px Nu;text-align:center}}.bt.m{{background:var(--u);color:#fff;border-color:var(--u)}}
.words{{display:grid;grid-template-columns:repeat(12,1fr);gap:8px;direction:rtl;background:var(--uL);border-radius:20px;padding:10px}}
.wc{{background:#fff;border-radius:14px;padding:6px 4px 4px;text-align:center}}.wc img{{width:100%;aspect-ratio:1;object-fit:contain}}.wc .ar{{font-size:15px;display:block;line-height:1.5}}
.wc.pl{{box-shadow:0 0 0 3px var(--u)}}
.foot{{display:flex;align-items:center;gap:12px;margin-top:auto;direction:ltr}}
.done{{padding:12px 20px;border-radius:14px;background:var(--g);color:#fff;font:900 15px Nu}}
.fix{{padding:12px 20px;border-radius:14px;background:#fff;border:2px solid var(--u);color:var(--u);font:900 15px Nu}}
.nav{{margin-left:auto;display:flex;gap:10px}}.nav span{{width:52px;height:52px;border-radius:50%;background:#fff;border:2px solid var(--line);display:grid;place-items:center;font:900 22px Nu}}
.side{{width:300px;background:#fff;border-radius:24px;padding:18px;display:flex;flex-direction:column;gap:12px;box-shadow:0 2px 0 var(--line)}}
.side h4{{font:900 13px Nu;color:var(--mut);text-transform:uppercase;letter-spacing:.06em}}
.note{{background:#fff8e6;border-radius:14px;padding:12px;font:800 14px/1.45 Nu}}.note b{{font-family:Nas;font-size:17px}}
.cnt{{display:grid;grid-template-columns:1fr auto;gap:6px 10px;font:800 14px Nu;direction:rtl}}.cnt .ar{{font-size:17px}}.cnt i{{font-style:normal;color:var(--u);font-weight:900;direction:ltr}}
.kids{{display:flex;flex-wrap:wrap;gap:6px}}.kids span{{padding:6px 10px;border-radius:10px;background:var(--bg);font:900 13px Nu}}.kids b{{color:#e0a100}}
.lab{{position:absolute;top:-14px;left:30px;background:var(--ink);color:#fff;font:900 13px Nu;padding:5px 12px;border-radius:9px}}
</style></head><body>
<div class="top"><div class="isl">٨</div><div><div class="ttl">الْأَيَّامُ</div><div class="sub">Урок 8 · страница 73 из 82</div></div>
<div class="pages">{pages}</div><div class="tg">Перевод детям <span class="sw"></span></div><div class="mode"><span class="on">Урок</span><span>Домашка</span></div></div>
<div class="wrap"><div class="sheet"><span class="lab">Страница 73 · как в книге</span>
<div class="ex"><span class="n">١</span><span class="ar">اُنْظُرْ وَاسْتَمِعْ وَأَعِدْ</span><span class="hint">▶ на каждой строке · Ру — перевод строки</span></div>
<div class="body"><div class="dlg">{lines}</div><div class="pic"><img src="{I('scene.jpg')}"><div class="btns"><span class="bt m">▶ Весь диалог</span><span class="bt">🙈 Только слушать</span><span class="bt">⏸ Пауза для повтора</span></div></div></div>
<div class="ex"><span class="n">٢</span><span class="ar">كَلِمَاتٌ جَدِيدَةٌ</span><span class="hint">Нажмите на картинку — звучит слово</span></div>
<div class="words">{words}</div>
<div class="foot"><span class="done">✓ Страница пройдена</span><span class="fix">🎯 Закрепить: 3 игры по этой странице</span><span class="nav"><span>‹</span><span>›</span></span></div></div>
<div class="side"><h4>Только учителю</h4><div class="note">Перед первым прослушиванием одна фраза: «Когда услышите <b>يَوْمَ</b> — хлопните».</div><div class="note">Жесты: <b>تَزُورُ</b> — постучать в дверь, <b>لَيْلَةَ</b> — ладонь у щеки.</div>
<h4>Счётчик повторений</h4><div class="cnt"><span class="ar">يَزُورُ</span><i>18 / 40</i><span class="ar">لَيْلَةٌ</span><i>11 / 40</i><span class="ar">الْخَمِيسُ</span><i>9 / 40</i><span class="ar">وَسَطٌ</span><i>6 / 40</i></div>
<h4>Дети · звёзды</h4><div class="kids"><span>Амина <b>★★</b></span><span>Ислам <b>★</b></span><span>Хадиджа <b>★★★</b></span><span>Билал <b>★</b></span><span>Марьям <b>★★</b></span></div></div></div></body></html>'''
T=[('s1','اِسْمِي هِنْدٌ،',None),('s2','أَزُورُ جَدَّتِي فِي بَيْتِهَا يَوْمَ الْخَمِيسِ.','Я навещаю бабушку у неё дома в четверг.'),('s3','أَذْهَبُ أَنَا وَوَالِدِي وَوَالِدَتِي بِالسَّيَّارَةِ.',None),('s4','اِسْمُ جَدَّتِي لَيْلَى.',None)]
tl=''.join(f'<div class="tl {"on" if k=="s2" else ""}"><span class="ic play">▶</span><span class="ar">{t}</span><span class="ic ru {"act" if r else ""}">Ру</span>{f"<div class=tr>{r}</div>" if r else ""}</div>' for k,t,r in T)
Q=[('اِسْمُ وَالِدَةِ هِنْدٍ لَيْلَى.','x'),('تَزُورُ هِنْدٌ جَدَّتَهَا يَوْمَ السَّبْتِ.',''),('لَا تَذْهَبُ هِنْدٌ وَوَالِدُهَا وَوَالِدَتُهَا بِالسَّيَّارَةِ.',''),('اِسْمُ جَدَّةِ هِنْدٍ لَيْلَى.','')]
ql=''.join(f'<div class="q"><span class="ar">{q}</span><span class="tf"><b class="{"ok" if a=="x" else ""}">✗</b><b>✓</b></span></div>' for q,a in Q)
mob=f'''<!doctype html><html><head><meta charset=utf-8><style>{CSS}
body{{width:390px}}
.top{{background:#fff;padding:14px 16px 10px;border-bottom:1px solid var(--line);display:flex;align-items:center;gap:10px;direction:rtl}}
.isl{{width:38px;height:38px;border-radius:12px;background:var(--u);color:#fff;display:grid;place-items:center;font:26px Lal}}
.ttl{{font:26px Lal}}.sub{{font:800 12px Nu;color:var(--mut);direction:ltr}}.pr{{margin-right:auto;font:900 12px Nu;color:var(--g);background:#e8f4ec;padding:6px 10px;border-radius:10px;direction:ltr}}
.bar{{height:5px;background:var(--line)}}.bar i{{display:block;height:5px;width:62%;background:var(--u)}}
.sheet{{margin:12px;background:var(--paper);border-radius:22px;padding:16px;display:flex;flex-direction:column;gap:12px;box-shadow:0 8px 24px #0000000d}}
.pgn{{font:900 12px Nu;color:var(--mut);direction:ltr}}
.ex{{display:flex;align-items:center;gap:8px;direction:rtl}}.n{{width:28px;height:28px;border-radius:50%;background:var(--u);color:#fff;display:grid;place-items:center;font:700 16px Nas}}.ex .ar{{font-size:21px;color:var(--u)}}
.paper{{background:#fff;border-radius:16px;padding:10px 8px;background-image:repeating-linear-gradient(#fff 0 47px,#e9eef6 47px 49px);border:2px solid var(--line)}}
.paper img{{width:100%;border-radius:12px;margin-bottom:6px}}
.tl{{display:flex;align-items:center;gap:8px;padding:5px 4px;border-radius:12px;flex-wrap:wrap;direction:rtl}}.tl.on{{background:var(--uL)}}
.tl .ar{{font-size:21px;line-height:1.7;flex:1}}.tl .ic{{width:32px;height:32px;font-size:12px}}.tl .ru{{opacity:.7}}.tl .ru.act{{background:var(--ink);color:#fff;opacity:1}}
.tr{{flex-basis:100%;font:800 13px Nu;color:var(--mut);direction:ltr;text-align:right;padding:0 40px 4px 0}}
.q{{display:flex;align-items:center;gap:8px;background:#fff;border:2px solid var(--line);border-radius:14px;padding:8px 10px;direction:rtl}}.q .ar{{font-size:18px;flex:1;line-height:1.6}}
.tf{{display:flex;gap:6px}}.tf b{{width:38px;height:38px;border-radius:11px;border:2px solid var(--line);display:grid;place-items:center;font:900 18px Nu;color:var(--mut)}}.tf b.ok{{background:#e8f4ec;border-color:var(--g);color:var(--g)}}
.cta{{display:flex;gap:8px;direction:ltr}}.cta span{{flex:1;text-align:center;padding:12px;border-radius:14px;font:900 14px Nu}}
.c1{{background:var(--u);color:#fff}}.c2{{background:#fff;border:2px solid var(--line)}}
.dots{{display:flex;justify-content:center;gap:6px;padding:4px 0 14px}}.dots i{{width:7px;height:7px;border-radius:50%;background:#d8d2c8}}.dots i.c{{width:22px;border-radius:4px;background:var(--u)}}
</style></head><body>
<div class="top"><div class="isl">٨</div><div><div class="ttl">الْأَيَّامُ</div><div class="sub">Домашка · Амина</div></div><span class="pr">5 из 8 страниц</span></div><div class="bar"><i></i></div>
<div class="sheet"><div class="pgn">Страница 81 · свайп ← →</div>
<div class="ex"><span class="n">٣</span><span class="ar">اِقْرَأْ، وَأَجِبْ بِـ (✓) أَوْ (✗)</span></div>
<div class="paper"><img src="{I('b_chtenie.jpg')}">{tl}</div>
{ql}
<div class="cta"><span class="c2">‹ стр. 80</span><span class="c1">Дальше · стр. 82 ›</span></div></div>
<div class="dots"><i></i><i></i><i></i><i></i><i class="c"></i><i></i><i></i><i></i></div></body></html>'''
open('/home/claude/maket/desk.html','w').write(desk);open('/home/claude/maket/mob.html','w').write(mob)
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        pg=await b.new_page(viewport={'width':1440,'height':900},device_scale_factor=1.5);await pg.goto('file:///home/claude/maket/desk.html');await pg.wait_for_timeout(700);await pg.screenshot(path='/home/claude/maket/d.png')
        pg=await b.new_page(viewport={'width':390,'height':800},device_scale_factor=3);await pg.goto('file:///home/claude/maket/mob.html');await pg.wait_for_timeout(700);await pg.screenshot(path='/home/claude/maket/m.png',full_page=True)
        await b.close()
asyncio.run(main())
