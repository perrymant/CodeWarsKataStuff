def black_or_white_key(k):
    bw, x = '010110101101', -4*((k-1)//88)
    return ['black', 'white'][int(bw[(k+x)%12])]


"""
def black_or_white_key(key_press_count):
    return "black" if (key_press_count - 1) % 88 % 12 in [1, 4, 6, 9, 11] else "white"

#
w, b = "white", "black"
keyboard = [w, b, w, w, b, w, b, w, w, b, w, b]

def black_or_white_key(count):
    return keyboard[(count - 1) % 88 % 12]


#

bk={1,4,6,9,11}

def black_or_white_key(k):
    return 'black' if (k-1)%88%12 in bk else 'white'


#





#
