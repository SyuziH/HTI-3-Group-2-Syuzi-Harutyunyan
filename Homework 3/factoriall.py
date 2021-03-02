def is_factorial(num):
    fact = 1
    if num == 0:
        print(1)
    else:
        for i in range(1, num + 1):
            fact = i * fact
        print(fact)


num = int(input('Enter the number '))
is_factorial(num)
