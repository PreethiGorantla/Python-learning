num=int(input("Enter a number :"))
if num <0:
    print("Factorial does not exist for negative numbers")
elif num==0:
    print("Factorial of zero(0) is 1")
else:
    factorial=1
    for i in range(1,num+1):
        factorial*=i
    print(f"Factorial of {num} is {factorial}")
