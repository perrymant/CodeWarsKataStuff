#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 22:38:14 2017

@author: unityspace
"""
operation = "T1"
op1 = "T1"
op2 = "T10"
op3 = "T1I"
op4 = "T10I"
op = op4
a = [0, 3, 6]
if op[-1] == "I":
    b = sorted([((12-i)+int(op[1:-1]))%12 for i in a])
else:
    b = sorted([i+int(op[1:]) for i in a])
print(b)