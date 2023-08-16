numbers = [1, 2, 3, 4, 5]
numbers_new = [num for num in numbers if num % 2 == 0]
print(numbers_new)

# The num for num syntax in a list comprehension is used to specify what value should be added to the new list for each element in the original list.

# The first num is what gets added to the new list for each element in the original list. The for num part is the loop that iterates over each element in the original list.

# So num for num in numbers means "for each number in numbers, add that number to the new list". If you wanted to add something else to the new list, you would change the first num. For example, num * 2 for num in numbers would add double each number to the new list.

numbers_new = [num * 2 for num in numbers if num % 2 == 0] # Returns double value for each valid num


You are my programming tutor, I'm learning python and I'm relatively new. I know basics about data types, strings, lists, tuples, loops, etc. Some of my knowledge has holes. Give me some beginner-intermidate level problems to solve and be ready to check my solutions.
Phind

Write a Python function that takes a list of numbers as input and returns a new list containing only the even numbers.
Write a Python function that takes a string as input and returns a new string that is the reverse of the input string.
Write a Python function that takes two lists as input and returns a new list that contains only the elements that are common between the two lists (without duplicates).
Write a Python function that takes a string as input and returns a dictionary where the keys are the characters in the string and the values are the number of times each character appears in the string.
Write a Python function that takes a number as input and returns True if the number is a prime number, and False otherwise.