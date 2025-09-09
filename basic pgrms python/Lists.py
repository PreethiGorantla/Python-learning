#Lists
""" Lists are used to store multiple items in a single variable
    list are ordered and muttable/changable
    allows duplicate numbers"""

fruits=["apple","banana","orange","pine apple","mango"]
print(fruits)
print(fruits[1])
print(fruits[1:3])
print(type(fruits))
print(len(fruits))

print("---------------------------------------")
print("LIST METHODS")
fruits.append("guava") #adds an elements at the end of the list and extend also used to add an element at end of list
print(fruits)
fruits.insert(2,"promaganate") #insert an element at specified position
print(fruits)
fruits.remove("pine apple") #it removes the specified element from the list
print(fruits)
fruits.pop(1) #pops or removes an element at specified index
print(fruits)
fruits.reverse() #reverse the order of the list
print(fruits) 
fruits.clear() #the list still remains but it has no elements
print(fruits) 

#example
#append adds element at the end
l1=[2,5,6,7,4,7,4,8]
print(l1)
l1.append(10)
print(l1)
l1.append([2,4,5])
print(l1)
#insertion : insert element at specified position
l1.insert(2,25) #[index,element]
print(l1)
l1.count(7) # counts how many times 7 is repeated in the list
print(l1)
print(dir(list)) #returns all the methods available in the list
print(id(l1))
l3=l1
print(l3)
print(id(l3))

for i in l1:
    print(i,end=" ")




for i in range(len(l1)):
    print(i, end =" ")