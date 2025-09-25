# sets are colletion of elements written in "{ }". does not contains any duplicate values if duplicate values present then it removes duplicates it won't give any error.
s1={2,5,3,6,2,4,5,8,10}
print(s1)
print(type(s1))
#add an element into set
s1.add(20)
print(s1)
#s1.add({2,4,5}) # returns an error
print(s1)
s1.add((12,13,14)) 
print(s1)

#update : adds multiple elements at a time
s1.update((19,18,36))
print(s1)

#methods
s1.discard(3) #removes 3 from the set
print(s1)
s2={3,5,6,3,9}
print(s1.intersection(s2))
print(s1.difference(s2))
print(s2.difference(s1))
print(type(s2))