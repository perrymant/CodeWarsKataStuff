def palindrome_chain_length(n):
    s = 0
    while True:
        if str(n) == str(n)[::-1]:
            return s
        else:
            n = n+int(str(n)[::-1])
            s += 1
            
