strng = "123456987654"
sz = 6
#return "" if sz <= 0 or sz == ""
def revrot(strng, sz):
    if sz > len(strng):
        return ""
    elif sz <= 0 or sz == "":
        return ""
    else:
        pass

    lo, hi, result = 0, sz, ""
    strng_grp = strng[lo:hi]
    while lo <= len(strng)-sz:
        strng_grp = strng[lo:hi]
        s = sum([int(i)**2 for i in strng_grp])%2
        if s == 0:
            result += strng_grp[::-1]
        else:
            result += (strng_grp[1:] + strng_grp[:1])           
        lo, hi = lo+sz, hi+sz+1
    return result

"""
https://www.codewars.com/kata/reverse-or-rotate/train/python

The input is a string str of digits. Cut the string into chunks (a chunk here is a substring of the initial string) of size sz (ignore the last chunk if its size is less than sz).

If a chunk represents an integer such as the sum of the cubes of its digits is divisible by 2, reverse that chunk; otherwise rotate it to the left by one position. Put together these modified chunks and return the result as a string.

If

sz is <= 0 or if str is empty return ""
sz is greater (>) than the length of str it is impossible to take a chunk of size sz hence return "".
Examples:
revrot("123456987654", 6) --> "234561876549"
revrot("123456987653", 6) --> "234561356789"
revrot("66443875", 4) --> "44668753"
revrot("66443875", 8) --> "64438756"
revrot("664438769", 8) --> "67834466"
revrot("123456779", 8) --> "23456771"
revrot("", 8) --> ""
revrot("123456779", 0) --> "" 
revrot("563000655734469485", 4) --> "0365065073456944"

############

def revrot(s, n, res=""):
    if not s or n < 1 or n > len(s):
        return ""
    
    while len(s) >= n:
        group = s[:n]
        if sum([int(d)**3 for d in group]) % 2 == 0:
            res += group[::-1]
        else:
            res += group[1:] + group[0]
        s = s[n:]
    
    return res


#############


##strng = "123456987654"
##sz = 6
##revrot("563000655734469485", 4) --> "0365065073456944"
strng = "563000655734469485"
sz = 4

if sz > len(strng):
    print("1")
elif sz <= 0 or sz == "":
    print("2")
else:
    pass

lo, hi = 0, sz
result = ""
strng_grp = strng[lo:hi]
while lo <= len(strng)-sz:
    strng_grp = strng[lo:hi]
    print(strng_grp)
    s = sum([int(i)**2 for i in strng_grp])%2
    if s == 0:
        print("3")
        result += strng_grp[::-1]
    else:
        print("4")
        result += (strng_grp[1:] + strng_grp[:1])           
    lo, hi = lo+sz, hi+sz
    print(result)
print(result)


5630 0065 5734 4694 85", 4) -->
0365 0650 7345 6944"
3    3    3    3    



    
"""
