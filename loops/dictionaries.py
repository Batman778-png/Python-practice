#Dictionaries are unordered collections of items. They store data in key-value pairs.
#Keys must be unique and immutable (e.g., strings, numbers, or tuples), while values can be of any type.
## Creating Dictionaries
empty_dict={}
print(type(empty_dict))


student={"name":"Krish","age":32,"grade":24}
print(student)
print(type(student))
o/p: {'name': 'Krish', 'age': 32, 'grade': 24}
<class 'dict'>

# Single key is slways used
student={"name":"Krish","age":32,"name":24}
print(student)
o/p:{'name': 24, 'age': 32}


## accessing Dictionary Elements
student={"name":"Krish","age":32,"grade":'A'}
print(student)
o/p:{'name': 'Krish', 'age': 32, 'grade': 'A'}


## Accessing Dictionary elements
print(student['grade'])
print(student['age'])

## Accessing using get() method
print(student.get('grade'))
print(student.get('last_name'))
print(student.get('last_name',"Not Available"))
o/p:A
32
A
None
Not Available

## Modifying Dicitonary Elements
## Dictionary are mutable,so you can add, update or delete elements
print(student)
o/p:{'name': 'Krish', 'age': 32, 'grade': 'A'}
student["age"]=33  ##update value for the key
print(student)
student["address"]="India" ## added a new key and value
print(student)
o/p:{'name': 'Krish', 'age': 33, 'grade': 'A'}
{'name': 'Krish', 'age': 33, 'grade': 'A', 'address': 'India'}


del student['grade'] ## delete key and value pair
print(student)
o/p:{'name': 'Krish', 'age': 33, 'address': 'India'}


## Dictionary methods
keys=student.keys() ##get all the keys
print(keys)
values=student.values() ##get all values
print(values)

items=student.items() ##get all key value pairs
print(items)
o/p:dict_keys(['name', 'age', 'address'])
dict_values(['Krish', 33, 'India'])
dict_items([('name', 'Krish'), ('age', 33), ('address', 'India')])



## shallow copy
student_copy=student
print(student)
print(student_copy)
o/p:{'name': 'Krish1', 'age': 33, 'address': 'India'}
{'name': 'Krish1', 'age': 33, 'address': 'India'}

student["name"]="Krish2"
print(student)
print(student_copy)
o/p:{'name': 'Krish2', 'age': 33, 'address': 'India'}
{'name': 'Krish2', 'age': 33, 'address': 'India'}

student_copy1=student.copy() ## shallow copy
print(student_copy1)
print(student)
o/p:{'name': 'Krish2', 'age': 33, 'address': 'India'}
{'name': 'Krish2', 'age': 33, 'address': 'India'}

student["name"]="KRish3"
print(student_copy1)
print(student)
o/p:{'name': 'Krish2', 'age': 33, 'address': 'India'}
{'name': 'KRish3', 'age': 33, 'address': 'India'}

### Iterating Over Dictionaries
## You can use loops to iterate over dictionatries, keys,values,or items
## Iterating over keys
for keys in student.keys():
    print(keys)
o/p:
name
age
address

## Iterate over values
for value in student.values():
    print(value)
  o/p:
  KRish3
  33
  India


## Iterate over key value pairs
for key,value in student.items():
    print(f"{key}:{value}")
o/p:
name:KRish3
age:33
address:India

## Nested Disctionaries
students={
    "student1":{"name":"Krish","age":32},
    "student2":{"name":"Peter","age":35}
}
print(students)
o/p:{'student1': {'name': 'Krish', 'age': 32}, 'student2': {'name': 'Peter', 'age': 35}}

## Access nested dictionaries elementss
print(students["student2"]["name"])
print(students["student2"]["age"])
o/p:
Peter
35

students.items()
o/p:dict_items([('student1', {'name': 'Krish', 'age': 32}), ('student2', {'name': 'Peter', 'age': 35})]


## Iterating over nested dictionaries
for student_id,student_info in students.items():
    print(f"{student_id}:{student_info}")
    for key,value in student_info.items():
        print(f"{key}:{value}")
 o/p:
student1:{'name': 'Krish', 'age': 32}
name:Krish
age:32
student2:{'name': 'Peter', 'age': 35}
name:Peter
age:35


## Dictionary Comphrehension
squares={x:x**2 for x in range(5)}
print(squares)
o/p:
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

## Condition dictionary comprehension
evens={x:x**2 for x in range(10) ifx%2==0}
print(even)
o/p:{0: 0, 2: 4, 4: 16, 6: 36, 8: 64}


#practical Example
## USe a dictionary to count he frequency of elements in list
numbers=[1,2,2,3,3,3,3,4,4,4,4]
frequncy={}
for number in numbers:
  if number in frequency:
    frrequency[number]+=1
  else:
    frequency[number]=1
print(frequency)
o/p:{1: 1, 2: 2, 3: 3, 4: 4}


## Merge 2 dictionaries into one
ct1={"a":1,"b":2}
dict2={"b":3,"c":4}
merged_dict={**dict1,**dict2}
print(merged_dict)
o/p:
{'a': 1, 'b': 3, 'c': 4}






