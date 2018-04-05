"""

"to" and "too" replaced by  number 2
"for" and "fore" replaced by  number 4
Any remaining double o's should be replaced with zeros (E.g. noob = n00b)
"be" = b,
"are" = r,
"you" = u,
"please" = plz,
"people" = ppl,
"really" = rly,
"have" = haz, and
"know" = no
When replacing words, always maintain case of the first letter unless another rule forces the word to all caps.
The letter "s" should always be replaced by a "z", maintaining case
"LOL" must be added to the beginning of any input string starting with a "w" or "W"
"OMG" must be added to the beginning (after LOL, if applicable,) of a string 32 characters1 or longer
All evenly numbered words2 must be in ALL CAPS (Example: Cake is very delicious. becomes Cake IZ very DELICIOUZ)
If the input string starts with "h" or "H", the entire output string should be in ALL CAPS
Periods ( . ), commas ( , ), and apostrophes ( ' ) are to be removed
3A question mark ( ? ) should have more question marks added to it, equal to the number of words2 in the sentence (Example: Are you a foo? has 4 words, so it would be converted to r U a F00????)
3Similarly, exclamation points ( ! ) should be replaced by a series of alternating exclamation points and the number 1, equal to the number of words2 in the sentence (Example: You are a foo! becomes u R a F00!1!1

"""
https://www.codewars.com/kata/552ec968fcd1975e8100005a/train/python
"""

('Hi, how are you today?'), 'HI HOW R U 2DAY?????'
"""


import re



rule1 = re.compile(r'to+', re.I)
result = rule1.sub('2', a)

rule2 = re.compile(r'fore?', re.I)
result = rule2.sub('4', a)

rule3 = re.compile(r'oo', re.I)
result = rule3.sub('00', a)

rule4 = re.compile(r'\?$', re.I)
result = rule3.sub('00', a)

""" turn dict to regex pattern
rdict = {'oo': '00', 'be':'b', 'are':'r', 'you':'u', 'please':'plz', 'people':'ppl', 'really':'rly','have':'haz', 'know':'no'}
pattern = re.compile('|'.join(rdict.keys()))
"""

rdict = {'oo': '00', 'be':'b', 'are':'r', 'you':'u', 'please':'plz', 'people':'ppl', 'really':'rly','have':'haz', 'know':'no'}
pattern = re.compile('|'.join(rdict.keys()))p
attern.sub(lambda x: rdict[x.group()], a)

rule10 = re.compile(r'^[hH]')
result.upper() if rule1.search(a) else rule1

rep = {".": "", ",": "", "\'": ""}

pattern.sub(lambda m: rep[re.escape(m.group(0))], "(condition1) and --condition2--")
'() and --text--'
result = result.replace(".", "")
