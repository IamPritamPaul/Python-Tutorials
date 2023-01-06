""" Python - Access Tuple Items """

print("------------------------------------------------------------")
""" Access Tuple Items """
# You can access tuple items by referring to the index number, inside square brackets:
thistuple = ("apple", "banana", "cherry")
print("thistuple :",thistuple)
print("thistuple[1] :",thistuple[1])

print("------------------------------------------------------------")
""" Negative Indexing """
# Negative indexing means start from the end. -1 refers to the last item, -2 refers to the second last item etc.
thistuple = ("apple", "banana", "cherry")
print("thistuple[-1] :",thistuple[-1])
print("thistuple[-3] :",thistuple[-3])

print("------------------------------------------------------------")
""" Range of Indexes """
# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new tuple with the specified items.
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print("thistuple[2:5] :",thistuple[2:5])  #[2,5)  close open interval ie; from index 2 to 4
# By leaving out the start value, the range will start at the first item:
print("thistuple[:4] :",thistuple[:4]) # index from 0 to 3
# By leaving out the end value, the range will go on to the end of the list:
print("thistuple[2:] :",thistuple[2:])

print("------------------------------------------------------------")
""" Range of Negative Indexes """
# Specify negative indexes if you want to start the search from the end of the tuple:
print("thistuple[-4:-1] :",thistuple[-4:-1])

print("------------------------------------------------------------")
""" Check if Item Exists """
# To determine if a specified item is present in a tuple use the in keyword:
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
if("guava" not in thistuple):
    print("NO, 'guava' is not in the fruits tuple")
