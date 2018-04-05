def black_or_white_key(k):
    x = -4*((k-1)//88)
    return ["G#", "A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G"][int((k+x)%12)]
