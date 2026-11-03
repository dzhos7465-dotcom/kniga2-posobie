#!/usr/bin/env python3
"""Просмотровая сборка урока ٦ (только чтобы посмотреть до встраивания).
Берёт src/template.html, НЕ меняя его, и в копии в памяти подменяет места, где записан урок ٥,
на данные L6 из lessons/urok6/data.js. Результат: lessons/urok6/preview/urok6_preview.html (в git не кладётся).
Настоящее встраивание (LESSONS[n]) делает главный чат."""
import base64, json, os, glob, re
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
L6D = f'{root}/lessons/urok6'
t = open(f'{root}/src/template.html', encoding='utf-8').read()

def sub(old, new, count=1):
    global t
    n = t.count(old)
    assert n >= 1, 'not found: ' + old[:80]
    if count == 'all':
        t = t.replace(old, new)
    else:
        assert n == count, f'{n}x: ' + old[:80]
        t = t.replace(old, new)

def const(name, expr):
    global t
    i = t.index(f'const {name}=')
    k = i + len(f'const {name}='); depth = 0
    while True:
        c = t[k]
        if c in '[{(': depth += 1
        elif c in ']})': depth -= 1
        elif c == ';' and depth == 0: break
        k += 1
    t = t[:i] + f'const {name}={expr}' + t[k:]

for n in ['LX','BLOB','S1','S1C','S2','S3','S4','SUBW','R1','RCOL','RTEXT','RQ','R4','LET','ACT','ACOL','CONC','GAPS']:
    const(n, 'L6.' + n)
const('PAGE', 'L6.meta.PAGE')
const('PARTS', """[
 {id:'p1',c:'١',tabs:[['dialog','Диалог','53'],['words','Слова','53']]},
 {id:'p2',c:'٢',tabs:[['tree','Картинки · صِلْ','54'],['listen','Слушание','55']]},
 {id:'p3',c:'٣',tabs:[['pairs','Говорим в парах','56–57']]},
 {id:'p4',c:'٤',tabs:[['sounds','Звуки ث / س','58'],['listen2','Слушание','59']]},
 {id:'p5',c:'٥',tabs:[['read','Читаем','60–61'],['letters','Буквы','61']]},
 {id:'p6',c:'نَشَاط',wide:1,tabs:[['activity','Игра со страницы 62','62']]},
 {id:'p7',c:'Игры',wide:1,rus:1,tabs:[['games','Игры','']]},
 {id:'p8',c:'Тест',wide:1,rus:1,tabs:[['test','Мини-тест','']]}]""")

# шапка урока
sub('<span class="n">٥</span></div><div><h1>أُسْرَةُ مُحَمَّدٍ</h1><div class="rus">Урок 5 · страницы 43–52</div>',
    '<span class="n">٦</span></div><div><h1>حِذَائِي</h1><div class="rus">Урок 6 · страницы 53–62 · просмотр</div>')
# слова: 8 вместо 12
sub("['yusalli','yadhhab'].includes(w.k)", "L6.blueWords.includes(w.k)")
sub("wIdx=(wIdx+11)%12", "wIdx=(wIdx+L5.words.length-1)%L5.words.length")
sub("wIdx=(wIdx+1)%12", "wIdx=(wIdx+1)%L5.words.length")
sub("if(i>=12||S.view!=='words')", "if(i>=L5.words.length||S.view!=='words')")
# игры и тест: 8 слов
sub("ks[i%12]", "ks[i%ks.length]", 'all')
sub("for(let i=9;i<12;i++){const same=i!==10;qs.push({type:'tf',img:ks[i],word:same?ks[i]:ks[(i+4)%12],ok:same})}",
    "for(let i=9;i<12;i++){const same=i!==10;const a=ks[i%ks.length];qs.push({type:'tf',img:a,word:same?a:ks[(i+3)%ks.length],ok:same})}")
i = t.index('function makeTest(){'); j = t.index('function test(){')
t = t[:i] + t[i:j].replace('ks[i]', 'ks[i%ks.length]') + t[j:]
sub("const deco=(a,b)=>", "const DECO={jadd:'hidha',akh:'tawil',sadiq:'qasir',amm:'qarib',khal:'baid',bayt:'mata',yadhhab:'yuti'};const deco=(a,b)=>(a=DECO[a]||a,b=DECO[b]||b,")
t = t.replace("const deco=(a,b)=>(a=DECO[a]||a,b=DECO[b]||b,`<img class=\"deco r\" src=\"${A['w_'+a]}\" alt=\"\"><img class=\"deco l\" src=\"${A['w_'+b]}\" alt=\"\">`;",
              "const deco=(a,b)=>(a=DECO[a]||a,b=DECO[b]||b,`<img class=\"deco r\" src=\"${A['w_'+a]}\" alt=\"\"><img class=\"deco l\" src=\"${A['w_'+b]}\" alt=\"\">`);")
