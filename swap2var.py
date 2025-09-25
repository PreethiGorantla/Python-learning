#swapping of 2 variables
#method 1 by add & sub
a=int(input("Enter a :"))
b=int(input("Enter b :"))
a=a+b
b=a-b
a=a-b
print("swap of a,b is: ",a,b)


#method 2 by mul & divide
a=int(input("Enter a :"))
b=int(input("Enter b :"))
a=a*b
b=a//b
a=a//b
print("swap of a,b is: ",a,b)

# method 3 by using functions

def swap(x,y):
    return y,x
a,b=swap(7,8)
print("swap of a,b :",a,b)