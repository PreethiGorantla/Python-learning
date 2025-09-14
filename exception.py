#by using else and finally 

try:
    num=int(input("enter a positive number: "))
    if num<0:
       raise ValueError("negative numbers are not allowed")
except ValueError as e:
    print("error:",e)
else:
    print("Square of the numbers:",num*num)
finally:
    print("code is executed")