""" Sort List Alphanumerically """
# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort()
# print(thislist)

""" Sort the list numerically: """
# thislist2 = [100, 50, 65, 82, 23]
# thislist2.sort()
# print(thislist2)

""" Sort Descending """
# thislist1 = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist1.sort(reverse=True)
# print(thislist1)

""" Sort Descending """
# thislist3 = [100, 50, 65, 82, 23]
# thislist3.sort(reverse = True)
# print(thislist3)

""" Customize Sort Function """
# def abc(n):
#     return abs(n-50)
# list1=[100,50,65,82,23]
# list1.sort(key=abc)
# print(list1)

# # 50 0 15 32 27
# # 0 15 27 32 50
# # 50 65 23 82 100

""" Case Insensitive Sort """
""" By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters: """
# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort()
# print(thislist)
""" in reverse order """
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(reverse=True)
print(thislist)


