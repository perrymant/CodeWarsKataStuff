a, b = "ESTATE", "DUELED"

    e, f, g, h = [], 0, [], 0
    for i in a:
        if i not in e:
            print(i, "not in")
            e.append(i)
            e.append(f)
            f += 1
        elif i in e:
            print(i, "in")
            e.append(i)
            e.append(e.index(i)//2)
    print(e)


    for i in b:
        if i not in g:
            print(i, "not in")
            g.append(i)
            g.append(h)
            h += 1
        elif i in g:
            print(i, "in")
            g.append(i)
            g.append(g.index(i)//2)
    print(g)


if e[1::2] == g[1::2]:
    return true
else:
    
    




"""

def isomorph(a, b):
    e, f, g, h = [], 0, [], 0

    for i in a:
        if i not in e:
            e.append(i)
            e.append(f)
            f += 1
        elif i in e:
            e.append(i)
            e.append(e.index(i)//2)

    for i in b:
        if i not in g:
            g.append(i)
            g.append(h)
            h += 1
        elif i in g:
            g.append(i)
            g.append(g.index(i)//2)

    return True if e[1::2] == g[1::2] else False

###
def pattern(word):
  for index, letter in enumerate(word):
      word = word.replace(letter, str(index))
  return word
  
def isomorph(a, b):
    return pattern(a) == pattern(b)

###
def isomorph(a, b):
  return [a.index(x) for x in a] == [b.index(y) for y in b]
###


Example of using itemgetter() to retrieve specific fields from a tuple record:

>>>
>>> inventory = [('apple', 3), ('banana', 2), ('pear', 5), ('orange', 1)]
>>> getcount = itemgetter(1)
>>> list(map(getcount, inventory))
[3, 2, 5, 1]
>>> sorted(inventory, key=getcount)
[('orange', 1), ('banana', 2), ('apple', 3), ('pear', 5)]

"""





"""

https://www.codewars.com/kata/check-if-two-words-are-isomorphic-to-each-other/train/python


Two strings a and b are called isomorphic if there is a one to one mapping possible for every character of a to every character of b. And all occurrences of every character in a map to same character in b.

Task

In this kata you will create a function that return True if two given strings are isomorphic to each other, and False otherwise.

Example

True:

CBAABC DEFFED
RAMBUNCTIOUSLY THERMODYNAMICS
False:

AB CC
ABAB CD
"""
