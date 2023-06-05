# Python program to find Compound interest



p=int(input("Enter the principal amount: "))
r=int(input("Enter rate of interest: "))
t=int(input("Enter number of years: " ))
n=int(input("Enter number of times the interest is compounded per year:"))
A=p*(1+r/n)**n*t
print('Compount Interest:', A)