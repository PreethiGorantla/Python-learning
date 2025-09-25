N=int(input("Enter how many numbers : "))
numbers=[]
for i in range(N):
    num=float(input(f"Enter a number {i+1} "))
    numbers.append(num)
average=sum(numbers)/N
print(f"Average of {N} numbers is {average}")
