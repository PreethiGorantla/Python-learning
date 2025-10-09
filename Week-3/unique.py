numbers=[2,5,2,4,3,3,5,6,7,2]
unique=set(numbers)
b=list(set(numbers))
print(unique)
print(b)

#another method
unique=sorted(set(numbers))
print(unique)