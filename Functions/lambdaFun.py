#lamdba functions it's similar to vectorization in numpy(python library)

a=print((lambda x:x*x)(5))

b=print((lambda x,y:x/y)(2,6))

##by using map
nums =[2,3,4,5]
squares=list(map(lambda x:x**2,nums))
print(squares)

##example2 using list comprehension
n=[6,7,8,4]
sq=[x**2 for x in n]
print(sq)