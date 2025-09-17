#Global variables are declared outside the function
def spam():
     global eggs
     eggs = 'spam'
eggs = 'global'
spam()
print(eggs) # prints spam 


""" There are four rules to tell whether a variable is in a local scope or 
global scope:
 1. If a variable is being used in the global scope (that is, outside of all 
functions), then it is always a global variable.
 2. If there is a global statement for that variable in a function, it is a global 
variable.
 3. Otherwise, if the variable is used in an assignment statement in the 
function, it is a local variable.
 4. But if the variable is not used in an assignment statement, it is a global 
variable."""

def spam():
    global eggs
    eggs = 'spam' # this is the global
def bacon():
    eggs = 'bacon' # this is a local

def ham():
    print(eggs) # this is the global
eggs = 42 # this is the global
spam()
print(eggs)