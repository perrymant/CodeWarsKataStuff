#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 12:01:40 2018

@author: unityspace

"zaz","zazapulz"

"""



a = "mnopq"
b = "elmlzlwlzlilzlolzlilzlxlzlilzlnlzlilzlolzlilzlolzlilzlolzlilzlplzlilzlolzlilzlqlzlilzlolzlilzlqq"

import itertools
comb = itertools.combinations(b, len(a))
res = ["".join(i) for i in comb]
print(res.count(a))


#def solve(a, b):
#    import itertools
#    comb = itertools.combinations(b, len(a))
#    res = ["".join(i) for i in comb]
#    return res.count(a)