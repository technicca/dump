def sort(num, sequence):
    for i in range (len(sequence)):
        if num in sequence:
            return True
        return False
    
print(sort(99, numbers))


def count_words(sentence):
    words = sentence.split()
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

print(count_words('Palindrome Checker: Write a Python program to check if a string is a palindrome. A palindrome is a word, phrase, number, or other sequences of characters that reads the'))

def is_anagrams(string1, string2):
    if string1 == string2:
        return False
    if [*string1].sort() == [*string2].sort():
        return True

# This should be more robust:

def is_anagrams(string1, string2):
    if string1 == string2:
        return False
    if sorted(string1) == sorted(string2):
        return True
    
print(is_anagrams('test123', 'teset321'))


# ! Find the missing number: take the sum of all numbers we're given -> compare with the sum of i in range n+1, subtract, find the difference

def mis_number(numbers):
    n = len(numbers) + 1
    expected_sum = n * (n + 1) // 2
    missing = expected_sum - sum(numbers)
    return missing

print(mis_number([1, 2, 3, 4, 6, 7]))

# or shorter version:

def mis_number(numbers):
    missing = (len(numbers) + 1) * (len(numbers) + 2) // 2 - sum(numbers)
    return missing


# ! REVERSE STRINGS IN A SENTENCE, for "Python is fun", the output should be "fun is Python"
def reverse_sentence(sentence):
    words = sentence.split()
    words.reverse()  # reverse the list in-place
    reversed_sentence = ' '.join(words)  # join the words back into a sentence
    return reversed_sentence

print(reverse_sentence('Python is fun'))

