
##
##def max_rot(n):
##    a = str(n)[1:]+str(n)[0]
##    b = str(a)[0]+str(a)[2:]+str(a)[1]
##    c = str(b)[:2]+str(b)[3:]+str(b)[2]
##    d = str(c)[:3]+str(c)[4:]+str(c)[3]
##    print(a, b, c, d)
##    return(max(int(a), int(b), int(c), int(d), n))
##
##


"""
n = 56789
#a = str(n)[1:]+str(n)[0]#
a = str(n)[:0]+str(n)[1:]+str(n)[0]
b = str(a)[:1]+str(a)[2:]+str(a)[1]
c = str(b)[:2]+str(b)[3:]+str(b)[2]
d = str(c)[:3]+str(c)[4:]+str(c)[3]
return(max(int(a), int(b), int(c), int(d), n))



def max_rot(n):
    s, arr = str(n), [n]
    for i in range(len(s)):
        s = s[:i] + s[i+1:] + s[i]
        arr.append(int(s))
    return max(arr)


    
"""
n = 56789
st = [n]
for i, val in enumerate(str(n)):
    st.append(int(str(st[i])[:i]+str(st[i])[i+1:]+str(st[i])[i]))
    if i == len(str(n))-1:
        break
return max(st)
