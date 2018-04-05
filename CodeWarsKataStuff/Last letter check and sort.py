from collections import defaultdict
import itertools

s = 'man i need a taxi up to ubud'

s = s.split()
dup = [i[-1] for i in s]

#USEFUL: Find duplicates in a list
D = defaultdict(list)
for i, item in enumerate(dup):
    D[item].append(i)
D = {k:v for k,v in D.items() if len(v)>1}

#USEFUL lists the values of a dictionary
list(D.values())


"""
#USEFUL flat list from nested list
for sublist in l:
    for item in sublist:
        flat_list.append(item)

or

>>> a = [[1, 2], [4, 5]]
>>> a[0]+a[1]

"""
IndexDup = list(itertools.chain.from_iterable(list(D.values())))
IndexDupSet = set(list(itertools.chain.from_iterable(list(D.values()))))
IndexAllSet = set(list(range(len(s))))
IndexNot = list(IndexAllSet.difference(IndexDupSet)) # difference


#USEFUL Nested FOR loops as List Comprehension
#lst = [j + k for j in s1 for k in s2]
#or

#lst = [(j, k) for j in s1 for k in s2]
#if you want tuples.

#Like in the question, for j... is the outer loop, for k... is the inner loop.
#

#USEFUL Join two lists

"""

>>> # regular unsorted dictionary
>>> d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}

>>> # dictionary sorted by key
>>> OrderedDict(sorted(d.items(), key=lambda t: t[0]))
OrderedDict([('apple', 4), ('banana', 3), ('orange', 2), ('pear', 1)])

>>> # dictionary sorted by value
>>> OrderedDict(sorted(d.items(), key=lambda t: t[1]))
OrderedDict([('pear', 1), ('orange', 2), ('banana', 3), ('apple', 4)])

>>> # dictionary sorted by length of the key string
>>> OrderedDict(sorted(d.items(), key=lambda t: len(t[0])))
OrderedDict([('pear', 1), ('apple', 4), ('orange', 2), ('banana', 3)])

"""
