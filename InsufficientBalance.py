class InsufficientBalance(Exception): #user defined exception
    pass
def withdraw(amount,balance): #defining the function
    if amount>balance:
        raise InsufficientBalance("Invalid:Insufficient balance to withdraw the amount. ") # raising the exception if the "if" cdn is true
    balance-=amount # balance=balance-amount
    return balance
try:
    amount=int(input("Enter the amount to withdraw:")) #user input
    new_balance=withdraw(amount,1500)
    print("Remaining amount:",new_balance)
except InsufficientBalance as e:
    print("Message:",e)
