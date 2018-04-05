import re
import operator

def solve_runes(r):
    print(r)
    pattern = re.compile(r"(-)?(\d*)?([\-\+\*])(-)?(\d*)?=(-)?(\d*)?")
    rangeNew = list(range(10))
    [rangeNew.remove(int(i)) for i in re.findall(r"\d", r) if int(i) in rangeNew]
    for i in rangeNew:
        i = str(i)
        a = re.sub(r"\?", i, r)
        #print(a)
        x = int(re.match(pattern, a).group(2))
        x_neg = re.match(pattern, a).group(1)
        x = x*-1 if x_neg == "-" else x
        y = int(re.match(pattern, a).group(5))
        y_neg = re.match(pattern, a).group(4)
        y = y*-1 if y_neg == "-" else y
        if re.search(pattern, a).group(7)[0:2] == '00' :
            continue
        z = int(re.match(pattern, a).group(7))
        z_neg = re.match(pattern, a).group(6)
        z = z*-1 if z_neg == "-" else z
        symbol = re.match(pattern, a).group(3)
        opList = [operator.add(x, y), operator.sub(x, y), operator.mul(x, y)]
        ops = ['+', '-', '*']
        result = opList[ops.index(symbol)]
        if result == z:
            return int(i)
    else:
        return -1

#[print(i, re.match(pattern, a).group(i)) for i in range(1,8)]



"""
def solve_runes(r):
    # Your code here
    pass
    rl = list(r)
    qu = [m.start(0) for m in re.finditer(r"\?", r)]
    op = [m.start(0) for m in re.finditer(r"[\*\+\-]", a)]
    eq = [m.start(0) for m in re.finditer(r"=", r)]
    di = [m.start(0) for m in re.finditer(r"\d", r)]
    op2 = [operator.add(x, y), operator.sub(x, y), operator.mul(x, y)]
    ops = ['+', '-', '*']
    for i in qu:
	rl[i] = str(0)

i = "0"...."9"
a = re.sub(r"\?", i, r)
di= [m.start(0) for m in re.finditer(r"\d", a)]


val = re.split('[\*\+\-=]', a)
ops =op = [m.start(0) for m in re.finditer(r"[\*\+\-]", a)]
"""

===

import re

def solve_runes(runes):
    for d in sorted(set("0123456789") - set(runes)):
        toTest = runes.replace("?",d)
        if re.search(r'([^\d]|\b)0\d+', toTest): continue
        l,r = toTest.split("=")
        if eval(l) == eval(r): return int(d)
    return -1



===

import re


def solve_runes(runes):

    for i in range(10):
        eq = re.sub(r'\?', str(i), runes)
        eq = re.sub(r'=', '==', eq)

        if not re.findall(str(i), runes) and not re.findall(r'\D0+0', eq):
            try:
                if eval(eq):
                    return i
            except SyntaxError:
                continue

    return -1

===

import re


def solve_runes(runes):
    runes = runes.replace('=', '==')
    s = bool(re.search(r'\b0\d', runes.replace('?', '0')))
    for d in map(str, range(s, 10)):
        if d not in runes and eval(runes.replace('?', d)):
            return int(d)
    return -1


===


def solve_runes(runes):
    for c in sorted(set('0123456789') - set(runes)):        
        s = runes.replace('?', c).replace('-', ' - ').replace('+', ' + ').replace('*', ' * ').replace('=', ' == ')
        if not any(e[0] == '0' and e != '0' for e in s.split()) and eval(s): return int(c)
    return -1


===
