nums = range(2, 100)
for i in range(2, 10):
    nums = filter(lambda x: x == i or x % i, nums)
print (nums)



def backwardsPrime(start, stop):
    n = [x for x in range(start, stop) if not any(y for y in range(2,1+int(sqrt(x))) if not x%y)]
    res = [i for i in n if miller_rabin(int(str(i)[::-1]), 40) and int(str(i)[::-1]) != i]
    return res
