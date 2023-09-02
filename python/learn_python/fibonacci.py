def fibonacci(n):
    num1, num2 = 0, 1
    for i in range(n):
        print(num1, end=' ')
        num1, num2 = num2, num1 + num2
    return num1


fibonacci(17)