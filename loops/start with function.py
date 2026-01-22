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









