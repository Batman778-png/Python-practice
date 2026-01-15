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

#tuple methods
#tuples have 2 method
color=('blue','green','orange','blue')

#count
print(color.count('blue'))  #o/p:2

#index
color=('blue','green','orange','blue')
print(color.index('green'))  #o/p:1

#tuple functions
num=(2,3,4,1)
#len
print(len(num)) #o/p:4

#tuple functions
num=(2,3,4,1,5,7)

#sum
print(sum(num)) #o/p:22
#min and max
print(min(num))#o/p:1
print(max(num))#o/p:7


#sort
num=(7,4,3,1,5,2)
a=sorted(num)
num_sorted=tuple(a)
print(num_sorted) #o/p:[1, 2, 3, 4, 5, 7]

#TUPLE PACK AND UNPACK
a="Madhav"
b=21
c="Engineer"# ye kya krta jo multiple variables he vo pack ke andar

tuple_pack=a,b,c 
print(tuple_pack)

#TUPLE PACK AND UNPACK
a="Madhav"
b=21
c="Engineer"
tuple_pack=a,b,c
name,age,profession=tuple_pack
print(name)
print(age)
print(profession)

#modifying tuple
tuple_num=(10,20,30)
#tuple_num[0] = 100 #error

#how to mutate/modify tuple
list_num=list(tuple_num)
print(list_num) #o/p:[10, 20, 30]


list_num[0]=100
print(list_num)#o/p:[100, 20, 30]











