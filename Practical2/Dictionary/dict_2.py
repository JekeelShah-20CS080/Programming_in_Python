#  20CS080 Jekeel Shah
#  b. Write a Python script to merge two Python dictionaries.

# sample dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

#making a copy of d1
d = dict1.copy()

#adding d2 to d
d.update(dict2)

#printing d
print(d)