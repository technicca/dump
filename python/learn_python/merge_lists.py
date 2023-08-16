list1 = [1, 2, 3, 4, 5]
list2 = [2, 4, 6, 8, 10]

def concatenate(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common_elements = list(set1.intersection(set2))
    return common_elements

print(concatenate(list1, list2))

# If you don't know how many lists you're gonna have upfront then use *args:

def concatenate(*args):
    sets = [set(lst) for lst in args]
    common_elements = set.intersection(*sets)
    return list(common_elements)
