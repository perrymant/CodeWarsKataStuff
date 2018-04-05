def eval_postfix(text):
    s = list()
    plus = None
    for symbol in text:
        if symbol in "0123456789":
            s.append(int(symbol))
        
        elif not s:
            if symbol == "+":
                plus = s.pop() + s.pop()
            elif symbol == "-":
                plus = s.pop() - s.pop()
            elif symbol == "*":
                plus = s.pop() * s.pop()
            elif symbol == "/":
                plus = s.pop() / s.pop()
        if plus is not None:
            s.append(plus)
        else:
             raise Exception("unknown value %s"%symbol)
    return s.pop()
