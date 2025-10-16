def compress_string(s:str)-> str:
    if not s: # if s is empty then return " "
        return ""
    result=[] # list to store the compressed part like a3,b2 etc
    current=s[0] #  current stores the 1st character of the string
    count=1      # initially the char is seen once so it count is 1 
    for ch in s[1:]:  
        if ch==current: # it check the ch is our current char then count increment
            count+=1
        else:
            result.append(current if count==1 else f"{current}{count}")
            current=ch  #after stepping into next char.current=ch
            count=1      #again it count that char.how many tyms it has been repeated
    result.append(current if count==1 else f"{current}{count}")
    return "".join(result)
print(compress_string("aaabbyy")) #o/p:a3b2y2
print(compress_string("preethi"))
print(compress_string("Hanvika"))
print(compress_string("abc"))
