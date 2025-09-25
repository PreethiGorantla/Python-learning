# A variable created inside the function is called Local Variable..A Local scope can access global variable

#def spam():
 #   eggs=3155
#spam()
#print(eggs)   """This pgrms gives us error because eggs is exits only in local scope created when spam is defined.when \ spam() is called it 
#            destroy the local variable.."""

def spam():
    eggs=3155
    print(eggs)
spam()


"""  If you try to use a local variable in a function before you assign a value 
to it, as in the following program, Python will give you an error."""
#def spam():
#    print(eggs) # ERROR!
#    eggs = 'spam local'
#eggs = 'global'
#spam()