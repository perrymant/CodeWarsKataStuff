def how_much_coffee(events):
    a = [i for i in events if i in ['cw','dog','cat','movie', 'CW','DOG','CAT','MOVIE']]
    b = sum([1 if i.islower() else 2 for i in a])
    return 'You need extra sleep' if b > 3 else b


"""

https://www.codewars.com/kata/how-much-coffee-do-you-need/train/python

Everybody know that you passed to much time awake during night time...

Your task here is to define how much coffee you need to stay awake after your night. You will have to complete a function that take an array of events in arguments, according to this list you will return the number of coffee you need to stay awake during day time. Note: If the count exceed 3 please return 'You need extra sleep'.

The list of events can contain the following:

You come here, to solve some kata ('cw').
You have a dog or a cat that just decide to wake up too early ('dog' | 'cat').
You just watch a movie ('movie').
Other events can be present and it will be represent by arbitrary string, just ignore this one.
Each event can be downcase/lowercase, or uppercase. If it is downcase/lowercase you need 1 coffee by events and if it is uppercase you need 2 coffees.


test.describe("Basic Tests")
test.assert_equals(how_much_coffee([]), 0)
test.assert_equals(how_much_coffee(['cw']), 1)
test.assert_equals(how_much_coffee(['CW']), 2)
test.assert_equals(how_much_coffee(['cw','CAT']), 3)
test.assert_equals(how_much_coffee(['cw','CAT','DOG']), 'You need extra sleep')
test.assert_equals(how_much_coffee(['cw','CAT', 'cw=others']), 3)


#
cs={'cw':1,'CW':2,'cat':1,'CAT':2,'dog':1,'DOG':2,'movie':1,'MOVIE':2}

def how_much_coffee(events):
    c=sum(cs.get(e,0) for e in events)
    return 'You need extra sleep' if c>3 else c
    
"""
