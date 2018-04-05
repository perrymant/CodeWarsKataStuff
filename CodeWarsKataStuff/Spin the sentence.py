for i in a.split(" "):
    if len(i)>6 or i.count("t")>=2 or i.count("T")>=2:
            print(i[::-1])
    elif len(i) == 2:
            print(i.upper())
    elif len(i) == 1:
            print("0")
    else:
            print(i)



"""
https://www.codewars.com/kata/spin-the-sentence

In this kata you will have to modify a sentence so it meets the following rules:

convert every word backwards that is:

longer than 6 characters
OR

has 2 or more 'T' or 't' in it
convert every word uppercase that is:

exactly 2 characters long
OR

before a comma
convert every word to a "0" that is:

exactly one character long
NOTES:

  Punctuation must not be touched. if a word is 6 characters long, and a "." is behind it,
  it counts as 6 characters so it must not be flipped, but if a word is 7 characters long,
  it must be flipped but the "." must stay at the end of the word.
  -----------------------------------------------------------------------------------------
  Only the first transformation applies to a given word, for example 'companions,'
  will be 'snoinapmoc,' and not 'SNOINAPMOC,'.
  -----------------------------------------------------------------------------------------
  As for special characters like apostrophes or dashes, they count as normal characters, 
  so e.g 'sand-colored' must be transformed to 'deroloc-dnas'.

"""
