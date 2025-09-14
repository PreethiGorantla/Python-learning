class InvalidAgeValidator(Exception):  #here we are creating an exception to handle, these are user defined exceptions 
    pass
try:
    age=int(input("Enter your age: ")) #to take input from the user
    if age<18:
        raise InvalidAgeValidator("You are not eligible to vote") #if the age is below 18 it raise thsi exception.
    else:
        print("You are eligible to vote")
except InvalidAgeValidator as e:
    print("Invalid:",e)

