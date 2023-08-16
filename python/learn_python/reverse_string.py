input_str = 'test123'
# The syntax for slicing is [start:stop:step]
def reverse(str):
    return str[::-1]
print(reverse(input_str))

# If you don't know how many arguments you need, just use *args:
def reverse(*args):
    return [arg[::-1] for arg in args]
print(reverse(input_str))
print(reverse(input_str2))
print(reverse(input_str3))
