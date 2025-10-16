def alternative_char(s):
    result=" "
    for i,ch in enumerate(s):
        if i%2==0:
            result+=ch.upper()
        else:
            result+=ch.lower()
    return result
text="python programming"
print(alternative_char(text))