char=input("Enter a character : ").lower()
if char.isalpha():
    if char in "aeiou":
        print(char, " is a vowel")
    else:
        print(char, "is a consonant")
else:
    print("please Enter a alphabetic character")