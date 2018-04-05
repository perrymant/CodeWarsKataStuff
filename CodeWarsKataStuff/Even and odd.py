a = [0,1,2,3, 4, 5]
odd, even = 0, 0
for i in a:
    if not str(i).isdigit():
        pass
    else:
        if i%2 == 0:
            even += 1
        else:
            odd += 1
print( even - odd)


"""
def solve(a):
    return sum(1 if v % 2 == 0 else -1 for v in a if type(v) == int)


def solve(a):
    return sum( isinstance(x, int) and [1, -1][x % 2] for x in a )
"""
