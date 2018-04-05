from random import randrange

def primes(x , y):
    l = [2] # list of prime numbers
    for n in range(3,y+1,2): # iterations over odd numbers
        isprime = True
        for e in l:
            if n % e == 0:
                isprime = False
                break
        if(isprime):
            l.append(n)
    return [e for e in l if e >= x]

def miller_rabin(n, k):
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def backwardsPrime(start, stop):
    n = primes(start, stop+1)
    res = [i for i in n if miller_rabin(int(str(i)[::-1]), 4) and int(str(i)[::-1]) != i]
    print("res=", res)
    return res

print(backwardsPrime(60000, 70000))
