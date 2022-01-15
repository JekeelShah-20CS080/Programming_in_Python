#  20CS080 Jekeel Shah
#  a.Write a Python program to add member(s) in a set and clear a set

#Defining function to add items
def addtoset(set,items):
    for item in items:
        set.add(item)
    return set

#Sample set
set = {"1","2","3","4"}

#Another Sample set
items = {'a','b','c','d'}

#Calling function addtoset()
set = addtoset(set,items)

#printing the set
print(set)