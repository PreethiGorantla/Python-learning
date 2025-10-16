def check_anagram(s1,s2):
    if len(s1) !=len(s2):
        return False
    freq={}
    for ch in s1:
        freq[ch]=freq.get(ch,0)+1 #return current count(default 0 if not present) and increase by 1.
    #subtract counts using s2
    for ch in s2:
        if ch not in freq:
            return False
        freq[ch]-=1
        if freq[ch]<0:
            return False
    return True
    for values in freq.values():
        if values!=0: #after processing both strings.all char should be 0.if any non-zero value remains then there is a mismatch
            return False
        return True
print(check_anagram("listen","silent"))
print(check_anagram("hello","hellooooo"))
print(check_anagram("earth","heart"))