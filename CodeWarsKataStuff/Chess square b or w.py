c, r = 'ABCDEFGH', '12345678'
cell = input("Which chess square? ")
cc, cr = c.index(cell[0]), r.index(cell[1])
print("black") if (int(cc)+int(cr)) % 2 == 0 else print("white")
