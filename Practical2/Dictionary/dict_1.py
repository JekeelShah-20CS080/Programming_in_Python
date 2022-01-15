
#  20CS080 Jekeel Shah
#  a. Write a Python script to check whether a given key already exists in a dictionary.

Cars = {
  "brand": "Ferrari",
  "model": "Portofino",
  "year": 2018,
}
#key to find if it exists
key = 'brand'
#if key is present in dictionary
if key in Cars:
    print("Present")
else:
    print("Not present")
#key to find if exists
key = 'Owner'
if key in Cars:
    print("Exists")
else:
    print("Not present")


