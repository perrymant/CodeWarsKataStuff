p1, p2, sum = [2,2],[1,1], 0
if len(p1) != len(p2):
    print( -1)
else:
    for i in range(len(p1)):
        sum += (p1[i] - p2[i])
print( sum)


def distance(p1, p2):
    sum = 0
    if len(p1) != len(p2):
        return -1
    elif p1 == [] or p2 == []:
        return -1
    else:
        for i in range(len(p1)):
            sum += (p1[i] - p2[i])**2
    return sum **0.5


test.describe("Normal cases")
test.assert_equals(distance([2,2],[1,1]),2**0.5)
test.assert_equals(distance([4],[1]),3)
test.assert_equals(distance([1,1,1],[0,0,0]),3**0.5)
test.assert_equals(distance([2,1,3,1],[2,0,2,-1]),6**0.5)
test.assert_equals(distance([3,2,3],[0,1,1]),14**0.5)

test.describe("Bad input/edge cases")
test.assert_equals(distance([],[]),-1)
test.assert_equals(distance([1],[1,1,1,1,1,1,1,1,1]),-1)

def distance(a, b):
    return sum((i - j) ** 2 for i, j in zip(a, b)) ** 0.5 if len(a) == len(b) and a and b else -1


Test Cases:

import random;
import math;

print(random.random())

test.describe("Normal cases")
test.assert_equals(distance([2,2],[1,1]),2**0.5)
test.assert_equals(distance([4],[1]),3)
test.assert_equals(distance([1,1,1],[0,0,0]),3**0.5)
test.assert_equals(distance([2,1,3,1],[2,0,2,-1]),6**0.5)
test.assert_equals(distance([3,2,3],[0,1,1]),14**0.5)

test.describe("Bad input/Edge cases")
test.assert_equals(distance([],[]),-1)
test.assert_equals(distance([1],[1,1,1,1,1,1,1,1,1]),-1)

def d(p1, p2):
    if len(p1) != len(p2) or len(p1) == 0:
        return -1
        
    if len(p1) == 1:
        return math.fabs(p1[0]-p2[0])
    
    dist = 0
    for i in range(len(p1)):
        dist += (p1[i]-p2[i])**2
    
    return dist**0.5


def randlist(l):
    new_list = []
    for _ in range(l):
        new_list.append(random.random()*100)
    return new_list;
    

test.describe("Random tests")
for _ in range(20):
    rand_length = random.randint(1,9)
    rand = random.random()
    if rand < 0.15:
        test.assert_equals(distance([],randlist(rand_length)),-1)
    elif rand < 0.3:
        rand_length_2 = random.randint(0,rand_length-1)
        test.assert_equals(distance(randlist(rand_length),randlist(rand_length_2)),-1)
    else:
        point1 = randlist(rand_length)
        point2 = randlist(rand_length)
        print("Normal test")
        test.assert_equals(distance(point1,point2),d(point1,point2))
    continue
