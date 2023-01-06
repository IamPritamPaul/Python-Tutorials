""" Accessing Items """

# You can access the items of a dictionary by referring to its key name, inside square brackets:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)
# There is also a method called get() that will give you the same result:
x = thisdict.get("model")
print(x)


""" Get Keys """
# The keys() method will return a list of all the keys in the dictionary.
x = thisdict.keys()
l1=list(x)
print(x)
print(l1)


print("--------------------------------------------")
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change




""" Get Values """
# The values() method will return a list of all the values in the dictionary.
x = thisdict.values()
print(x)



print("--------------------------------------------")
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the chang
car["year"] = 2020
print(x) #after the change
car["color"] = "red"
print(x)




print("--------------------------------------------")
""" Get Items """
# The items() method will return each item in a dictionary, as tuples in a list.
x = thisdict.items()
l=list(x)
print(x)
print(l)



print("--------------------------------------------")
""" Check if Key Exists """
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")