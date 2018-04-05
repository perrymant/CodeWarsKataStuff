def sea_sick(sea):
    waveType = ["~", "_"]
    choppyness = sum([1 for x, y in zip(sea, sea[1:]) if x != y ])
    return "Throw Up" if choppyness > len(sea)*0.2 else "No Problem" 




"""
Thanks to the effects of El Nino this year my holiday snorkelling trip was akin to being in a washing machine... Not fun at all.

Given a string made up of '~' and '_' representing waves and calm respectively, your job is to check whether a person would become seasick.

Remember, only the process of change from wave to calm (and vice versa) will add to the effect (really wave peak to trough but this will do). Find out how many changes in level the string has and if that figure is more than 20% of the string, return "Throw Up", if less, return "No Problem".


sea = ("_~~~~~~~_~__~______~~__~~_~~")

for x, y in zip(sea, sea[1:]):
	print(x, y)

##c = [1 if (x != y) for x,y in zip(sea, sea[1:])]#not working?
sum([1 for x, y in zip(sea, sea[1:]) if x != y ])



def sea_sick(sea):
    return "Throw Up" if (sea.count("~_") + sea.count("_~"))/len(sea) > 0.2 else "No Problem"
    
"""

