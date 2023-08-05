import random

user = int(input('Pick an integer between 1 and 10: '))

while user > 10 or user < 1:
    print('Invalid number')
    user = int(input('Pick an integer between 1 and 10: '))

comp_guess = random.randint(1, 10)
print('Computer guessed:', comp_guess)

if comp_guess == user:
    print('Computer wins!')
else:
    print('You win!')