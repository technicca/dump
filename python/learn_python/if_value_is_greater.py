# Return a list with the same length as L, where the value at index i is 
#  True if L[i] is greater than thresh, and False otherwise.
#     >>> elementwise_greater_than([1, 2, 3, 4], 2)
#     [False, False, True, True]

def elementwise_greater_than(L, thresh):
    return [True if val > thresh else False for val in L]
