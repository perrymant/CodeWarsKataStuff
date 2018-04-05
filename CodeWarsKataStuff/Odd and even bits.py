numbers =[7,-3,20]
def bits_war(numbers):
    odd, even = "", ""
    for i in numbers: 
        if i%2 == 1:
            odd += bin(i)[2:]
        else:
            even += bin(i)[2:]
    if int(odd, 2) > int(even, 2):
        return "odds win"
    elif int(even, 2) > int(odd, 2):
        return "even win"
    else:
        return "tie"

print(bits_war(numbers))

