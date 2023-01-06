""" Python Sets """
myset = {"apple", "banana", "cherry"}


print("---------------------------------------------")
""" Set """
# Sets are used to store multiple items in a single variable.
# A set is a collection which is unordered, unchangeable*, and unindexed.
# Note: Set items are unchangeable, but you can remove items and add new items.
# Sets are unordered, so you cannot be sure in which order the items will appear.
thisset={"apple", "banana", "cherry"}
print("thisset :",thisset)


print("---------------------------------------------")
""" Set Items """
# Set items are unordered, unchangeable, and do not allow duplicate values.
thisset1 = {"apple", "banana", "cherry", "apple"}
print("thisset1 :",thisset1)



print("---------------------------------------------")
""" Get the Length of a Set """
# To determine how many items a set has, use the len() function.
print("len(thisset1) :",len(thisset1))



print("---------------------------------------------")
""" Set Items - Data Types """
# Set items can be of any data type:
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print("set1 :",set1)
print("set2 :",set2)
print("set3 :",set3)


# A set can contain different data types:
set1 = {"abc", 34, True, 40, "male"}


print("---------------------------------------------")
""" type() """
myset = {"apple", "banana", "cherry"}
print("type(myset) :",type(myset))


print("---------------------------------------------")
""" The set() Constructor """
# It is also possible to use the set() constructor to make a set.
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print("thisset :",thisset)
list1=["pritam","anik","anirban","ricky","patari"]
print("list1 :",list1)
tuple1=("pritam","anik","anirban","ricky","patari")
print("tuple :",tuple1)
set_from_list=set(list1)
set_from_tuple=set(tuple1)
print("set_from_list :",set_from_list)
print("set_from_tuple :",set_from_tuple)
