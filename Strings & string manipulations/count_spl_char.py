def count_special_char(text):
    #letters,digits,white spaces are not spl chars
    special_char=[ch for ch in text if not ch.isalnum() and not ch.isspace()]
    return len(special_char),special_char
sentence="hey! hello how @re /you."
char,count=count_special_char(sentence)
print("number of spl chars:",count)
print("spl chars:",char)