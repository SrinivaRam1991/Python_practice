#Creating a Function
def my_function():
  print("Hello from a function")

  # Calling a Function
def my_function():
  print("Hello from a function")

my_function()

# Arguments
def my_function(fname):
  print(fname + " names")

my_function("srinivas")
my_function("vas")
my_function("srinu")

# Default Parameter Value
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
 
 # Passing a List as an Argument
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

# Arbitrary Arguments, *args
def srinivas(*a):
  print(a)
srinivas(123,45,56)

# Keyword Arguments
def dictionary(**a):
  print(a)
dictionary(name = "srinivas", age = 30)

# Return Values
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

#Add Two Numbers
# function that adds two numbers
def add_numbers(num1, num2):
    sum = num1 + num2
    return sum

# calling function with two values
result = add_numbers(5, 4)

print('Sum: ', result)

# Advanced Functions

lambda : print('Hello World')
#Python lambda Function Declaration
greet = lambda : print('Hello World')
# call the lambda
greet()

# Python lambda Function with an Argument
# lambda that accepts one argument
greet_user = lambda name : print('Hey there,', name)

# lambda call
greet_user('Delilah')

# Python Local Variables
def greet():

    # local variable
    message = 'Hello'
    
    print('Local', message)

greet()

# try to access message variable 
# outside greet() function
print(message)

# Python Global Variables
# declare global variable
message = 'Hello'

def greet():
    # declare local variable
    print('Local', message)

greet()
print('Global', message)

# Python Nonlocal Variables
# outside function 
def outer():
    message = 'local'

    # nested function  
    def inner():

        # declare nonlocal variable
        nonlocal message

        message = 'nonlocal'
        print("inner:", message)

    inner()
    print("outer:", message)

outer()
# Global in Nested Functions
def outer_function():
    num = 20

    def inner_function():
        global num
        num = 25
    
    print("Before calling inner_function(): ", num)
    inner_function()
    print("After calling inner_function(): ", num)

outer_function()
print("Outside both function: ", num)

# Anonymous Functions
 # The map() function:
tup= (5, 7, 22, 97, 54, 62, 77, 23, 73, 61)
newtuple = tuple(map(lambda x: x+3 , tup)) 
print(newtuple)

# The filter() function:
def func(x):
    if x>=3:
        return x
y = filter(func, (1,2,3,4))  
print(y)
print(list(y))

# Lambda within filter() functions:

y = filter(lambda x: (x>=3), (1,2,3,4))
print(list(y))

# The reduce() function:
from functools import reduce
reduce(lambda a,b: a+b,[23,21,45,98])

