import re
def solution(string,markers):
    for i, _ in enumerate(markers):
        mark = markers[i]
        pattern = r"[ ]*" + re.escape(mark) + r".*[^\n]?"
        string = re.sub(pattern, "", string)
    return string
