# print(10 > 9)
# print(10 == 9)
# print(10 < 9)

# a = 200
# b = 33

# if (b):
#   print("b is greater than a")
# else:
#   print("b is NOT greater than a")



# print(bool(None))
# print(bool(""))
# print(bool(15))
# print(bool(-15))
# print(bool(0))


# x = "Hello"
# y = 15
# print(bool(x))
# print(bool(y))


"""
Almost any value is evaluated to True if it has some sort of content.

Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones.

"""

"""
One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:
"""
# class myclass():
#   def __len__(self):
#     return 0
# class my_class_2():
#     def abc(self):
#         return 1

# myobj = myclass()
# obj2=my_class_2()
# print(bool(myobj))
# print(bool(obj2))


"""
Functions can Return a Boolean
"""
# def myFunction() :
#   return True

# print(myFunction())

# def myFunction() :
#   return True

# if myFunction():
#   print("YES!")
# else:
#   print("NO!")


# x = 200.6
# print(isinstance(x, int))  #Python isinstance() function returns True if the object is specified types, and it will not match then return False. 

# x = 200
# print(isinstance(x, int))



 