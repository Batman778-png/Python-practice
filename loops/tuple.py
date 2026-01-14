#2. without paranthesis
tuple1=1,2,3
print(tuple1)
print(type(tuple1))

#tuple constructor
tuple2=tuple((1,5,9))
print(type(tuple2))
print(tuple2)

#craete a single element
a=("a",) #add coma
print(type(a))

#acess tuple-indexing
fruits=('apple','banana','cherry')
print(fruits[0])
#print(fruits[-1]) turned into +
print(fruits[3-1]

#tuple slicing
new_tuple=(10,20,30,40,50)
print(new_tuple[0:3:2])

#concatenate-join tuple
tuple1=(1,2,3)
tuple2=('a','b')
tuple3=tuple1+tuple2
print(tuple3)

#repetative
tuple1=(1,2,3)*4
print(tuple1)
o/p:(1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3)

#tuple iteration
#for loop
fruits=('cherry','banana','mango')
for i in fruits:
    print(i)

#while loop
fruits=('cherry','banana','apple')
i=0
while i<len(fruits):
    print(fruits[i])
    i+=1













