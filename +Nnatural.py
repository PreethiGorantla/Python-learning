#sum of N natural numbers
N=int(input("Enter a number: "))
if N<0:
    print("please enter positive number")
else:
    total=N*(N+1)//2
    print(f"Sum of (N) natural numbers is {total}")