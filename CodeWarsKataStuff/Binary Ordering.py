def sortByBinaryOnes (numList): 
    binary = [str((bin(i)[2:])) for i in numList]
    ones = [i.count("1") for i in binary]
    sorting = sorted(list(zip(ones, numList, binary)))
    sorting.sort(key=lambda k: (k[0], -k[1]), reverse=True)
    numList = [i[1] for i in sorting]
    return numList


sortByBinaryOnes([1,15,5,7,3])



"""

http://www.codewars.com/kata/sort-by-binary-ones/train/python


In this example you need to implement a function that sort a list of integers based on it's binary representation.

The rules are simple:

sort the list based on the amount of 1's in the binary representation of each number.
if two numbers have the same amount of 1's, the shorter string goes first. (ex: "11" goes before "101" when sorting 3 and 5 respectively)
if the amount of 1's is same, lower decimal number goes first. (ex: 21 = "10101" and 25 = "11001", then 21 goes first as is lower)
Examples:

Input: [1,15,5,7,3]
( in binary strings is: ["1", "1111", "101", "111", "11"])
Output: [15, 7, 3, 5, 1]
(and after sortByBinaryOnes is: ["1111", "111", "11", "101", "1"])



def sortByBinaryOnes(numList):
    def key(n):
        s = format(n, 'b')
        return -s.count('1'), len(s), n
    return sorted(numList, key=key)
"""
