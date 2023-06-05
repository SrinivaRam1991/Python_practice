''' Type conversion is the process of converting the value of one data type(integer,string,float,etc..)
 Python has two type conversions:-
1.implicit type conversion
2.explicit type conversion 
'''

#implicit type conversion

a=15 #int
# int ----> float
print(float(a)) # output 15.0 there is no data loss so we can call it as implicit type converstion

# explicit conversion

b=2.345 #float
#float -----> int
print(int(b)) #result is 2 here we have data lost so we can call it as explicit type conversion