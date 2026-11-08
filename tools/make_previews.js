// Превью для ссылок на домашку (картинка в WhatsApp / Telegram), 1200×630.
// Запуск: node tools/make_previews.js   → docs/hw/l<N>-<часть>.jpg, docs/hw/l<N>.jpg, docs/hw/book.jpg
// Потом python3 build.py (он пишет страницы docs/hw/*.html с этими картинками).
// Шрифты лежат в tools/fonts (OFL), картинки слов — lessons/urokN/img/w_*.jpg.
const fs = require('fs'), path = require('path');
const { chromium } = require('playwright');
const root = path.resolve(__dirname, '..');
const LESSONS = {};
eval(fs.readFileSync(root + '/lessons/book.js', 'utf8') + ';globalThis.BOOK=BOOK;');
for (const d of fs.readdirSync(root + '/lessons')) {
  const m = d.match(/^urok(\d+)$/); if (!m || !fs.existsSync(`${root}/lessons/${d}/data.js`)) continue;
  eval(fs.readFileSync(`${root}/lessons/${d}/data.js`, 'utf8'));
}
const tpl = fs.readFileSync(root + '/src/template.html', 'utf8');
const PALM = tpl.match(/const PALM=`([^`]*)`/)[1];
const F = f => 'data:font/woff2;base64,' + fs.readFileSync(root + '/tools/fonts/' + f).toString('base64');
const img = (n, k) => { const f = `${root}/lessons/urok${n}/img/w_${k}.jpg`; return fs.existsSync(f) ? 'data:image/jpeg;base64,' + fs.readFileSync(f).toString('base64') : null; };
const AR = n => String(n).replace(/\d/g, d => '٠١٢٣٤٥٦٧٨٩'[d]);

function card({ num, title, sub, chip, note, pics }) {
  return `<!DOCTYPE html><html><head><meta charset="utf-8"><style>
