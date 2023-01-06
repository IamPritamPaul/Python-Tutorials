""" Join Two Lists """
""" There are several ways to join, or concatenate, two or more lists in Python. """

""" One of the easiest ways are by using the + operator """
# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
# list3 = list1 + list2
# print(list3)

""" Another way to join two lists is by appending all the items from list2 into list1, one by one: """
# list1=["a","b","c","d"]
# list2=[1,2,3,4,5]
# list3=[]
# for i in list1:
#     list3.append(i)
# for i in list2:
#     list3.append(i)
# print("List1 : ",list1)
# print("List2 : ",list2)
# print("List3 : ",list3)


""" you can use the extend() method, which purpose is to add elements from one list to another list """
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)