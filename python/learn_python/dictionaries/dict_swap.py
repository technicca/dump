# Write a Python function that takes a dictionary as input and returns a new dictionary where the keys and values are swapped.
# Purpose of this code: To swap the keys and values of a dictionary.
# It handles situations where multiple original keys have the same value by grouping them into a list.

ex_dict = {
    'key1': 12,
    'key2': 23,
    'key3': 32
    }

'''Here, you need to check if the value already exists as a key in new_dict
If it does, append the current key to the list of keys for this value
If it doesn't, create a new list with the current key as the only element
Use the setdefault method here'''

def swap_dict(input_dict):
    # The function 'swap_dict' takes a dictionary as input and swaps its keys with values.
    # It iterates over each (key,value) pair.
    new_dict = {}
    for key, value in input_dict.items():
        if value in input_dict.keys():
            new_dict.update(value = key)
        new_dict.setdefault(value)
    return new_dict
print(swap_dict(ex_dict))

'''
My original solution, problems:
 - Checks if values is in input_dict instead of new_dict
 - The update method is used to update the dictionary with the elements from another dictionary object or from an iterable of key/value pairs. In your case, you want to add a new key/value pair to new_dict, so you should use the assignment operator (=) to add a new key/value pair to new_dict. However, since multiple keys in the original dictionary might have the same value, you need to check if the value already exists as a key in new_dict. If it does, you should append the current key to the list of keys for this value. If it doesn't, you should create a new list with the current key as the only element.
'''

def swap_dict(input_dict):
    new_dict = {}
    for key, value in input_dict.items():
        if value in new_dict:
            # If this value is already a key in 'new_dict', append the original 'key' to the associated list.
            new_dict[value].append(key)
        else:
            # If this value is not a key in 'new_dict', create a new list with this 'key'.
            new_dict[value] = [key]
    return new_dict
print(swap_dict(ex_dict))

'''
In this function, for each key/value pair in input_dict, we check if value is already a key in new_dict. If it is, we append key to the list of keys for this value. If it isn't, we create a new list with key as the only element and assign this list to value in new_dict.
'''