@font-face{font-family:Lalezar;src:url(${F('lalezar-arabic-400-normal.woff2')});unicode-range:U+0600-06FF}
@font-face{font-family:Lalezar;src:url(${F('lalezar-latin-400-normal.woff2')});unicode-range:U+0000-00FF}
@font-face{font-family:Naskh;font-weight:700;src:url(${F('noto-naskh-arabic-arabic-700-normal.woff2')})}
@font-face{font-family:Nunito;font-weight:900;src:url(${F('nunito-cyrillic-900-normal.woff2')});unicode-range:U+0400-04FF}
@font-face{font-family:Nunito;font-weight:900;src:url(${F('nunito-latin-900-normal.woff2')});unicode-range:U+0000-03FF,U+2000-206F}
@font-face{font-family:Nunito;font-weight:800;src:url(${F('nunito-cyrillic-800-normal.woff2')});unicode-range:U+0400-04FF}
@font-face{font-family:Nunito;font-weight:800;src:url(${F('nunito-latin-800-normal.woff2')});unicode-range:U+0000-03FF,U+2000-206F}
*{box-sizing:border-box;margin:0}
body{width:1200px;height:630px;overflow:hidden;background:radial-gradient(circle at 85% 0%,#c85a86 0,#b84773 35%,#8c2d55 100%);font-family:Nunito;position:relative}
.dots{position:absolute;inset:0;background-image:radial-gradient(rgba(255,255,255,.09) 2px,transparent 2px);background-size:34px 34px}
.top{position:absolute;top:34px;right:56px;left:56px;display:flex;flex-direction:row-reverse;align-items:center;gap:30px}
.island{position:relative;width:190px;height:150px;flex:none}
.sand{position:absolute;bottom:0;left:8px;right:0;height:40px;border-radius:50%;background:#f4c86a;box-shadow:inset 0 -7px 0 rgba(0,0,0,.08)}
.island svg{position:absolute;left:6px;bottom:22px;width:104px;height:130px}
.num{position:absolute;right:8px;bottom:6px;font:150px/1 Lalezar;color:#fff;-webkit-text-stroke:9px #8c2d55;paint-order:stroke fill}
.tt{text-align:right;color:#fff;flex:1}
h1{font:700 92px/1.25 Naskh;direction:rtl;text-shadow:0 4px 0 rgba(0,0,0,.15)}
.sub{font:900 34px/1.2 Nunito;color:#ffe2ee;margin-top:2px}
.panel{position:absolute;left:44px;right:44px;bottom:40px;height:300px;background:#fff6dc;border-radius:40px;box-shadow:0 10px 0 rgba(0,0,0,.12);display:flex;flex-direction:row-reverse;align-items:center;gap:26px;padding:0 34px}
.txt{flex:1;text-align:right}
.chip{display:inline-block;background:#b84773;color:#fff;font:900 36px/1.2 Nunito;padding:12px 26px;border-radius:999px}
.note{font:800 26px/1.4 Nunito;white-space:nowrap;color:#7c6f80;margin-top:16px}
.pics{display:flex;gap:16px}
.pics div{width:156px;height:190px;background:#fff;border-radius:26px;border:4px solid #fbe7ef;display:grid;place-items:center;overflow:hidden}
.pics img{max-width:142px;max-height:176px;object-fit:contain}
</style></head><body><div class="dots"></div>
<div class="top"><div class="island"><div class="sand"></div>${PALM}<span class="num">${num}</span></div>
<div class="tt"><h1>${title}</h1><div class="sub">${sub}</div></div></div>
<div class="panel"><div class="txt"><span class="chip">${chip}</span><div class="note">${note}</div></div>
<div class="pics">${pics.filter(Boolean).slice(0, 3).map(s => `<div><img src="${s}"></div>`).join('')}</div></div>
</body></html>`;
}

(async () => {
  const out = root + '/docs/hw'; fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1200, height: 630 } });
  const shot = async (html, name) => { await p.setContent(html, { waitUntil: 'load' }); await p.evaluate(async () => { await document.fonts.ready; const bad=[...document.fonts].filter(f=>f.status==='error'); if(bad.length) throw new Error('шрифт не загрузился'); }); await p.waitForTimeout(150);
    await p.screenshot({ path: `${out}/${name}.jpg`, type: 'jpeg', quality: 86 }); console.log('docs/hw/' + name + '.jpg'); };
  for (const n of Object.keys(LESSONS).map(Number).sort((a, b) => a - b)) {
    const L = LESSONS[n]; const all = L.words.map(w => w.k);
    const parts = [...(L.HW || []).map((h, i) => ({ id: `l${n}-${i + 1}`, chip: `Часть ${AR(i + 1)}`, note: h.t + '<br>Слушай, соединяй, собирай · 10 минут', words: h.words || all })),
                   { id: `l${n}`, chip: 'Весь урок', note: 'Все слова, фразы и текст урока<br>Слушай, соединяй, собирай · 10 минут', words: all }];
    for (const [i, pt] of parts.entries()) {
      const ks = pt.words.slice(i * 3 % Math.max(1, pt.words.length - 2)).concat(pt.words).slice(0, 3);
      await shot(card({ num: L.meta.n, title: L.meta.t, sub: `Урок ${n} · домашнее задание`, chip: pt.chip, note: pt.note, pics: ks.map(k => img(n, k)) }), pt.id);
    }
  }
  const ns = Object.keys(LESSONS).map(Number);
  await shot(card({ num: '٢', title: 'العربية بين يدي أولادنا', sub: 'Книга 2 · пособие по урокам', chip: 'Уроки ' + ns.map(AR).join(' и '),
    note: 'Диалоги с голосом диктора, слова, игры и тесты', pics: ns.map(n => img(n, LESSONS[n].words[0].k)).concat(img(ns[ns.length - 1], LESSONS[ns[ns.length - 1]].words[4].k)) }), 'book');
  await b.close();
})();
