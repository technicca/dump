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

# Optimized version that divides only up to the rounded square root of num:
# If 'n' has a factor greater than its square root, the corresponding co-factor must be less than the square root. For example, if 'n' is 36, its square root is 6. The factors of 36 are 1, 2, 3, 4, 6, 9, 12, 18, and 36. The factors greater than 6 (9, 12, 18, and 36) correspond to the factors less than 6 (4, 3, 2, and 1). So if 36 had no factors less than or equal to 6, it would have no factors greater than 6 either, and it would be prime.

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
print(is_prime(99999999978))