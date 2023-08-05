import random

x = 100
guess = 0
feedback = ''
low = 1
high = x

print('Think of a random number between 1 and', x)

while feedback != 'c' and low != high:
    guess = random.randint(low, high)
    feedback = input(f'Is {guess} number too high (H), too low (L), or correct (C) ? ').lower()
    if feedback == 'h':
        high = guess - 1
    elif feedback == 'l':
        low = guess + 1
else:
    print('The computer guessed your number!')