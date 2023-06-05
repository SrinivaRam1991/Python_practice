#Creating a frozen set
# Empty frozen set
fset = frozenset()
# Frozen set of integers
fset = frozenset([1, 2, 3])
# Frozen set of strings
fset = frozenset(['apple', 'banana', 'cherry'])
# Frozen set of mixed types
fset = frozenset([1, 'apple', 3.14])
#Accessing elements in a frozen set
fset = frozenset(['apple', 'banana', 'cherry'])
for x in fset:
    print(x)
#Set operations with frozen sets
fset1 = frozenset([1, 2, 3])
fset2 = frozenset([2, 3, 4])

# Intersection
fset3 = fset1 & fset2
# or 
fset3 = fset1.intersection(fset2)

# Union
fset4 = fset1 | fset2
# or 
fset4 = fset1.union(fset2)

# Difference
fset5 = fset1 - fset2
# or 
fset5 = fset1.difference(fset2)

# Other useful functions for frozen sets
len(fset) #Returns the number of elements in the frozen set.
fset.copy() #Returns a shallow copy of the frozen set.
fset.isdisjoint(other) # Returns True if the frozen set has no elements in common with the other set.
fset.issubset(other) #  Returns True if all elements of the frozen set are in the other set.
fset.issuperset(other) # Returns True if all elements of the other set are in the frozen set.


#Creating a set
s = set()  # Empty set
s = {1, 2, 3} # Set of integers
s = {'apple', 'banana', 'cherry'} # Set of strings
s = {1, 'apple', 3.14} # Set of mixed types

# Accessing elements in a set
s = {'apple', 'banana', 'cherry'}
for x in s:
    print(x)

    # Set operations
    s1 = {1, 2, 3}
    s2 = {2, 3, 4}
    s3 = s1 | s2  # Union  
    # or 
    s3 = s1.union(s2)
    s4 = s1 & s2 # Intersection
    # or
    s4 = s1.intersection(s2)
   
    s5 = s1 - s2   # Difference
    # or
    s5 = s1.difference(s2)
    s6 = s1 ^ s2 # Symmetric difference
    # or 
    s6 = s1.symmetric_difference(s2)
    # Other useful functions for sets
    len(s) #Returns the number of elements in the set.
    s.add(x) # Adds the element x to the set.
    s.remove(x) # Removes the element x from the set. Raises a KeyError if x is not in the set.     
    s.discard(x) # Removes the element x from the set if it is present, otherwise does nothing.
    s.pop() # Removes and returns an arbitrary element from the set. Raises a KeyError if the set is empty.
    s.clear() # Removes all elements from the set.