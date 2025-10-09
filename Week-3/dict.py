''' Dictionary are in the form of keys:values.these dictionaries are unordered and mutable
doesn't allows duplicates.'''
df={"Name":"preethi","course":"MCA","place":"Hyd","Age":21}
print(df)
print(type(df))
print(df.keys()) 
print(df.values())
print(df["Name"])  #returns preethi
df["Name"]="Preethi","Hari"
print(df)
#update Age
df["Age"]=21,22
print(df)
df.update({"course":"AI"})
print(df)
#remove specific key
df.pop("place")
print(df)
del df["course"]
print(df)
#clear entire dictionary
df.clear()
print(df)
print("------------merge-----------")
d1={"Name":"preethi","course":"MCA","place":"Hyd"}
d2={"Age":[21,22]}
merge={**d1,**d2} #using dict unpacking **
print(merge)
merged=d1|d2
print(merged)
print("---------------count frequency of characters in string--------------------")
#using collections.counter
from collections import Counter
text="programming"
freq=Counter(text)
print(freq)