def count_letters_digits(s):
    letters=0
    digits=0
    for ch in s:
        if ch.isalpha():
            letters+=1
        elif ch.isdigit():
            digits+=1
    return letters,digits
text="helloo how are you, iam 5n 98738427"
print(count_letters_digits(text))