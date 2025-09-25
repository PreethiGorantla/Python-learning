# Using string slicing
num=int(input("Enter a number : "))
reverse_num=int(str(num)[::-1])
print("Reversed number is : ", reverse_num)



#Using While loop
num=int(input("Enter a number : "))
reverse_num=0
while num>0:
    digit=num%10 #get last num
    reverse_num=reverse_num*10+digit
    num//=10
print(f"Reverse number is {reverse_num}")