def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i == 0):
                print('No')
                break
        else:
            print('Yes')

    else:
        print('Is not a prime number')


number = int(input('Enter the number '))
is_prime(number)
