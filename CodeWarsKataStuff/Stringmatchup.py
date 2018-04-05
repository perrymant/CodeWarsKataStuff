##array1 = ['abc', 'abc', 'xyz', 'cde', 'uvw']
##array2 = ['abc', 'cde', 'uap']
result = []

array1, array2 = ['quick', 'brown', 'fox', 'is', 'quick'], ['quick', 'abc', 'fox']

for i in enumerate(array2):
    result.insert(i[0], array1.count(i[1]))
print(result)



def solve(array1,array2):
    result=[]
    for i in enumerate(array2):
        result.insert(i[0], array1.count(i[1]))
    return result


Test.assert_equals(solve(['abc', 'abc','xyz','abcd','cde'], ['abc', 'cde', 'uap']), [2, 1, 0])
Test.assert_equals(solve(['abc', 'xyz','abc', 'xyz','cde'], ['abc', 'cde', 'xyz']), [2, 1, 2])
Test.assert_equals(solve(['quick', 'brown', 'fox', 'is', 'quick'], ['quick', 'abc', 'fox']), [2, 0, 1])

"""

def solve(a,b):
    return [a.count(e) for e in b]


"""
