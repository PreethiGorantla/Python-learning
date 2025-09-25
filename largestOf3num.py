#largest of three numbers
a=int(input("Enter 1st number : "))
b=int(input("Enter 2nd number : "))
c=int(input("Enter 3rd number : "))
print("The largest number of a,b,c: ")
if a>=b and a>=c:
    print("The largest number is:",a)
elif b>=a and b>=c:
    print("The largest number is:",b)
else:
    print("The largest number is:",c)




#method 2
a=int(input("Enter 1st number : "))
b=int(input("Enter 2nd number : "))
c=int(input("Enter 3rd number : "))
Largest= max(a,b,c)
print("largest number is :", Largest)