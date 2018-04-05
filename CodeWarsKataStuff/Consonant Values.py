
s = "mischtschenkoana"
import re
list_of_vales, sum = [], 0
b = [a.start() for a in re.finditer(r"[^aeiou]", s)]
for i in b:
    sum += ord(s[i])-96
    if i+1 not in b:
        list_of_vales.append(sum)
        sum = 0
        
print(max(list_of_vales))    


"""

import re

def solve(s):
    return max(sum(ord(c)-96 for c in subs) for subs in re.split('[aeiou]+', s))



    >>> re.split('\W+', 'Words, words, words.')
['Words', 'words', 'words', '']
>>> re.split('(\W+)', 'Words, words, words.')
['Words', ', ', 'words', ', ', 'words', '.', '']
>>> re.split('\W+', 'Words, words, words.', 1)
['Words', 'words, words.']
>>> re.split('[a-f]+', '0a3B9', flags=re.IGNORECASE)
['0', '3', '9']


import re
def solve(s):
    list_of_vales, sum = [], 0
    b = [a.start() for a in re.finditer(r"[^aeiou]", s)]
    for i in b:
        sum += ord(s[i])-96
        if i+1 not in b:
            list_of_vales.append(sum)
            sum = 0
            
    return(max(list_of_vales))


    
list_of_vales, sum = [], 0

b = [a.start() for a in re.finditer(r"[^aeiou]", s)]
for i in b:
    sum += ord(s[i])-96
    if i+1 not in b:
        list_of_vales.append(sum)
        sum = 0
        
print(max(list_of_vales))    

"""


"""#("zodiac"),26)

A consonant is any letter of the alphabet except a, e, i ,o, u. The consonant substrings in the word "zodiacs" are z, d, cs. Assuming a = 1, b = 2 ... z = 26, the values of these substrings are 26 ,4, 22 because z = 26,d = 4,cs=3+19=22. The maximum value of these substrings is 26. Therefore, solve("zodiacs") = 26.

Given a lowercase string that has alphabetic characters only and no spaces, return the highest value of consonant substrings.

import re
s = "mischtschenkoana"
t = "cheese"
list_of_vales = []
sum = 0
##for i in re.finditer(r"[^aeiou]", s):
##    print(i)
#a = re.findall(r"[^aeiou]+", t)
#a = [a.start() for a in re.finditer(r"[^aeiou]+", t)]
b = [a.start() for a in re.finditer(r"[^aeiou]", s)]
for i in b:
    sum += ord(s[i])-96
    if i+1 not in b:
        list_of_vales.append(sum)
        sum = 0
        
print(max(list_of_vales))    

#b = [ord(i)-96 for i in a]

#sum += (ord(i)-96)

"""
