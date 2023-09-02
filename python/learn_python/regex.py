import re


# Check if only certain characters are in the string. By using the ^ we can check if there are any symbols except the ones we specified. ^ allows us to check for any symbol that is NOT what we specified.

def characters(word):
    result = re.search('[^a-zA-Z0-9]', word)
    if result == None:
        return True
    return False
        
print(characters('test'))

# Write a Python program that matches a string that has an 'a' followed by zero or more 'b's
# * in ab* finds zero or more of the preceding element before *
# For example, abbb* wil search for a, followed by 3 or more b

def find_b(word):
    result = re.search('ab*', word)
    if result == None:
        return False
    return True

print(find_b('adhshabb'))


# match a string that has an 'a' followed by one or more 'b's.
# To match an 'a' followed by one or more 'b's, you should use the + character, which means "one or more of the preceding element".

def match_b(word):
    if re.search('ab+', word) == None:
        return False
    return True

print(match_b('abbb'))