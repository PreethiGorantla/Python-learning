#checking whether any permutation(rearrangement) of the given string form a palindrome
def can_form_palindrome(s:str)->bool:
    s=s.replace(" ","").lower()
    freq={} # dictionary to store char frequency
    for ch in s:
        freq[ch]=freq.get(ch,0)+1 # ex:civic, freq={"i"=2,"v"=1,"c"=2 }
        odd_count=sum(1 for count in freq.values() if count%2!=0)
    return odd_count<=1
print(can_form_palindrome("civic"))
print(can_form_palindrome("abab")) 
print(can_form_palindrome("hello"))        
