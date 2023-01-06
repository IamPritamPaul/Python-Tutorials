""" Python Lists """


# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[:4])
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:])

# negative indexing
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# # print(thislist[-4:-1])
# print("kiwi" in thislist)
# print("orange" in thislist)
# print("water mallon" in thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["watermelon"]
# print(thislist)
""" Insert Items """
# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")
# print(thislist)
""" Append Items """
# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)
""" Extend List """
# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)
""" Add Any Iterable """
# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
# print(thislist)






""" Python - Remove List Items """


""" Remove Specified Item """
# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)
""" Remove Specified Index """
# thislist = ["apple", "banana", "cherry"]
# thislist.pop(1)
# print(thislist)
""" If you do not specify the index, the pop() method removes the last item. """
# thislist = ["apple", "banana", "cherry"]
# thislist.pop()
# print(thislist)
""" The del keyword also removes the specified index: """
# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)
""" The del keyword can also delete the list completely. """
# thislist = ["apple", "banana", "cherry"]
# del thislist
# print(thislist)
'''
print(thislist)
          ^^^^^^^^
NameError: name 'thislist' is not defined
'''

""" Clear the List """
# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)
