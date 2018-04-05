import re
input = "123 - 3 - 20 - 100"
#input = "18 + 4 * 6"

import re
def calculate(input): 
    print('input= ', input)
    try:
        if " 0* " in input or " *0 " in input:
            return False
        res = re.sub(r'[\b[\-\+\\\*]?0*]', '', input)
        print('res= ', res)
        return eval(res)
        
    except:
        return False
