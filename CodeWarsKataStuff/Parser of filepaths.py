import re
result = []
rws = re.compile(r'(\d+)-(\d+):(\d+)') #range with step
ran = re.compile(r'(\d+)-(\d+)') #range
sin = re.compile(r'\d+') #single
for i, j in enumerate(s.split(",")):
    if bool(re.findall(rws, j)) == True: #range with step
        a = int(re.search(rws, j).group(1))
        b = int(re.search(rws, j).group(2))
        c = int(re.search(rws, j).group(3))
        result += list(range(a, b, c))
    elif bool(re.findall(r"\d+-\d+", j)) == True: #range
        a = int(re.search(ran, j).group(1))
        b = int(re.search(ran, j).group(2))
        result += list(range(a, b))       
    elif bool(re.search(r"\d+", j).group()) == True:  #single
        a = int(re.search(sin, j).group())
        result += [a]

print(result.sort())



'''

>>> "AB-CD-EF".partition('-')
('AB', '-', 'CD-EF')
>>> "AB-CD-EF".partition(' ')
('AB-CD-EF', '', '')
>>> "AB-CD-EF".partition('D')
('AB-C', 'D', '-EF')


>>> "image.png".partition('.') # this example breaks image file-path into its components
('image', '.', 'png')

def range_parser(string):
    res = []
    for range_ in string.split(','):
        first_last, _, step = range_.partition(':')
        first, _, last = first_last.partition('-')
        res += range(int(first), int(last or first) + 1, int(step or 1))
    return res



import re

def range_parser(s):
    return [x for r in re.split(r', *', s)
              for start,end,step in re.findall(r'(\d+)-?(\d*):?(\d*)',r) 
              for x in range(int(start), int(end or start)+1, int(step or '1'))]

              
