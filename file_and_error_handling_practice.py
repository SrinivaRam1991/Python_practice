# File Handling Practice:
# Opening a file in write mode
file = open("example.txt", "w")

# Writing to the file
file.write("Hello, World!")

# Closing the file
file.close()

# Reading a file line by line
for line in file:
    print(line)

# Opening a file in read mode
file = open("example.txt", "r")


# Appending to a file
# Opening a file in append mode
file = open("example.txt", "a")

# Appending to the file
file.write("\nHow are you today?")

# Closing the file
file.close()

# Error handling
# SyntaxError
print ("Hello World!") # missing parenthesis

# NameError
print(x) # variable x is not defined

# TypeError
print("5" + 5) # concatenation of string and integer

# IndexError
my_list = [1, 2, 3]
print(my_list[3]) # index 3 is out of range

# ValueError
int("hello") # cannot convert string to integer

# KeyError
my_dict = {"a": 1, "b": 2, "c": 3}
print(my_dict["d"]) # key "d" not found in dictionary

# ZeroDivisionError
print(5/0) # division by zero