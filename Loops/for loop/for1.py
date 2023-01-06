""" Python For Loops """

# A for loop is used for iterating over a sequence 
# (that is either a list, a tuple, a dictionary, a set, or a string).

# This is less like the for keyword in other programming languages, and works more 
# like an iterator method as found in other object-orientated programming languages.
# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

print("-----------------------------------------------------------")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

print("-----------------------------------------------------------")
# Looping Through a String
for x in "banana":
  print(x)

print("-----------------------------------------------------------")
# The break Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

print("-----------------------------------------------------------")
# The continue Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

print("-----------------------------------------------------------")
# The range() Function
# The range() function returns a sequence of numbers, starting from 0 by default, 
# and increments by 1 (by default), and ends at a specified number.

for x in range(6):
  print(x)

for x in range(2, 6):    # 2 will be included whereas 6 won't be just like [2,6)
  print(x)

for x in range(2, 30, 3): #here 3 is the increment value bydefault which was 1
  print(x)

print("-----------------------------------------------------------")
""" Else in For Loop """
for x in range(6):
  print(x)
else:
  print("Finally finished!")

# Note: The else block will NOT be executed if the loop is stopped by a break statement.
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")


print("-----------------------------------------------------------")
""" Nested Loops """
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

print("-----------------------------------------------------------")
# The pass Statement
for x in [0, 1, 2]:
  pass

