""" Python - Remove Dictionary Items """
# There are several methods to remove items from a dictionary:

print("\n-----------  pop() --------------------\n")
# pop() method
# The pop() method removes the item with the specified key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print("Before pop() thisdict is:",thisdict)
thisdict.pop("model")
print("After pop() operation thisdct is:",thisdict)

print("\n-----------  popitem()  --------------------\n")
# popitem() method
# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print("Before popitem() thisdict is:",thisdict)
thisdict.popitem()
print("After popitem() operation thisdct is:",thisdict)

print("\n-----------  del  --------------------\n")
# del keyword
# The del keyword removes the item with the specified key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print("Before del operation thisdict is :",thisdict)
del thisdict["model"]
print("After del operation thisdict is :",thisdict)


# clear() method
# The clear() method empties the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print("Before clear() operation thisdict is :",thisdict)
thisdict.clear()
print("After clear() operation thisdict is :",thisdict)