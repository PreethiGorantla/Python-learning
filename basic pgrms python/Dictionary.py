# Dictionary contains key and values 
"""dictionary is ordered and mutable and no duplicate members"""

students={"name":"preethi","regd_no":"242FD01007","course":"MCA","university":"VFSTR"}
print(students.get("name"))
print(students.values())
print(students.keys())
print(students.get("preethi","Harish"))
print(students)
print(students["regd_no"])
print(type(students))
print(len(students))
print(sorted(students))
