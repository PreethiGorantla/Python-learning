char = input("Enter a character : ")
if len(char)==1:
    ascii_value =ord(char)
    print(f"Ascii value of {char} is {ascii_value}")
else:
    print("Enter a single character only.")