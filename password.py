class weakPassword(Exception):
    "raise this exception when the password is weak"
    pass
def set_password(password):
    if password <str(6):
        raise weakPassword("Your password is too weak.. create strong password")
    if password.isalpha():
        raise weakPassword("The password must contains special characters and numerics")
    print("password set successfully")
try:
    #assword=input("Enter new_password: ")
    set_password("preethi@123")
except weakPassword as e:
    print("error:",e)


