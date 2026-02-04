#Definition:
A function is a block of code that performs a specific task.
Functions help in organizing code, reusing code, and improving readability.

#basic sytntax
def function_name(parameters):
    """Docstring"""
    # Function body
    return expression

## why functions?
num=24
if num%2==0:
    print("the number is even")
else:
    print("the number is odd")o/p:this number is even
# so nnow whenever we need to check if it number is odd or even we donot have to write all code just call the function
def even_or_odd(num):
    """This function finds even or odd"""
    if num%2==0:
        print("the number is even")
    else:
        print("the number is odd")

## Call this function
even_or_odd(24) o/p:the number is even

## function with multiple parameters
def add(a,b):
    return a+b

result=add(2,4)
print(result)  o/p:6
    

#default parameters
def greet(name):  
  print(f"Hello {name} Welcome To the paradise")
greet("Devesh")


def greet(name="Guest"):  
    print(f"Hello {name} Welcome To the paradise")

greet("Krish")  #yaha agar name nhi diya to bhi chalega so it wil give guest in name otherwise if we mention name then it will take that in o/p
o/p : Hello Krish Welcome To the paradise

### Variable Length Arguments
## Positional And Keywords arguments
def print_numbers(*Devesh):
  for number in Devesh:
    print(number)
print_numbers(1,2,3,4,5,6,"Devesh")

#keyword Aurguments (kW):it is given by double star
 def print_details(**kwargs):# in kwyword argumengt all the parameter will be in key value pairs
       for key,value in kwargs.items():
          print(f"{key}:{value}")
 print_details(name="Devesh",age="20",country="India")
 o/p:
name:Devesh
age:20
country:India

def print_details(*args,**kwargs):
    for val in args:
        print(f" Positional arument :{val}")
    
    for key,value in kwargs.items():
        print(f"{key}:{value}")
print_details(1,2,3,4,"Krish",name="Krish",age="32",country="India")
o/p:
 Positional arument :1
 Positional arument :2
 Positional arument :3
 Positional arument :4
 Positional arument :Krish
name:Krish
age:32
country:India


#Return statement
### Return statements
def multiply(a,b):
    return a*b

multiply(2,3 ) 
o/p:6

### Return multiple parameters
def multiply(a,b):
    return a*b,a

multiply(2,3)
o/p:(6,2)


#more coding example w function
#examploe 1:Temprature conversion
def convert_temperature(temp,unit):
    if unit=="C":
        return temp *9/5 + 32 
    elif unit=="F":
        return(temp-32)*5/9
    else:
        return None
print(convert_temperature(25,"C"))
print(convert_temperature(77,"F"))

#example 2:Passsword strengh checker
def is__sttrong_password(password):

    if len(password)<8:
        return False
    if not any(char.isdigit() for char in password):


        
## Example 7: Validate Email Address
# Email validation function
def is_valid_email(email):
    """This function checks if the email is valid."""
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

# Calling the function
print(is_valid_email("test@example.com"))  # Output: True
print(is_valid_email("invalid-email"))  # Output: False


What is a lambda function ?????????

A lambda function is a small, one-line function that you use when you don’t want to write a full function.

syntax
lamda argument: expression

ex:
addition=lambda a,b:a+b
type(addition)
print(addition(5,6))

ex:
def even(num):
    if num%2==0:
     return true
even(24)
#using lambda function   
even1=lambda num:num%2==0                           
 even1(12)           


#normal fuction
def addition(x,y,z):
    return x+y+z
addition(12,13,14)
#lamda function
additionl=lambda x,y,z:x+y+Z
addition1=(12,13,14)]


*****MAP FUNCTION- Applies a function to all items in a list. this praticularly useful for transforming data in a list comprehensively

Basic syntax:
map(function, iterable)
function → what you want to do
iterable → list, tuple, etc.
⚠️ map() returns a map object, so we usually convert it to list.


numbers=[1,2,3,4,5,6,7]
list(map(square,numbers))

## lambda function with map
numbers=[1,2,3,4,5,6,7,8]
list(map(lambda x:x*x,numbers))

#map multiple iterable
numbers1=[1,2,3]
numbers2=[4,5,6]
added_numbers=list(map(lambda x,y:x+y,numbers1,numbers2)
print(added_numbers)


# map() to convert a list of strings to integers
words=['apple','banana','cherry']
upper_word=list(map(str.upper,words))
print(upper_word)

def get_name(person):
    return person['name']
people=[
    {'name':'devesh','age':20},
    {'name':'ved','age':20}
]
list(map(get_name,people))

*****FILTER FUNCTION 
filter() is used to select elements from an iterable based on a condition.

filter(function, iterable)

#Basic syntax
function → returns True or False
iterable → list, tuple, etc.
Returns a filter object (iterator)


#basic example
lst=[1,2,3,4,5,6,7,8,9,10,11,12]
list(filter(even,lst))  o/p:[2,3,6,8,10,12]


#filter wirth a lambda function
numbers=[1,2,3,4,5,6,7,8,9]
greater_than_five=list(filter(lambda x:x>5,numbers))


#filter wirth a lambda function and multiple condition
numbers=[1,2,3,4,5,6,7,8,9]
even_and_greater_than_five=list(filter(lambda x:x>5 and x%2==0,numbers))

#filter() to check if the age is greater than 25 in dictionaries
people=[
    {'name':'devesh','age':21},
    {'name':'ved','age':26}
     {'name':'tejas','age':28}
]
def age_greater_than_25(person):
    return person['age']>25
list(filter(age_greater_than_25,people))    
