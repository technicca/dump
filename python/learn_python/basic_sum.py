number = float(input('Name a number: '))
number2 = 0.0

if 9 < number < 21:
    number2 = float(input('Name a second number: '))
    sum = number + number2
    print(sum)
else:
    print('')

if sum > 100:
    print ('That\'s a large sum')
    
    

# Optimal:

number = float(input('Name a number: '))
number2 = 0.0

if 9 < number < 21:
    number2 = float(input('Name a second number: '))
    total = number + number2
    print(total)
    if total > 100:
        print ('That\'s a large sum')
