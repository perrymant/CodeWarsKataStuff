name = input("Enter your name: ")
while True:   
    if len(name)<3:
        name = input("Error. Enter your name: ")
    elif not name.isalpha():
        name = input("Error. Enter your name: ")
    else:
        break

print("prog")
