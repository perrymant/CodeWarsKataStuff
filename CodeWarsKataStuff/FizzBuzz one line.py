for i in range(1, 101): print("Fizz"[(i%3)*4:] + "Buzz"[(i%5)*4:] or i)


"""
for i in range(1, 101): print(i,"\t", "Fizz"[(i%3)*4:] + "Buzz"[(i%5)*4:] or i)
"""
