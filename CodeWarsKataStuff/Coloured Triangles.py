# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.


R G B G
 B R R
  G R
   B
   
   def triangle(row):
while len(row) > 1: 
    new, RGB = '', {'R','G', 'B'} 
    for i, j in zip(row[:-1], row[1:]):
        if i == j:
            new += i
        else:
            new += (RGB.difference({i, j})).pop()
        row = new
    triangle(new)
return row
"""

row = 'RGBG'
#for i, j in enumerate(start):
#    print(i, j)



def triangle(row):
    for t in range(len(row)-1): 
        new, RGB = '', {'R','G', 'B'} 
        for i, j in zip(row[:-1], row[1:]):
            if i == j:
                new += i
            else:
                new += (RGB.difference({i, j})).pop()
            row = new
    return row