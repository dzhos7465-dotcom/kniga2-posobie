#!/usr/bin/env python3
"""Сборка пособия: src/template.html + lessons/urokN/{data.js,img,audio} -> docs/index.html.
Картинки и звук вшиваются как data: URI в объект A (ключ = имя файла без расширения).
Пока шаблон рассчитан на один урок (5); при добавлении уроков данные станут LESSONS[n]."""
import base64, json, os, glob
root = os.path.dirname(os.path.abspath(__file__))
A = {}
for f in sorted(glob.glob(f'{root}/lessons/urok5/img/*') + glob.glob(f'{root}/lessons/urok5/audio/*')):
    k = os.path.splitext(os.path.basename(f))[0]
    mime = {'.mp3': 'audio/mpeg', '.jpg': 'image/jpeg', '.png': 'image/png'}[os.path.splitext(f)[1]]
    A[k] = f'data:{mime};base64,' + base64.b64encode(open(f, 'rb').read()).decode()
s = open(f'{root}/src/template.html', encoding='utf-8').read()
s = s.replace('/*DATA*/', open(f'{root}/lessons/urok5/data.js', encoding='utf-8').read())
s = s.replace('/*ASSETS*/', 'const A=' + json.dumps(A) + ';')
os.makedirs(f'{root}/docs', exist_ok=True)
open(f'{root}/docs/index.html', 'w', encoding='utf-8').write(s)
print('docs/index.html', round(len(s) / 1e6, 2), 'MB')
