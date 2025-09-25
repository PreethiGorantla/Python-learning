import math
a = int(input("Enter a value: "))
b=int(input("Enter b value: "))
print("GCD of a,b :",math.gcd(a,b))


print("----------------Using Euclidean Algorithm -------------------")
def GCD(a,b):
    while b!=0:
        a,b = b,a%b
    return a
print(GCD(12,16))