assert "b=DECO[b]||b,`<img class=\"deco r\" src=\"${A['w_'+a]}\" alt=\"\"><img class=\"deco l\" src=\"${A['w_'+b]}\" alt=\"\">`);" in t
sub("урок ٥", "урок ٦", 'all')
sub("Урок ٥ · أُسْرَةُ مُحَمَّدٍ", "Урок ٦ · حِذَائِي")
sub("(упр. ٢ стр. ٥٠)", "(упр. ٢ стр. ٦٠)")
# пары: пять упражнений
sub("['١','٢','٣','٤'][P.ex]", "['١','٢','٣','٤','٥'][P.ex]")
sub("['١','٢','٣','٤'][i]", "['١','٢','٣','٤','٥'][i]")
# звуки: ث вместо ش только внутри функции sounds()
i = t.index('function sounds(){'); j = t.index('// ================= pairs')
t = t[:i] + t[i:j].replace('ش', 'ث') + t[j:]
# подсказки урока ٥ из шаблона не накладываем
sub("Object.assign(NOTES,{", "Object.assign({},{")
# часть ٢: вместо дерева семьи — «Соедини» (стр. ٥٤) и «Правда или нет?» по сцене
tree6 = r"""
let T6={mode:'m1',i:0,ans:null};
function tree(){
 const M=L6.MATCH1.items,TFL=L6.TF;let body='';const list=T6.mode==='m1'?M:TFL;const q=list[T6.i];
 if(T6.mode==='m1'){const [w,a,b,key]=q;
  body=`<div class="say"><div class="bubble q">${W(w).w}</div></div><div class="opts n2">${[['أ',a,'a'],['ب',b,'b']].map(([l,k,s])=>`<button class="op ${T6.ans===s?(s===key?'good':'bad'):(T6.ans&&s===key?'good':'')}" data-m="${s}"><span class="tag">${l}</span><img src="${PIC(k)}" alt=""></button>`).join('')}</div>`}
 else body=`<div class="say"><div class="bubble q">${q.line}</div>${T6.ans?`<div class="bubble r">${q.fix}</div>`:`<div class="tf"><button id="ty">👍</button><button id="tno">👎</button></div>`}</div><div class="pic" style="max-width:520px;margin:0 auto"><img class="zoom" src="${A[q.img]}" alt="" style="width:100%;border-radius:18px"></div>`;
 $('#view').innerHTML=`<div class="hrow">${LAB('١','صِلْ')}<div class="seg"><button id="tw" class="${T6.mode==='m1'?'on':''}">Соедини · стр. ٥٤</button><button id="tt" class="${T6.mode==='tf'?'on':''}">Правда или нет?</button></div><span style="font-weight:900;color:var(--mut)">${T6.i+1} / ${list.length}</span><button class="btn main" id="tn">${I.left}Дальше</button><button class="btn ghost" id="tp">${I.right}</button></div><div class="stage">${body}</div>`;
 $('#tw').onclick=()=>{T6={mode:'m1',i:0,ans:null};tree()};$('#tt').onclick=()=>{T6={mode:'tf',i:0,ans:null};tree()};
 $('#tn').onclick=()=>{T6.i=(T6.i+1)%list.length;T6.ans=null;tree();if(T6.mode==='m1')play('a_'+list[T6.i][0])};$('#tp').onclick=()=>{T6.i=(T6.i+list.length-1)%list.length;T6.ans=null;tree()};
 if(T6.mode==='m1'){$$('[data-m]').forEach(b=>b.onclick=()=>{if(T6.ans)return;T6.ans=b.dataset.m;tone(T6.ans===q[3]);tree()});$('.bubble.q').onclick=()=>play('a_'+q[0])}
 else if(!T6.ans){const h=v=>{tone(v===q.ok);T6.ans=1;tree()};$('#ty').onclick=()=>h(true);$('#tno').onclick=()=>h(false)}
}
"""
i = t.index('function tree(){'); j = t.index('// ================= listening')
t = t[:i] + tree6 + '\n' + t[j:]

# данные: урок ٦ + служебное из урока ٥ (дерево и т.п. не используются)
d6 = open(f'{L6D}/data.js', encoding='utf-8').read()
book = re.search(r'const BOOK=\[.*?\];', open(f'{root}/lessons/urok5/data.js', encoding='utf-8').read(), re.S).group(0)
book = book.replace(",ready:true}", "}").replace("p:'стр. 53–62'}", "p:'стр. 53–62',ready:true}")
data = book + '\n' + d6 + """
const L5={words:L6.words,dialog:L6.dialog,build:L6.build};
const PAIRS=L6.PAIRS;const NOTES=Object.assign({},NOTES6);function femAns(s){return s}
const TREE_W=1,TREE_H=1,TREE={},NAME={},WHO=[];
"""
t = t.replace('/*DATA*/', data)
A = {}
for f in sorted(glob.glob(f'{L6D}/img/*') + glob.glob(f'{L6D}/audio/*')):
    k = os.path.splitext(os.path.basename(f))[0]
    mime = {'.mp3': 'audio/mpeg', '.jpg': 'image/jpeg', '.png': 'image/png'}[os.path.splitext(f)[1]]
    A[k] = f'data:{mime};base64,' + base64.b64encode(open(f, 'rb').read()).decode()
t = t.replace('/*ASSETS*/', 'const A=' + json.dumps(A) + ';')
out = f'{L6D}/preview/urok6_preview.html'
open(out, 'w', encoding='utf-8').write(t)
print(out, round(len(t) / 1e6, 2), 'MB')
