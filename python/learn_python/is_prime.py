def is_prime(num):
    if num < 2: # 1 is not prime
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


# Shorter version:

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return num > 1

print(is_prime(13))

# My original solution
# Problem: function will return True for num = 1 or 2

def is_prime(num):
    if num > 2:
        for i in range(2, num-1):
            if num % i == 0:
                return False
    return True
