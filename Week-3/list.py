'''List are used store collection of elements in a single variable
List are oredered and mutable and can store different data types together.'''




list=[3,5,6,3,7,8]
print(list)
list.insert(0,2)
print(list)
list.append(9)
print(list)
del list[3]  #delete the element at index 3
print(list)
list.pop(1)  #delete element at index 1
print(list)
list.remove(3)  #it removes the value 3 from the list
print(list)
max=max(list)   # print max element in the list
print(max)
min=min(list)  # print min element in the list
print(min)
sum=sum(list)   #sum the list elements
print(sum)
l3=tuple(list)
print(l3)
print(type(l3))