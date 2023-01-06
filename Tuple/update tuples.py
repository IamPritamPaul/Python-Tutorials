""" Python - Update Tuples """
# Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.
# But there are some workarounds.

print("-----------------------------------------------------------------")
""" Change Tuple Values """
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
x = ("apple", "banana", "cherry")
print("tuple x :",x)
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print("updated tuple x :",x)


print("-----------------------------------------------------------------")
""" Add Items """
# Since tuples are immutable, they do not have a build-in append() method, but there are other ways to add items to a tuple.
# 1. Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.
thistuple = ("apple", "banana", "cherry")
print("Tuple 'thistuple' is :",thistuple)
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print("Updated Tuple 'thistuple' is :",thistuple)

print("-----------------------------------------------------------------")
# 2. Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:
thistuple = ("apple", "banana", "cherry")
print("thistuple :",thistuple)
y = ("orange",)
print("y :",y)
thistuple += y
print("Updated tuple (thistuple+=y) thistuple :",thistuple)


print("-----------------------------------------------------------------")
""" Remove Items """
# Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items:
thistuple = ("apple", "banana", "cherry")
print("thistuple :",thistuple)
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print("Updated Tuple after removing 'apple', 'thistuple' is :",thistuple)


print("-----------------------------------------------------------------")
# Or you can delete the tuple completely:
# The del keyword can delete the tuple completely:
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists


