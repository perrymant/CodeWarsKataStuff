import operator

"""

"56 65 74 100 99 68 86 180 90" ordered by numbers weights becomes:
"100 180 90 56 65 74 68 86 99"


"""
#s = "56 65 74 100 99 68 86 180 90"
s = "103 123 4444 99 2000"
def order_weight(s):
    sList, wNum= s.split(" "), []
    for i in sList:
        wNum.append([sum([int(j) for j in i])])
    _, result = zip(*sorted(zip(wNum, sList), key=operator.itemgetter(0)))
    return " ".join(result)

print(order_weight(s))

# https://stackoverflow.com/questions/9543211/sorting-a-list-in-python-using-the-result-from-sorting-another-list
# Schwartzian_transform
#list_1_sorted, list_2_sorted = zip(*sorted(zip(n, p), key=operator.itemgetter(0)))

