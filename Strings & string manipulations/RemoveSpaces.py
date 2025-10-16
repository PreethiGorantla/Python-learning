import re # regular expression
def remove_whitespaces(s:str)->str:
    return re.sub(r'\s+',' ',s) #'''re.sub(pattern,replacement,string) r'\s+ means regular expression pattern
                                #  /s matches any white spaces char./s+ means one or more whitespace char'''
text="Hello \n welcome to \t python   programming"
print("original text:",repr(text))
print("cleaned:",remove_whitespaces(text))