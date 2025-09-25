#Fibonacci series :sequence wher each number is the sum of previous two numbers
# 0,1,1,2,3,5,8,13,21.......
N=int(input("Enter a number : "))
#initialize 2 numbers
a,b=0,1
if N<=0:
    print("please, enter positive integer")
elif N==1:
    print("Fibonacci series : ",a)
else:
    for _ in range(N):
        print("Fibonacci series : ",a)
        a,b=b,a+b