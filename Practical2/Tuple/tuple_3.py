#  20CS080 Jekeel Shah
#  c.Write a Python program to add an item in a tuple.

#Sample tuple
jekeel = (7, 1, 0, 55, 33, 17)
print(jekeel)

#using merge of tuples with the + operator you can add an element and it will create a new tuple, because tuples are immutable
jekeel =jekeel + (94,)
print(jekeel)

#adding items in a specific index
jekeel= jekeel[:5] + (25, 2, 56) + jekeel[5:]
print(jekeel)

#converting the tuple to list
listx = list(jekeel)

#use different ways to add items in list
listx.append(30)
jekeel = tuple(listx)
print(jekeel)