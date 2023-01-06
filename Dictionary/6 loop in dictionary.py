""" Python - Loop Dictionaries """
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x,"--->",thisdict[x])


print("--------------------------------------------------")
# You can also use the values() method to return values of a dictionary:
print("Values: ",end="")
for x in thisdict.values():
  print(x,end=" ")
print()

print("--------------------------------------------------")
# You can also use the keys() method to return keys of a dictionary:
print("Keys: ",end="")
for i in thisdict.keys():
    print(i,end=" ")
print()

print("--------------------------------------------------")
# Loop through both keys and values, by using the items() method:
print("Keys\t\t\tValues")
for x,y in thisdict.items():
    print(x,"\t\t\t",y)
