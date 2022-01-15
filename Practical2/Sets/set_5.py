#  20CS080 Jekeel Shah
#  e.Write a Python program to find the most common elements and their counts from list, tuple, dictionary.

#defining function for finding commmon items
def findcommon(items):
    tracker = {}
    for item in items:
        if item not in tracker.keys():
            tracker[item] = 0
        tracker[item]+=1
    maxitem = None
    max = -1
    for key in tracker.keys():
        if((tracker[key]) > max):
            max = tracker[key]
            maxitem = key
    return maxitem,max

#Sample list l1
l1 = [1,2,3,2,3,2,4,5,6]

#Sample tuple tuple1
tuple1 = ("apple","banana","apple","mango")

#printing common elements in list l1
print(findcommon(l1))

#printing common elements in tuple tuple1
print(findcommon(tuple1))
