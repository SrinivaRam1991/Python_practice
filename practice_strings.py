# Strings
print("Hello")
print('Hello')
a = "Hello"
print(a) # Assign String to a Variable
#Multiline Strings
a = """You can assign a 
multiline string to a variable 
by using three double quotes."""
A = '''
You can assign a multiline string 
to a variable by using three single 
quotes
'''
print("A:",A), print("a:",a)
# Strings are Arrays
a = "Hello, World!"
print(a[1]) # Get the character at position 1
#Looping Through a String
for a in "RamSrinivas":
  print(a)
  # String Length
  a = "RamSrinivas"
print(len(a))
# Check String
a = "Hello Ram Srinivas!"
print("Hello" in a)
if "Hello" in a:
  print("Yes, 'Hello' is present.") # use check string with 'if' statement
  print("hi" not in a) # Check if NOT
  # Slicing
  a = "Ram Srinivas!"
print(a[2:5])
print(a[:5]) # Slice From the Start
print(a[2:]) # Slice From the end
print(a[-5:-2]) # Negative Indexing
print(a.upper()) # Upper Case
print(a.lower()) # Lower Case
print(a.strip()) # Remove Whitespace
print(a.replace("R", "a")) # Replace String
print(a.split(",")) # split() method
b =" ".join(a)
print(b) # join() method
# String Concatenation
x = "Hello"
y = "World"
z = x + y
print(z)

# String Format
age = 30
name = "My name is srinivas, and I am {}"
print(name.format(age))
print(a.isalpha()) # isalpha() method
print(a.isnumeric()) # isnumeric() method
print(a.isalnum()) #isalnum() method

# ordinal
h = 'B'
print(ord(h))

# title()
book_name = "data types in python"
print(book_name.title())


