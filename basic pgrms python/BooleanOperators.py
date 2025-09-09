'''boolean operators are
 and ,or,not : 
 AND is used when both conditions are true
 OR is used either 1 condition should be true
 NOT print false if is true'''

condition1="True"
condition2="False"
print(not condition1) # it print false
print(condition1 and condition2) # and is used when both conditions are true
print(condition1 or condition2) #or operator is used 

print("-------------------")
#or operator: atleast one condition should be true ,
print(0 or 1)# it going to return not a false value where 0 is a false so it return 1
print(False or 'heyy') #it return "heyy" because False is a false value but in 'or' operator it return not a false value.
print("hi" or "hello") # it returns "hi" because hi is not a false value.
print([] or "hello") 
print(False or [])

print("---------------------")
#bool condition
done=True
if done:
    print("yes")
else:
    print("no")

#bool conditions
done=False
if done:
    print("yes")
else:
    print("no")
    print(type(done)) # check the type of done 


# except 0 is return any value True
done=0  # HERE the o/p will be "no"
if done:
    print("yes")
else:
    print("no")
    print(type(done))

#now we take any value it may be negative also except 0 then it returns true
done=10  # HERE the o/p will be "yes" ,try here by assigning negative value
if done:
    print("yes")
else:
    print("no")


print("-----------------------------")

book1=True
book2=False
book=any([book1,book2])
print(book) #any is used atleast one is true it returns true

book=all([book1,book2]) # if everything is true then it returns true otherwise false
print(book)

