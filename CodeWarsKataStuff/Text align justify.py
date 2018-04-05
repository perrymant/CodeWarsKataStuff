text, width, final, space, char_line = '123 45 6', 7, [], 1, 0
lines = text.split(" ")

for i, j in enumerate(lines):
    final.append((i, len(j)))

complete, sum, count, i, char_line_list = [], 0, 0, 0, []

def spaces(n,t):
    spaces = []
    for i in list(range(t, 0, -1)):
        spaces.append(n//i)
        n = n - n//i
    spaces = spaces[::-1] 
    return spaces

while i != len(lines):
    if sum + final[i][1] < 7:
        sum += (final[i][1] + (1*count))
        complete.append(lines[i])
        char_line += final[i][1]
        count += 1
        i += 1
    else:
        complete.append("\n")
        char_line_list.append((char_line, count))
        sum, count, char_line= 0, 0, 0




   

result, c = "", 0
for i,j in enumerate(complete):
    n = width -  char_line_list[i][0]
    t = char_line_list[i][1] - 1
    spaces(n, t)[i]

    c += len(j)
    if j == '\n':
	c = 0
    







#justify('123 45 6', 7), '123 45\n6'
"""
text = '123 45 6'
width = 7
final = []
for i, j in enumerate(text):
    if i != 0 and i % width == 0:
        final.append("\n")
    final.append(j)

lines = "".join(final).split("\n")
print(lines)
"""


"""
for i in lines:
    final.append(i)
    if len(final) >= width:


for i, _ in enumerate(final):
    if sum + final[i][1] + < 7:
	sum += final[i][1]

for i, _ in enumerate(final):
	print(final[i][1])
sum = 0

for i, _ in enumerate(final):
	if sum + final[i][1] + 1* < 7:
		sum += (final[i][1] + count)
		complete.append(lines[i])
	elif :

	
"""
