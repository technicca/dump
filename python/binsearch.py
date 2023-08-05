# Naive search looks through each member of an array and matches it with our target. If they match, then it returns the index of that item in the list.

def native_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
    return -1

print(native_search([1, 12, 3, 55, 11, 123, 112121, 5], 5))

# Binary search is superior for sorted lists

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 6

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == target:
            return mid
        elif guess > target:
            high = mid - 1
        else:
            low = mid + 1

    return None



print(binary_search(arr, target))  # Output: 5
