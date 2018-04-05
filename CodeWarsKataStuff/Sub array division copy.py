"""
solve([1,3,4,7,6],9) == true




def solve(arr,n):
    arr.sort()
    ab, ae = 0, len(arr)-1
    while ab < ae:
        test = ae
        ae -= 1
        if n-arr[test] in arr[ab:ae]:
            return True
        
    else:
        return False



def solve(arr,n):
    arr.sort()
    ab, ae = 0, len(arr)-1
    while ab < ae:
        test = ae
        ae -= 1
        if n-arr[test] in arr[ab:ae]:
            return True
    else:
        return False
        
        
        
from itertools import combinations

def solve(arr,n):    
    for i in range(len(arr)+1):
        a = combinations(arr, i)
        for i in a:
            d, r = (divmod(sum(i), n))
            if isinstance(d, int) and r == 0:
                return True
    else:
        return False

"""

from itertools import combinations

def solve(arr,n):    
    for i in range(1, len(arr)+1):
        a = combinations(arr, i)
        for i in a:
            d, r = (divmod(sum(i), n))
            if d>0 and r==0:
                return True
    else:
        return False


"""
from itertools import combinations

def solve(a, n):
    return any(sum(c) % n == 0 for i in range(len(a)) for c in combinations(a, i+1))

===

from itertools import combinations

def solve(arr,n):
    return next(( True for x in range(1, len(arr)+1) for c in combinations(arr, x) if not sum(c)%n), False)

    """
