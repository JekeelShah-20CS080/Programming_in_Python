#  20CS080 Jekeel Shah
#  b.Write a Python program to remove an item from a set if it is present in the set

#defining function to remove items
def removeitem(set,item):
    set.discard(item)
    return set

#Sample set
set = {1,2,3,4,5,6,7}

#calling function removeitem()
set = removeitem(set,2)

#printing set before removing item 2 from set
print(set)

#calling function
set = removeitem(set,10)

#printing set after removing item 10 from set
print(set)