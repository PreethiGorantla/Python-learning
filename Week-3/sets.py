''' Set is mutable and unordered 
    it does not allows duplicates'''
s1={4,7,2,8,3,2}  # it removes duplicates 2 is printed only once
print(s1)
print(type(s1))
s2={3,2,5,8,9,10}
print(s1.union(s2)) #combines s1 & s2 
print(s1.intersection(s2)) # returns common elements in both sets s1 & s2
print(s1.difference(s2))  # returns the elements that are in 1st set but not in 2nd set. (s1 - s2)
print(s1.symmetric_difference(s2)) #returns the elements that are in either of the sets bot not in both.(A-B)U(B-A).where A is s1 and B is s2.