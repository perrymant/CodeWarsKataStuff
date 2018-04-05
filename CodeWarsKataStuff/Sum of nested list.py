
#str(lst).replace("[", "").replace("]", "")

patt = re.findall("[0-9]", str(lst))
return sum([int(i) for i in patt])




import re
def sum_nested(lst):
    patt = re.findall("[0-9]+", str(lst))
    return sum([int(i) for i in patt])

"""
def sum_nested(lst):
  return sum(sum_nested(x) if isinstance(x,list) else x for x in lst)

  
def func(*args, **kwargs):
    print(args)
    print(kwargs)
    print(locals())

func(1, a=2)

# output:
#   (1,)
#   {'a': 2}
#   {'kwargs': {'a': 2}, 'args': (1,)}

"""
