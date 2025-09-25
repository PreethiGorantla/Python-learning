
def armstrong(num):
#step 1 : digits count
    temp = num
    digit = 0
    while temp>0:
        digit+=1 
        temp//=10
#step 2 : sum of powers
    temp=num
    total=0
    while temp>0:
        digits=temp%10
        total+=digits**digit
        temp//=10
    return total ==num
print(armstrong(153))
print(armstrong(245))

print("----------------By Taking user input ---------------------------")

Num=int(input("Enter a number : "))
digits=str(Num)
power=len(digits)
total = sum(int(d)**power for d in digits)
if total==Num:
    print(f"{Num} is an Armstrong number")
else:
    print(f"{Num} is not an Armstrong")