def is_palindrome(s:str) ->bool:
    s=s.casefold() # convert string into lowercase powerful than .lower()
    i,j=0,len(s)-1 # i=pointer that pointer starting point, j= pointer that points end point of the string.
    while i<j: # loops until left pointer is before right pointer
        while i<j and not s[i].isalnum(): # the char includes punctuations and spaces
            i+=1
        while i<j and not s[j].isalnum():
            j-=1
        if s[i]!=s[j]: #comparing char at i and j. if they are not equal returns false
            return False
        else:
            i+=1
            j-=1
    return True
s="preethi"
p="racecar"
text="A man, a plan, a canal : panama"
print("palindrome string :",is_palindrome(s))
print("palindrome string :",is_palindrome(p))
print("palindrome string :",is_palindrome(text))