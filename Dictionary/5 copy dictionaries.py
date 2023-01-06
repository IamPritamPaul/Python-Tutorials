""" Python - Copy Dictionaries """

""" You cannot copy a dictionary simply by typing dict2 = dict1, 
because: dict2 will only be a reference to dict1, 
and changes made in dict1 will automatically also be made in dict2. """

# There are ways to make a copy, 
# one way is to use the built-in Dictionary method copy().
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

# Another way to make a copy is to use the built-in function dict().
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

list1=[(1,2),(3,4),(5,6)]
# list1=[1,2,3,4,5,6]  not possible to convert into dictionary
mydict=dict(list1)
print(mydict)