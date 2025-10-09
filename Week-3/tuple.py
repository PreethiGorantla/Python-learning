'''Tuple are used to store collection of elements in a single variable.
tuple are immutable and ordered.  while tuple are immutable we cannot change or alter the tuple once 
created but we can modify by converting tuple into list.'''
a=(3,5,56,9,2.6,65)
print(a)
print(type(a)) # returns type = tuple
print(len(a))
print(a[3]) # prints the element at index 3
min = min(a)
print(min)
print(max(a))
b=list(a)  # converting tuple to list
print(b)
print(type(b))  #prints type = list
b2=b.insert(2,89) # it insert the value 89 at index 2.
print(b)
