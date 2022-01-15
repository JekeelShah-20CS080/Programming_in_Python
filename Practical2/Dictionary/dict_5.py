#  20CS080 Jekeel Shah
#  e. Write a Python script to concatenate following dictionaries to create a new one.

#function to concatenate dictionaries
def concatenatedict(dicts):
    newdict = {}
    for dict in dicts:
        for key in dict.keys():
            newdict[key] = dict[key]
    return newdict

#Sample Dictionaries
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

#Printing the new dictionary
newdict = concatenatedict([dic1,dic2,dic3])
print(newdict)