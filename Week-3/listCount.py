
#count frequency of elements in list using simple loop and dictionary
list=[2,4,3,5,2,4,2,6,8,5,9,10]
print(list)
freq={}
for item in list:
    if item in freq:
        freq[item]+=1
    else:
        freq[item]=1
print(freq)

print("-------------------using collections.counter--------------------")
from collections import Counter
freq=Counter(list)
print(freq)
