#!/usr/bin/env python3
"""«Живая книга»: src/kniga.html + lessons/urokN/{data.js,kniga.js} -> docs/kniga/N.html,
src/glavnaya.html -> docs/kniga/index.html (главная книги).
Отдельно от build.py: старый сайт (docs/index.html, docs/hw) не трогается.
Картинки и звук берутся из docs/a/N/ (их кладёт build.py), адреса с ?h= — как в основном сайте."""
import glob, hashlib, json, os, re, shutil, subprocess
root = os.path.dirname(os.path.abspath(__file__))
os.makedirs(f'{root}/docs/kniga/fonts', exist_ok=True)
for f in glob.glob(f'{root}/tools/fonts/*.woff2'):
    shutil.copy(f, f'{root}/docs/kniga/fonts/')
book = open(f'{root}/lessons/book.js', encoding='utf-8').read()
src = open(f'{root}/src/kniga.html', encoding='utf-8').read()
def assets(d, n):
    A = {}
    for f in sorted(glob.glob(f'{d}/img/*') + glob.glob(f'{d}/audio/*')):
        name = os.path.basename(f)
        A[os.path.splitext(name)[0]] = f'../a/{n}/{name}?h=' + hashlib.md5(open(f, 'rb').read()).hexdigest()[:8]
    return A
KN, SCENE, HWP = {}, {}, {}
for d in sorted(glob.glob(f'{root}/lessons/urok*')):
    n = int(re.search(r'urok(\d+)$', d).group(1))
    if not os.path.exists(f'{d}/data.js'):
        continue
    A = assets(d, n)
    if 'scene' in A: SCENE[n] = A['scene']
    js = "const LESSONS={},KNIGA={};" + book + open(f'{d}/data.js', encoding='utf-8').read()
    if os.path.exists(f'{d}/kniga.js'): js += open(f'{d}/kniga.js', encoding='utf-8').read()
    js += f"console.log(JSON.stringify({{hw:(LESSONS[{n}].HW||[]).map(p=>p.t),pages:KNIGA[{n}]?[...new Set(KNIGA[{n}].spreads.flatMap(s=>s.halves.map(x=>x.p)))]:null}}))"
    info = json.loads(subprocess.run(['node', '-e', js], capture_output=True, text=True, check=True).stdout)
    if info['hw']: HWP[n] = info['hw']
    if not info['pages']:
        continue
    KN[n] = {'pages': info['pages']}
    data = ['const LESSONS={},KNIGA={};', book, open(f'{d}/data.js', encoding='utf-8').read(), open(f'{d}/kniga.js', encoding='utf-8').read(),
            f'const N={n},ASSET=' + json.dumps(A, ensure_ascii=False, separators=(',', ':')) + ';']
    open(f'{root}/docs/kniga/{n}.html', 'w', encoding='utf-8').write(src.replace('/*DATA*/', '\n'.join(data)))
    print(f'docs/kniga/{n}.html')
g = open(f'{root}/src/glavnaya.html', encoding='utf-8').read()
J = lambda o: json.dumps({str(k): v for k, v in o.items()}, ensure_ascii=False, separators=(',', ':'))
g = g.replace('/*DATA*/', book + f'\nconst KN={J(KN)},SCENE={J(SCENE)},HWP={J(HWP)};')
open(f'{root}/docs/kniga/index.html', 'w', encoding='utf-8').write(g)
print('docs/kniga/index.html', list(KN), list(SCENE), list(HWP))
