#  20CS080 Jekeel Shah
#d. Write a Python script to add a key to a dictionary.

#function to add key to dictionary
def addkey(dict,keyname,keyvalue):
    dict[keyname] = keyvalue
    return dict

#Sample Dictionary
dict = {0: 10, 1: 20}

#New key to be added with its value
keyname = 2
keyvalue = 30

#Calling the function
dict = addkey(dict,keyname,keyvalue)

#Printing the Dictionary
print(dict)