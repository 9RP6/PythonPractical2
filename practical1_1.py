##20ce100
##RishiPatel


dictionary = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}
k1 = 'A'
k2 = 'G'
if k1 in dictionary:
    print(dictionary[k1], "is present in the dictionary")
else:
    print("Key is not present in the dictionary")
if k2 in dictionary:
    print(dictionary[k2], "is present in the dictionary")
else:
    print("Key is not present in the dictionary")

# Task B: Write a Python script to merge two Python dictionaries.
dictionary1 = {'a': 100, 'b': 200}
dictionary2 = {'x': 300, 'y': 400}
dictionary = {}
dictionary.update(dictionary1)
dictionary.update(dictionary2)
print("task B: ", dictionary)

# Task C: Write a Python program to sum all the items in a dictionary.
dictionary = {'a': 100, 'b': 200}
print("task C:: Sum of all items in dictionary:", sum(dictionary.values()))

# Task D: Write a Python script to add a key to a dictionary.
dictionary = {'a': 100, 'b': 200}
dictionary.update({'c': 300})
print("task D: ", dictionary)

# Task E: Write a Python script to concatenate following dictionaries to create a new one.
dictionary1={1:10, 2:20}
dictionary2={3:30, 4:40}
dictionary3={5:50,6:60}
dictionary4={}
dictionary4.update(dictionary1)
dictionary4.update(dictionary2)
dictionary4.update(dictionary3)
print("task E: ", dictionary4)