n = int(input('Enter the year:'))

if n % 100 == 0:
    print(int(n / 100))
elif n / 100 < 1:
    print(int(n / 100) + 1)
else:
    print(n // 100 + 1)

