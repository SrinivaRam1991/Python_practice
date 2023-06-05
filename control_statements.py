a, b = 33, 200
if b > a:
  print("b is greater than a") # If condition
  # elif condition
  a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

  #Else condition with elif
  a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

  #Else condition without elif
  a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

  # Nested If

  a = 34

if a > 10:
  print("Above ten,")
  if a > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

    #pass Statement
    a = 33
b = 200

if b > a:
  pass
# The break Statement
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

  #The continue Statement
  i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

  #The while Loop
  i = 1
while i < 6:
  print(i)
  i += 1

  # For Loop
  fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)