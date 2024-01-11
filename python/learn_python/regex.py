import re

# This file contains functions that demonstrate the use of regular expressions (regex) to perform pattern matching and string manipulation tasks.


# Check if only certain characters are in the string. By using the ^ we can check if there are any symbols except the ones we specified. ^ allows us to check for any symbol that is NOT what we specified.

def characters(word):
    # This function checks if the string 'word' contains only alphanumeric characters (a-z, A-Z, 0-9).
    # It uses a regular expression pattern that searches for any character that is not in the specified range.
    # If no such character is found, the string passes the check and 'True' is returned.
    result = re.search('[^a-zA-Z0-9]', word)
    if result == None:
        return True
    return False
        
print(characters('test'))

# Write a Python program that matches a string that has an 'a' followed by zero or more 'b's
# * in ab* finds zero or more of the preceding element before *
# For example, abbb* wil search for a, followed by 3 or more b

def find_b(word):
    # This function checks if the string 'word' contains an 'a' followed by zero or more 'b's using regex pattern 'ab*'.
    # The '*' quantifier matches zero or more occurrences of 'b'.
    # If the pattern is found, 'True' is returned; otherwise, 'False' is returned.
    result = re.search('ab*', word)
    if result == None:
        return False
    return True

print(find_b('adhshabb'))


# match a string that has an 'a' followed by one or more 'b's.
# To match an 'a' followed by one or more 'b's, you should use the + character, which means "one or more of the preceding element".

def match_b(word):
    # This function checks for the presence of an 'a' followed by one or more 'b's in the string 'word'.
    # The regex pattern 'ab+' uses the '+' quantifier to require at least one occurrence of 'b' following 'a'.
    # Returns 'True' if the pattern is matched, otherwise 'False'.
    if re.search('ab+', word) == None:
        return False
    return True

print(match_b('abbb'))