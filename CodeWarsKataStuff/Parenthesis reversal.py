s = "())((("
def solve(s):
    if len(s)%2 == 1:
        return -1
    else:
        count = 0
        front, back = s[:len(s)//2], s[len(s)//2:]
        for i in zip(front, back):
            if i == (")", "("):
                count += 2
            if i == ("(", ")"):
                count += 0
            else:
                count += 1
    return count

print(solve(s))



"""
https://www.codewars.com/kata/simple-reversed-parenthesis/train/python

s = "())((("
def solve(s):
    if len(s)%2 == 1:
        return -1
    else:
        count = 0
        front, back = s[:len(s)//2], s[len(s)//2:]
        for i in zip(front, back):
            if i == (")", "("):
                count += 2
            if i == ("(", ")"):
                count += 0
            else:
                count += 1
    return count

print(solve(s))

"""
