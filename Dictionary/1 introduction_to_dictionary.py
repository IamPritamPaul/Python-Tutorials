""" Python Dictionaries """
thisdict={"Name":"Pritam Paul","EmpID":"1156701","Branch":"Bangalore"}
print("thisdict :",thisdict)
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered, changeable and do not allow duplicates.
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

print(thisdict["Branch"])
# changable
thisdict["Branch"]="Hyderabad"
print(thisdict)
# Duplicates Not Allowed
thisdict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

# Dictionary Length
print(len(thisdict))
print(len(thisdict1))

#type
print(type(thisdict))

# The dict() Constructor
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

