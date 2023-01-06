""" Python - Set Methods """


""" Set Methods """
'''
Method	Description
add()--->	Adds an element to the set
clear()--->	Removes all the elements from the set
copy()--->	Returns a copy of the set
difference()--->	Returns a set containing the difference between two or more sets
difference_update()--->	Removes the items in this set that are also included in another, specified set
discard()--->	Remove the specified item
intersection()--->	Returns a set, that is the intersection of two other sets
intersection_update()--->	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()--->	Returns whether two sets have a intersection or not
issubset()--->	Returns whether another set contains this set or not
issuperset()--->	Returns whether this set contains another set or not
pop()--->	Removes an element from the set
remove()--->	Removes the specified element
symmetric_difference()--->	Returns a set with the symmetric differences of two sets
symmetric_difference_update()--->	inserts the symmetric differences from this set and another
union()--->	Return a set containing the union of sets
update()--->	Update the set with the union of this set and others

'''



print("-------------------------------------------------")
""" Python Set add() Method """
# The add() method adds an element to the set.
# If the element already exists, the add() method does not add the element.

# Sybtax : set.add(elmnt)

fruits = {"apple", "banana", "cherry"}
print("Fruits :",fruits)
fruits.add("orange")
print("After adding 'orange', Fruits :",fruits)


print("-------------------------------------------------")
""" Python Set clear() Method """
# The clear() method removes all elements in a set.
# Syntax : set.clear()
fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)


print("-------------------------------------------------")
""" Python Set difference() Method """
# Return a set that contains the items that only exist in set x, and not in set y:
# The difference() method returns a set that contains the difference between two sets.
# Meaning: The returned set contains items that exist only in the first set, and not in both sets.
# Syntax : set.difference(set)
x = {"apple", "banana", "cherry"}
print("X :",x)
y = {"google", "microsoft", "apple"}
print("Y :",y)
z = x.difference(y)
print("X-Y :",z)
z1=y.difference(x)
print("Y-X :",z1)


print("-------------------------------------------------")
""" Python Set difference_update() Method """
# The difference_update() method removes the items that exist in both sets.
# The difference_update() method is different from the difference() method, 
# because the difference() method returns a new set, without the unwanted items, 
# and the difference_update() method removes the unwanted items from the original set.
# Syntax : set.difference_update(set)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)
print(x)


print("-------------------------------------------------")
""" Python Set discard() Method """
# The discard() method removes the specified item from the set.
# This method is different from the remove() method, because the remove() method will raise an error if the specified item does not exist, and the discard() method will not.
# Syntax : set.discard(value)
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)


print("-------------------------------------------------")
""" Python Set isdisjoint() Method """
# The isdisjoint() method returns True if none of the items are present in both sets, otherwise it returns False.
# Syntax : set.isdisjoint(set)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)
print(z)
print("-------------------------------------------------")
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.isdisjoint(y)
print(z)



print("-------------------------------------------------")
""" Python Set issubset() Method """
# Return True if all items in set x are present in set y:
# The issubset() method returns True if all items in the set exists in the specified set, otherwise it retuns False.
# Syntax : set.issubset(set)
x = {"a", "b", "c"}
print("x :",x)
y = {"f", "e", "d", "c", "b", "a"}
print("y: ",y)
z = x.issubset(y)
print("z: ",z)



print("-------------------------------------------------")
x = {"a", "b", "c"}
print("x :",x)
y = {"f", "e", "d", "c", "b"}
print("y: ",y)
z = x.issubset(y)
print("z: ",z)



print("-------------------------------------------------")
""" Python Set issuperset() Method """
# The issuperset() method returns True if all items in the specified set exists in the original set, otherwise it retuns False.
# Syntax : set.issuperset(set)
x = {"f", "e", "d", "c", "b", "a"}
print("x :",x)
y = {"a", "b", "c"}
print("y: ",y)
z = x.issuperset(y)
print("z: ",z)


print("-------------------------------------------------")
x = {"f", "e", "d", "c", "b"}
print("x :",x)
y = {"a", "b", "c"}
print("y: ",y)
z = x.issuperset(y)
print("z: ",z)