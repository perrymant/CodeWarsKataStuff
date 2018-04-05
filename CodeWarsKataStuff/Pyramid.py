def pyramid(n):
    pyr = ""
    for i,j in enumerate(range(n, 0, -1)):
        if j == 1:
            pyr = pyr + ("/" + "_"*(i*2) + "\\\n")
        else:
            pyr = pyr +  (" "*(j-1) + "/" + " "*(i*2) + "\\"+ "\n")
    return pyr

'   /\\   \n  /  \\  \n /    \\ \n/______\\\n' should equal
'   /\\\n  /  \\\n /    \\\n/______\\\n'
