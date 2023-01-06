""" List Methods """
""" Python has a set of built-in methods that you can use on lists. """

"""
Method-> Description

append()->	Adds an element at the end of the list

clear()->	Removes all the elements from the list

copy()->	Returns a copy of the list

count()->	Returns the number of elements with the specified value

extend()->	Add the elements of a list (or any iterable), to the end of the current list

index()->	Returns the index of the first element with the specified value

insert()->	Adds an element at the specified position
list1.insert(index,value)

pop()->	Removes the element at the specified position

remove()->	Removes the item with the specified value

reverse()->	Reverses the order of the list

sort()->	Sorts the list
"""

# append()
l1=[1,2,3,4,5]
print("List1 :",l1)
l1.append([6,7,8])
print("List1 :",l1)
l2=[6,7,8]
l1.append(l2)
print("List1 :",l1)
for i in l2:
    l1.append(i)
print("List1 :",l1)

print("-------------------------------------------------------")
# clear()
l1.clear()
print("List1 :",l1)

print("-------------------------------------------------------")
#copy()
l1=[1,2,3,4,5]
# l2=l1.copy()
l2=list(l1)
print("List2 :",l2)

print("-------------------------------------------------------")
# count()
list1=[1,1,1,3,3,2,2,2,2,2,5,5,5,5,5,5,6,6,6,6,6]
print("Number of elements in list1 :",list1.count(5))

print("-------------------------------------------------------")
#extend()
list2=[1,2,3]
list3=[4,5,6]
print("List2 :",list2)
print("List3 :",list3)
list2.extend(list3)
print("After being extended by list3, List2 is :",list2)


print("-------------------------------------------------------")
#index()
list4=list1.copy()
print("list4 is :",list4)
print("First Index of 3 is :",list4.index(3))
print("First Index of 4 is :",list4.index(5))


print("-------------------------------------------------------")
#insert()
list5=list2.copy()
print("List 5 :",list5)
list5.insert(1,0)  #1 is the index and 0 is the value
print("After Inserting 0 at index 1 :",list5)


print("-------------------------------------------------------")
#pop()
list5[0],list5[1]=list5[1],list5[0]
print("List5 is :",list5)
list5.pop()
print("After a pop() operation, List5 is: ",list5)
list5.pop()
print("After a pop() operation, List5 is: ",list5)


print("-------------------------------------------------------")
#remove()
list6=[x for x in range(10)]
print(list6)
list6.remove(6)
print("After removeing 6 List6 is: ",list6)

print("-------------------------------------------------------")
#reverse()
print("list6 is :",list6)
list6.reverse()
print("After reversing list is :",list6)


print("-------------------------------------------------------")
#sort()
list6.sort()
print("Sorted in assending order :",list6)
list6.sort(reverse=True)
print("Sorted in descending order :",list6)