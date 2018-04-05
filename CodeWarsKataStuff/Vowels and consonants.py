s = "orudere"
from itertools import permutations
perms = [''.join(p) for p in permutations(s)]
vowel, consonant = "aeiou", "bcdfghjklmnpqrstvwxyz"

sv , sc = sum([s.count(i) for i in vowel]), sum([s.count(i) for i in consonant])
if sv-sc == 0:
    for i in sorted(perms):
        if all (i in vowel for i in i[::2]) and all (i in consonant for i in i[1::2]):
            print(i)
            break
elif -1<= sv-sc <= 1:
    for i in sorted(perms):
        #if sum([1 for x, y in zip(i, i[1:]) if x == y ]) == 0:
        if all (i in vowel for i in i[::2]) and all (i in consonant for i in i[1::2]):
            print(i)
            break
        elif all (i in vowel for i in i[1::2]) and all (i in consonant for i in i[::2]):
            print(i)
            break
else:
    print("failed")


"""   
all (i in vowel for i in s[::2])
all (i in consonant for i in s[1::2])


"""

#alternate = re.compile('[aeiou]?([^aeiou][aeiou])+{'+str(len(s)//2)+'}')


#for i in perms:
#	re.match(alternate, i)

"""

for x, y in zip(vowel, consonant[1:]):
	print(x, y)



	
"""
