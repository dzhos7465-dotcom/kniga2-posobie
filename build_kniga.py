#!/usr/bin/env python3
"""Прототип «живой книги»: src/kniga.html + lessons/urokN/{data.js,kniga.js} -> docs/kniga/N.html.
Отдельно от build.py: текущий сайт (docs/index.html, docs/hw) не трогается.
Картинки и звук берутся из docs/a/N/ (их кладёт build.py), адреса с ?h= — как в основном сайте."""
import glob, hashlib, json, os, re, shutil
root = os.path.dirname(os.path.abspath(__file__))
src = open(f'{root}/src/kniga.html', encoding='utf-8').read()
os.makedirs(f'{root}/docs/kniga/fonts', exist_ok=True)
for f in glob.glob(f'{root}/tools/fonts/*.woff2'):
    shutil.copy(f, f'{root}/docs/kniga/fonts/')
for d in sorted(glob.glob(f'{root}/lessons/urok*')):
    if not os.path.exists(f'{d}/kniga.js'):
        continue
    n = int(re.search(r'urok(\d+)$', d).group(1))
    A = {}
    for f in sorted(glob.glob(f'{d}/img/*') + glob.glob(f'{d}/audio/*')):
        name = os.path.basename(f)
        A[os.path.splitext(name)[0]] = f'../a/{n}/{name}?h=' + hashlib.md5(open(f, 'rb').read()).hexdigest()[:8]
    data = ['const LESSONS={},KNIGA={};', open(f'{root}/lessons/book.js', encoding='utf-8').read(),
            open(f'{d}/data.js', encoding='utf-8').read(), open(f'{d}/kniga.js', encoding='utf-8').read(),
            f'const N={n},ASSET=' + json.dumps(A, ensure_ascii=False, separators=(',', ':')) + ';']
    open(f'{root}/docs/kniga/{n}.html', 'w', encoding='utf-8').write(src.replace('/*DATA*/', '\n'.join(data)))
    print(f'docs/kniga/{n}.html')
