
words = "sort the inner content in descending order"
result = []
for w in words.split():
    if len(w)>3:
        result.append(w[0]+''.join(sorted(w[1:-1], reverse=True))+w[-1])
    else:
        result.append(w)
        
