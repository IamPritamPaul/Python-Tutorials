""" Copy a List """
""" You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2. """
""" There are ways to make a copy, one way is to use the built-in List method copy(). """
list1=["apple","banana","mango","orange","cherry"]
list2=list1.copy()
print("List 1 : ",list1)
print("List 2 : ",list2)
print("----------------------------------------------------------------")
""" Another way to make a copy is to use the built-in method list() """
list1=["apple","banana","mango","orange","cherry"]
list2=list(list1)
print("List 1 : ",list1)
print("List 2 : ",list2)