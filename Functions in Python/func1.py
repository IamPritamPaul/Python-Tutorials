""" Python Functions """
def my_function():
  print("Hello from a function")

my_function()


print("------------------------------------------")
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


print("------------------------------------------")
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")


print("------------------------------------------")
""" def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil") """
# error 


print("------------------------------------------")
""" Arbitrary Arguments, *args """
# If you do not know how many arguments that will be passed into your function,
# add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly:
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


print("------------------------------------------")
""" Keyword Arguments """
# You can also send arguments with the key = value syntax.
# This way the order of the arguments does not matter.
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
# The phrase Keyword Arguments are often shortened to kwargs in Python documentations.


print("------------------------------------------")
""" Arbitrary Keyword Arguments, **kwargs """
# If you do not know how many keyword arguments that will be passed into your function, 
# add two asterisk: ** before the parameter name in the function definition.
# This way the function will receive a dictionary of arguments, and can access the items accordingly:
def my_function(**kid):
    print(kid["name"],end=" ")
    print(kid["surname"])

my_function(name="Pritam",surname="Paul")



print("------------------------------------------")
""" Default Parameter Value """
# If we call the function without argument, it uses the default value:
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()  # default parameter will take care of this
my_function("Brazil")



print("------------------------------------------")
""" Passing a List as an Argument """
# You can send any data types of argument to a function (string, number, list, dictionary etc.), 
# and it will be treated as the same data type inside the function.
# E.g. if you send a List as an argument, it will still be a List when it reaches the function:
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]
my_function(fruits)



print("------------------------------------------")
""" Return Values """
# To let a function return a value, use the return statement:
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))


""" The pass Statement """
# function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
def myfunction():
  pass


print("------------------------------------------")
""" Recursion """
def abc(n):
    if n==0: return
    abc(n-1)
    print(n,end=" ")
abc(10)