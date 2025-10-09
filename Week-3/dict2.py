'''list of dictionary means you have a list ([]) where each element is a dictionary'''
students=[{"Name":"preethi","Age":21,"course":"MCA"},
          {"Name":"Hari","Age":22,"course":"B-tech"}]
print(students)
print(students[0]) #returns 1st dictionary
print(students[0]["Name"]) #returns preethi
print(students[1]["Name"]) #returns Hari
#Adding new dictionary to thw list
students.append({"Name":"Khusi","Age":1,"course":"Baby"})
print(students)
#updating a value in dictionary
students[1]["Age"]=21
print(students[1])
#deleting dictionary from the list
del students[2] #removes Khusi record
print(students)
print("---------------------Nested dictionaries-------------")
employees=[{"id": 1, "name": "Preethi", "details": {"dept": "IT", "salary": 50000}},
    {"id": 2, "name": "Ravi", "details": {"dept": "HR", "salary": 45000}},]
print(employees)
print(employees[0]["details"]["salary"])

print("---------------count total elements in nested list---------------------")
def count_elements(ele):
    count=0
    for item in ele:
        if isinstance(item,list): #if element is a list --> recursive call
            count+=count_elements(item)
        else:
            count+=1
    return count
nested_list=[1,[2,4],[5,[8,7,5]],[6,9],10]
print("Total elements:",count_elements(nested_list))
