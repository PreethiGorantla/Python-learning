try:
    numerator=int(input("enter numerator:"))
    denominator=int(input("enter denominator:"))
    result=numerator/denominator
    print(result)
except ValueError:
    print("Invalid input! enter only integer values")
except ZeroDivisionError:
    print("error: divide by 0 is not allowed")