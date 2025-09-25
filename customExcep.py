class NegativeNumberError(Exception):
    pass
try:
    n=int(input("enter a number:"))
    if n<0:
        raise NegativeNumberError("Negative values are not allowed.")
    print("number is: ",n)
except NegativeNumberError as e:
    print("custom Exception: ",e)
    