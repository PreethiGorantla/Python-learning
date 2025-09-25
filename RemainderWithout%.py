dividend=int(input("Enter divident"))
divisor=int(input("Enter divisor"))
remainder=dividend - (divisor*(dividend//divisor))
print(f"The remainder when {dividend} is divided by {divisor} is {remainder}")