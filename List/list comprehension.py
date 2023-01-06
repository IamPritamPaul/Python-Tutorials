""" Python - List Comprehension """



""" List Comprehension """

""" 
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

Example:

Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

Without list comprehension you will have to write a for statement with a conditional test inside:
"""

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#   if "a" in x:
#     newlist.append(x)

# print(newlist)

""" With list comprehension you can do all that with only one line of code: """

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist=[x for x in fruits if 'a' in x]
# print(newlist)


""" The Syntax """
""" newlist = [expression for item in iterable if condition == True] """
""" The return value is a new list, leaving the old list unchanged. """
""" without any condition the syntax is """
""" newlist=[expression for intem in iterable] """
# newlist=[x for x in range(10)]
# newlist = [x for x in range(10) if x < 5]
# print(newlist)

""" Expression """
""" The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list: """
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x.upper() for x in fruits]
# print(newlist)
# newlist = [x.lower() for x in fruits]
# print(newlist)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist=['hello' for x in fruits]
# print(newlist)
# print(fruits)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist=[x if x!="banana" else "orange" for x in fruits]
# newlist=[]
# for x in fruits:
#     if x!="banana": newlist.append(x)
#     else: newlist.append("orange")
# print(newlist)

