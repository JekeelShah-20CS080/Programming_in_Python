#  20CS080 Jekeel Shah
#  c. Write a Python program to sum all the items in a dictionary.

# funtction to find the sum of all vales of all keys in a dictionary
def sumofdict(dict):
    sum = 0
    #for every key add the value to sum
    for key in dict.keys():
        sum += dict[key]
    return sum

#Sample dictionary
dict = {'A': 1, 'B':2, 'C':3}

#Printing the dictionary
print(sumofdict(dict))