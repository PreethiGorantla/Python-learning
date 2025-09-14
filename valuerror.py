try:
    num=int(input("Enter a number:"))
    print("you entered",num)
except ValueError:
    print("error:invalid input! enter integer value")