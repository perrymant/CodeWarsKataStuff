n = 99249557
#a = str(n)[1:]+str(n)[0]#
a = str(n)[:0]+str(n)[1:]+str(n)[0]
b = str(a)[:1]+str(a)[2:]+str(a)[1]
c = str(b)[:2]+str(b)[3:]+str(b)[2]
d = str(c)[:3]+str(c)[4:]+str(c)[3]
print(a, b, c, d)
print((max(int(a), int(b), int(c), int(d), n)))
