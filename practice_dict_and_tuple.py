# Python Dictionaries
dictionary_p = {"brand": "Ford","model": "eco sport","year": 2002}
print(dictionary_p)
# Dictionary Items
print(dictionary_p["brand"])
# Duplicates not allowed in Dictionaries
dictionary_p1 = {"brand": "Ford","model": "eco sport","year": 2002,"year": 2020}
print(dictionary_p)
# Dictionary Length
print(len(dictionary_p))
# Data types in Dictionaries
dictionary_p2 = {"brand": "Ford","model": "eco sport","year": 2002, "colors" : ["red", "white", "blue"]}  
print(dictionary_p2)
print(type(dictionary_p2)) # print the type() of dict
dictionary_p3 = dict(name = "srinivas", age = 30, country = "india")
print(dictionary_p3)
#Access Dictionary Items
x = dictionary_p["model"]
print(x)
# get() method
x = dictionary_p.get("model"),print(x)
y = dictionary_p3.keys()
print(y) #keys() method 
z = dictionary_p.values()
print(z) # values() method
#items() method 
e = dictionary_p.items()
print(e)
# Check if Key Exists
if "model" in dictionary_p:
  print("Yes, 'model' is dictionary")
  #Change Values
  dictionary_p["year"] = 2018
  print(dictionary_p)
  # Update Dictionary
  dictionary_p2.update({"engine":"1000cc"})
print(dictionary_p2)
# Adding Items to Dict
dictionary_p2["making year"] = "2023"
print(dictionary_p2)
# Removing Items
#pop() method
dictionary_p1.pop("model")
print(dictionary_p1) 
# del keyword
del dictionary_p["model"]
print(dictionary_p)
#clear() method
print(dictionary_p3)
# Loop Through a Dictionary
for i in dictionary_p3:
 print(i)
 print(dictionary_p3[i]) #Print all values in the dictionary, one by one
 # copy() method:
 mydict = dictionary_p3.copy()
print(mydict)
mydict1 = dict(dictionary_p2)
print(mydict1) # Make a copy of a dictionary with the dict() function
# Nested Dictionaries
vehicles = {
  "car" : {
    "brand" : "ford",
    "year" : 2004
  },
  "bike" : {
    "bike brand" : "pulsar",
    "year" : 2007
  },
  "scooty" : {
    "scooty brand" : "activa",
    "year" : 2011
  }
}
print(vehicles)

# Access Items in Nested Dictionaries
print(vehicles["bike"]["bike brand"])

# Tuples
#Creating a Tuple
# Using parentheses
my_tuple = (1, 2, 3)
# Using the tuple() constructor
my_tuple = tuple([1, 2, 3,4])

#Accessing Elements
# Accessing an element using indexing
print(my_tuple[0])  # Output: 1
# Accessing a slice of elements using slicing
print(my_tuple[1:4])  # Output: (2, 3, 4)

#Modifying Elements
my_tuple[0] = 4  # Raises a TypeError: 'tuple' object does not support item assignment

#Tuple Methods
my_tuple1 = (1, 2, 2, 3, 3, 3)
# Using count() method
print(my_tuple1.count(2))  # Output: 2
# Using index() method
print(my_tuple1.index(3))  # Output: 3

#Tuple Packing and Unpacking
# Tuple packing
my_tuple2 = 1, 2, 3
print(my_tuple2)  # Output: (1, 2, 3)
# Tuple unpacking
a, b, c = my_tuple2
print(a, b, c)  # Output: 1 2 3
