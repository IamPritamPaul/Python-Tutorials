""" Python Tuples """

# Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.
thistuple = ("apple", "banana", "cherry")
print(thistuple)

print("-------------------------------------------------")
""" Tuple Items """
# Tuple items are ordered, unchangeable, and allow duplicate values.
# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

""" Ordered """
# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

""" Unchangeable """
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

""" Allow Duplicates """
# Since tuples are indexed, they can have items with the same value:
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

print("-------------------------------------------------")
""" Tuple Length """
# To determine how many items a tuple has, use the len() function:
print("length of the tuple 'thistuple' :",len(thistuple))

print("-------------------------------------------------")
""" Create Tuple With One Item """
# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
# use a comma else it will not be recognized as tuple
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

print("-------------------------------------------------")
""" Tuple Items - Data Types """
# Tuple items can be of any data type:
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print(tuple1)
print(tuple2)
print(tuple3)
# A tuple can contain different data types:
tuple4=('apple',4,True,7.7,"apple",[1,2,3,4],tuple1,tuple2)
print(tuple4)

print("-------------------------------------------------")
""" The tuple() Constructor """
# It is also possible to use the tuple() constructor to make a tuple.
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
list1=[i for i in range(10)]
thistouple=tuple(list1)
print(thistouple)