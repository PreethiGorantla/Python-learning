# Using string conversion
number=int(input("Enter a number: "))
count=len(str(abs(number)))
print("Digit counts :",count)



#Using While loop
num=int(input("Enter a number: "))
n=abs(num)
count=0
if n==0:
   count=1
while n>0:
   count+=1
   n//=10
print(f"digit counts {count}")