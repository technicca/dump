def is_palindrome(input):
    if input == str(input[::-1]):
        return True
    return False

print(is_palindrome('1111'))

# If u want to handle some edge cases, turn input into string by default:

def is_palindrome(input):
    input_str = str(input)
    if input_str == input_str[::-1]:
        return True
    return False
