#!/usr/bin/env python3
"""Сборка пособия: src/template.html + lessons/book.js + lessons/urokN/{data.js,img,audio} -> docs/index.html.
Каждый урок кладёт свои данные в LESSONS[N] (lessons/urokN/data.js).
Картинки и звук вшиваются как data: URI в ASSETS[N] (ключ = имя файла без расширения),
поэтому одинаковые имена у разных уроков (d_0, x3_0, s1_0…) не путаются."""
import base64, json, os, glob, re
root = os.path.dirname(os.path.abspath(__file__))
MIME = {'.mp3': 'audio/mpeg', '.jpg': 'image/jpeg', '.png': 'image/png'}
lessons = sorted((int(re.search(r'urok(\d+)$', d).group(1)), d) for d in glob.glob(f'{root}/lessons/urok*') if os.path.exists(f'{d}/data.js'))
ASSETS, data = {}, ['const LESSONS={};', open(f'{root}/lessons/book.js', encoding='utf-8').read()]
for n, d in lessons:
    A = {}
    for f in sorted(glob.glob(f'{d}/img/*') + glob.glob(f'{d}/audio/*')):
        ext = os.path.splitext(f)[1]
        if ext not in MIME: continue
        A[os.path.splitext(os.path.basename(f))[0]] = f'data:{MIME[ext]};base64,' + base64.b64encode(open(f, 'rb').read()).decode()
    ASSETS[n] = A
    data.append(open(f'{d}/data.js', encoding='utf-8').read())
s = open(f'{root}/src/template.html', encoding='utf-8').read()
s = s.replace('/*DATA*/', '\n'.join(data))
s = s.replace('/*ASSETS*/', 'const ASSETS=' + json.dumps(ASSETS) + ';')
os.makedirs(f'{root}/docs', exist_ok=True)

# страницы-ссылки на домашку с превью (картинки рисует tools/make_previews.js → docs/hw/*.jpg)
SITE = 'https://dzhos7465-dotcom.github.io/kniga2-posobie/'
AR = lambda n: ''.join('٠١٢٣٤٥٦٧٨٩'[int(c)] if c.isdigit() else c for c in str(n))
meta_re = re.compile(r"meta:\{n:'([^']*)',t:'([^']*)'")
hw_re = re.compile(r"\{t:'([^']*)'[^}]*?rq:(?:true|false)\}")
os.makedirs(f'{root}/docs/hw', exist_ok=True)
def hw_page(slug, target, title, desc):
    img = f'{SITE}hw/{slug}.jpg' if os.path.exists(f'{root}/docs/hw/{slug}.jpg') else f'{SITE}hw/book.jpg'
    open(f'{root}/docs/hw/{slug}.html', 'w', encoding='utf-8').write(f'''<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta property="og:type" content="website"><meta property="og:site_name" content="Книга 2 · пособие по урокам">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<meta property="og:image" content="{img}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:url" content="{SITE}hw/{slug}.html"><meta name="twitter:card" content="summary_large_image">
<style>body{{font:18px system-ui;text-align:center;padding:40px;color:#8c2d55}}</style></head>
<body data-go="../{target}"><a href="../{target}">Открыть домашнее задание</a>
<script>var b=document.body;location.replace(b.getAttribute("data-go"))</script></body></html>''')
for n, d in lessons:
    src = open(f'{d}/data.js', encoding='utf-8').read()
    mm = meta_re.search(src); ln, lt = (mm.group(1), mm.group(2)) if mm else (AR(n), '')
    parts = hw_re.findall(src[src.find('HW:['):] if 'HW:[' in src else '')
    for i, t in enumerate(parts):
        hw_page(f'l{n}-{i+1}', f'#l{n}-test-{i+1}', f'Домашка · урок {n} «{lt}» · часть {i+1}', f'{t}. Слушай, соединяй, собирай фразы · около 10 минут.')
    hw_page(f'l{n}', f'#l{n}-test', f'Домашка · урок {n} «{lt}» · весь урок', 'Все слова, фразы и текст урока. Слушай, соединяй, собирай фразы · около 10 минут.')
open(f'{root}/docs/index.html', 'w', encoding='utf-8').write(s)
print('docs/index.html', round(len(s) / 1e6, 2), 'MB, уроки:', ', '.join(str(n) for n, _ in lessons))
