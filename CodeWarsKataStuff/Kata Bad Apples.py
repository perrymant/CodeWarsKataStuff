#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 18:55:01 2018

@author: unityspace
https://www.codewars.com/kata/bad-apples/train/python
"""

#apples = [[1,3],[7,6],[7,2],[1,3],[0,2],[4,5],[0,3],[7,6]]
#apples = [[1,3],[7,6],[7,2],[1,3],[0,2],[4,5],[0,3],[7,6],[0,0],[0,5],[0, 1]]
#apples = [[0,0],[1,0],[0,2],[3,0],[4,0],[0,5],[0,6],[7,0]]
#apples = [[1,3],[7,6],[7,2],[1,3],[0,1],[4,5],[0,3],[7,6]]
apples = [[1, 2], [5, 2], [4, 1], [0, 4], [5, 3], [1, 0], [1, 7], [3, 3], [2, 7], [0, 5], [2, 7], [0, 2], [0, 5], [0, 2]]

#apples = [[0, 0], [0, 0], [0, 1], [0, 0], [0, 0]]
index, res, counter = [], [], 0

for i in apples:
    if i == [0,0]:
        continue
    elif 0 in i:
        index.append((counter, sum(i)))
    else:
        res.append(i)
    counter+=1
print(index, "\n", res)
i1 = [i[0] for i in index]
i2 = [i[1] for i in index]
i1, i2 = i1[::-1], i2[::-1]

#check i1 in loop against loop count
for i in range(len(i2)//2):
    val = i2.pop(), i2.pop()
    res.insert(int(i1.pop()), list(val))


#print(res)

[[1, 2], [5, 2], [4, 1], [0, 4], [5, 3], [1, 0], [1, 7], [3, 3], [2, 7], [0, 5], [2, 7], [0, 2], [0, 5], [0, 2]]
[[1, 2], [5, 2], [4, 1], [4, 1], [5, 3], [5, 2], [1, 7], [3, 3], [2, 7], [5, 2], [2, 7]]
[[1, 2], [5, 2], [4, 1], [4, 1], [5, 3], [1, 7], [3, 3], [2, 7], [5, 2], [2, 7], [5, 2]]