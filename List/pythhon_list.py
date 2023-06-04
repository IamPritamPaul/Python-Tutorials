""" Python Lists """


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print("ThisList:",thislist)
print("thislist[:4]:",thislist[:4])
print("thislist[2:]:",thislist[2:])

print("--------------------------------------------------------")

""" negative indexing """
print("thislist[-4:-1]:",thislist[-4:-1])

print("--------------------------------------------------------")
""" in the list or not"""
print('''"kiwi" in thislist:''',"kiwi" in thislist)
print('''"orange" in thislist:''',"orange" in thislist)
print('''"water mallon" in thislist:''',"water mallon" in thislist)
print('''"water mallon" not in thislist:''',"water mallon" not in thislist)

print("--------------------------------------------------------")

thislist = ["apple", "banana", "cherry"]
print("ThisList:",thislist)
thislist[1:3] = ["watermelon"]
print('''thislist[1:3] = ["watermelon"]\t---------->\tThisList:''',thislist)

print("--------------------------------------------------------")

""" Insert Items """
thislist.insert(2, "orange")
print(thislist)

print("--------------------------------------------------------")

""" Append Items """
# thislist.append("orange")
# print(thislist)

print("--------------------------------------------------------")

""" Extend List """
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)

print("--------------------------------------------------------")

""" Add Any Iterable """
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
# print(thislist)






""" Python - Remove List Items """


""" Remove Specified Item """
# thislist.remove("banana")
# print(thislist)

print("--------------------------------------------------------")

""" Remove Specified Index """
# thislist = ["apple", "banana", "cherry"]
# thislist.pop(1)
# print(thislist)

print("--------------------------------------------------------")

""" If you do not specify the index, the pop() method removes the last item. """
# thislist = ["apple", "banana", "cherry"]
# thislist.pop()
# print(thislist)

print("--------------------------------------------------------")

""" The del keyword also removes the specified index: """
# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)

print("--------------------------------------------------------")

""" The del keyword can also delete the list completely. """
# thislist = ["apple", "banana", "cherry"]
# del thislist
# print(thislist)
'''
print(thislist)
NameError: name 'thislist' is not defined
'''

""" Clear the List """
# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)
