""" Sort List Alphanumerically """
l1 = ["orange", "mango", "kiwi", "pineapple", "banana"]
# l1.sort()
# print(l1)

""" Sort the list numerically: """
# l12 = [100, 50, 65, 82, 23]
# l12.sort()
# print(l12)

""" Sort Descending """
# l11 = ["orange", "mango", "kiwi", "pineapple", "banana"]
# l11.sort(reverse=True)
# print(l11)

""" Sort Descending """
# l13 = [100, 50, 65, 82, 23]
# l13.sort(reverse = True)
# print(l13)

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
# l1 = ["banana", "Orange", "Kiwi", "cherry"]
# l1.sort()
# print(l1)
""" in reverse order """
# l1 = ["banana", "Orange", "Kiwi", "cherry"]
# l1.sort(reverse=True)
# print(l1)



# l3=l1.sort()
# print(l3) 
""" In Python, the sort() method is used to sort a list in-place, meaning it modifies the original list directly 
without creating a new list. The sort() method does not return a new sorted list, but rather it sorts the list 
and returns None. That's wwhy the l3 is None here."""


""" if you want to store the sorted list into another list then u have to use sorted() function """
l2=sorted(l1)
print("l1:",l1)
print("l2:",l2)