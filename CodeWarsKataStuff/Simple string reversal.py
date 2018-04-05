"""
https://www.codewars.com/kata/simple-string-reversal/train/python

In this Kata, we are going to reverse a string while maintaining spaces.

For example:

solve("our code") = "edo cruo"
-- Normal reversal without spaces is "edocruo". 
-- However, there is a space after the first three characters, hence "edo cruo"

solve("your code rocks") = "skco redo cruoy"
solve("codewars") = "srawedoc"

"your code rocks"
"skco redo cruoy"
 012345678901234
"skcoredocruoy"
 0   4   8 


import re

def solve(s):
    index = [0] + [m.start() for m in re.finditer(' ', s)]
    string = "".join(s[::-1].split())
    res = [string[i:j] for i,j in zip(index, index[1:]+[None])]
    return ' '.join(res)
    
[0] + list(range(len(index)))[:-1]
"""
import re

s, res = 'your code rocks', ''
index =[m.start() for m in re.finditer(' ', s)]
string = "".join(s[::-1].split())
#parts = [string[i:j-k] for i,j, k in zip(index, index[1:]+[None],list(range(len(index))))]
print(' '.join(parts))
res = ''
for i, j in enumerate(string):
    if i in index:
        res += ' '
    else:
        res += j


##def insert_dash(string, index):
##    return string[:index] + ' ' + string[index:]

#print insert_dash("355879ACB6", 5)



function reverse(str){
  return str.split(" ").reverse().join(" ")





len_list = [len(i) for i in stri.split(" ")]
string_rev = "".join(s[::-1].split())
for i in len_list:
    res, string_rev = res + string_rev[:i], string_rev[i:]
    res += ' '
return res[:-1]



def solve(s, res = ''):
    len_list = [len(i) for i in s.split(" ")]
    string_rev = "".join(s[::-1].split())
    for i in len_list:
        res, string_rev = res + string_rev[:i], string_rev[i:]
        res += ' '
    return res[:-1]
