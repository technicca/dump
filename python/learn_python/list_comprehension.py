numbers = [1, 2, 3, 4, 5]
numbers_new = [num for num in numbers if num % 2 == 0]
print(numbers_new)

# The num for num syntax in a list comprehension is used to specify what value should be added to the new list for each element in the original list.

# The first num is what gets added to the new list for each element in the original list. The for num part is the loop that iterates over each element in the original list.

# So num for num in numbers means "for each number in numbers, add that number to the new list". If you wanted to add something else to the new list, you would change the first num. For example, num * 2 for num in numbers would add double each number to the new list.

numbers_new = [num * 2 for num in numbers if num % 2 == 0] # Returns double value for each valid num
