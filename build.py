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
open(f'{root}/docs/index.html', 'w', encoding='utf-8').write(s)
print('docs/index.html', round(len(s) / 1e6, 2), 'MB, уроки:', ', '.join(str(n) for n, _ in lessons))
