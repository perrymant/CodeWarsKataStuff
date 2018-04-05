def distribution_of(golds):
    a, b = [], [] #by dealing with a and b as lists, I was
    #going a`gainst "the input list shall not be mutated "
    #I should have used:
    #a , b, = 0, 0
    #and then kept a tally of the golds for each player
    if golds == None:
        return [0, 0]
    for i in range(len(golds)):
        if i%2 == 0:
            if golds[0] > golds[-1]:
                a.append(golds[0])
                del golds[0]
            elif golds[0] < golds[-1]:
                a.append(golds[-1])
                del golds[-1]
            else:
                a.append(golds[0])
                del golds[0]
        if i%2 == 1:
            if golds[0] > golds[-1]:
                b.append(golds[0])
                del golds[0]
            elif golds[0] < golds[-1]:
                b.append(golds[-1])
                del golds[-1]
            else:
                b.append(golds[0])
                del golds[0]
    
    
    return [sum(a), sum(b)]    


distribution_of([4,7,2,9,5,2])
    
"""

def distribution_of(piles):
    i, gold = False, [0, 0]
    while piles:
        gold[i], piles = (gold[i]+piles[-1], piles[:-1]) if piles[-1] > piles[0] else (gold[i]+piles[0], piles[1:])
        i = not i
    return gold



>>> gold = [-2, 3]
>>> gold[True]
3
>>> gold[False]
-2
>>> list[False, True]<< syntax


https://www.codewars.com/kata/simple-fun-number-334-two-beggars-and-gold/train/python

Task

In the field, two beggars A and B found some gold at the same time. They all wanted the gold, and they decided to use simple rules to distribute gold:

They divided gold into n piles and be in line. 
The amount of each pile and the order of piles all are randomly.

They took turns to take away a pile of gold from the 
far left or the far right.

They always choose the bigger pile. That is to say, 
if the left is 1, the right is 2, then choose to take 2.

If the both sides are equal, take the left pile.
Given an integer array golds, and assume that A always takes first. Please calculate the final amount of gold obtained by A and B. returns a two-element array [amount of A, amount of B].

Example

For golds = [4,2,9,5,2,7], the output should be [14,15].

The pile of most left is 4, 
The pile of most right is 7, 
A choose the largest one -- > take 7

The pile of most left is 4, 
The pile of most right is 2, 
B choose the largest one -- > take 4

The pile of most left is 2, 
The pile of most left is 2, 
A choose the most left one -- > take 2

The pile of most left is 9, 
The pile of most right is 2, 
B choose the largest one -- > take 9

The pile of most left is 5, 
The pile of most left is 2, 
A choose the largest one -- > take 5

Tehn, only 1 pile left, 
B  -- > take 2

A: 7 + 2 + 5 = 14
B: 4 + 9 + 2 = 15
For golds = [10,1000,2,1], the output should be [12,1001].

A take 10
B take 1000
A take 2
B take 1

A: 10 + 2 = 12
B: 1000 + 1 = 1001

"""
