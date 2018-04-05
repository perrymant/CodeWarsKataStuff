#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 22:16:27 2017

@author: unityspace
"""

def SumEvenFibonacci(limit):
    a, b, fib,  = 1, 2, []
    while a < limit:
        fib.append(a)
        a, b = b, a+b
    return sum([i for i in fib if i%2==0])