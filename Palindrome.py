#by using function
def Palindrome(num):
    s=str(num)
    return s==s[::-1]
print(Palindrome(121))
print(Palindrome(153))


print("----------using user input-------------")
 
Num=int(input("Enter a number : "))
s=str(Num)
if s==s[::-1]:
    print(f"{Num} is a palindrome")
else:
    print(f"{Num} is not a palindrome")