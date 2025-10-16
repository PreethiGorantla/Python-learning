#a3b2c1 = aaabbc
def expand_string(s:str)->str:
    result=""
    i=0
    while i<len(s):
        ch=s[i] #get character
        i+=1
        count=" " # to collect the digits that represents how many times to repeat the character. 
        #collect all following digits
        while i<len(s) and s[i].isdigit():
            count+=s[i]
            i+=1
            result+=ch*int(count) #repeat character
    return result
print(expand_string("a3b4c1"))