# Write a Python function that takes a string as input and returns a dictionary where the keys are the characters in the string and the values are the number of times each character appears in the string.

example = 'Scatter'
dictionary = {}

def to_dict(any_string):
    for char in any_string:
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1
    return dictionary
print(to_dict(example))

# The in keyword in Python is used to check if a value exists in a sequence (like a list, tuple, string, etc.) or other collection type (like a dictionary, set, etc.).

# In the context of if char in dictionary:, it's checking if char is a key in the dictionary. If char is a key in the dictionary, the statement char in dictionary will be True, and the code inside the if block will be executed. If char is not a key in the dictionary, the statement will be False, and the code inside the if block will be skipped.