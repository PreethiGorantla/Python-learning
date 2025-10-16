def unique_char(s):
    #first count frequent of each character
    freq={}
    for ch in s:
        freq[ch]=freq.get(ch,0)+1
        # find first char frequency with 1
    for ch in s:
        if freq[ch]==1:
            return ch
    return None
print(unique_char("hello"))
print(unique_char("swizz"))
print(unique_char("prep"))
