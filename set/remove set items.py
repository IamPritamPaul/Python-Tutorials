""" Python - Remove Set Items """

""" Remove Item """
# To remove an item in a set, use the remove(), or the discard() method.
thisset = {"apple", "banana", "cherry"}
print("thisset :",thisset)
thisset.remove("banana")
print("After reove() method, thisset :",thisset)

# Note: If the item to remove does not exist, remove() will raise an error.

# Remove "banana" by using the discard() method:
thisset = {"apple", "banana", "cherry"}
print("thisset :",thisset)
thisset.discard("banana")
print("After discard() method, thisset :",thisset)

# Note: If the item to remove does not exist, discard() will NOT raise an error.

# You can also use the pop() method to remove an item, but this method will remove the last item. Remember that sets are unordered, so you will not know what item that gets removed.
# The return value of the pop() method is the removed item.
# Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.
thisset = {"pritam", "sudeshna", "anik", "kanti", "anirban", "dell"}
x = thisset.pop()
print(x)
print(thisset)

l1=[]
for i in range(len(thisset)):
    l1.append(thisset.pop())
print(l1)


# The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)


# The del keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)  #error will come