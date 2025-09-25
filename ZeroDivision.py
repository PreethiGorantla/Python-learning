def spam(divide):
    try:
        return 42/divide
    except ZeroDivisionError:
        print("error: Invalid argument")
print(spam(15))
print(spam(16))
print(spam(0)) # it goes to the except block the gives the msg provided in that except block
print(spam(42))

#example2
def spam(divide):
    return 42/divide
try:
    print(spam(12))
    print(spam(24))
    print(spam(0))
    print(spam(12))
    print(spam(1))
except ZeroDivisionError:
    print("error:invalid argument")


""" the reason print(spam(12)) never executed because once the execution jumps to the except clause,it
does not return to try clause.instead it just continues nrml.
"""