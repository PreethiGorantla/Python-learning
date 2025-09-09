#comments
""" tuple is used to store multiple items in asingle variable
    tuple are ordered and immutable/unchangable
    allows duplicate numbers
    # immutable means we cannot change,add,remove the items after tuple has been created
    """

elements=("a","b","c")
print(elements)
print(type(elements))
print(elements[2]) #can also access the element with specified index

""" a tuple may contain different data types"""

languages=("python",34,"java",True,"abc")
print(languages)

""" as tuple are immutable we cannot change ,add,remove for this we can convert tuple intlo list
than we can add,remove and then again convert that list into tuple"""

x=("apple","banana","orange")
print(type(x))
y=list(x) # converting tuple into a list
print(y)
y[1]="kiwi" 
y.append("mango") # add mango 
y.remove("apple") #removes apple from the list
print(y)
print(y) # here it is a list 
x=tuple(y) # converting list into tuple
print(x) 


for i in x:
    print(i,end=" ")
