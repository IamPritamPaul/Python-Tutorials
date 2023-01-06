""" Python - Add Set Items """


""" Add elements """
# To add one item to a set use the add() method.
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

""" Add Sets """
# To add items from another set into the current set, use the update() method.
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

s1={3,5,2}
s2={9,7,8}
print(s1)
print(s2)
s1.update(s2)
print(s1)


""" Add Any Iterable """
# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
mytuple=("pritam","paul")
thisset.update(mylist)
thisset.update(mytuple)
print(thisset)