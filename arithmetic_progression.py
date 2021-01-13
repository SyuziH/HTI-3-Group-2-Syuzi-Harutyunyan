a1 = int(input('Enter the first member of arithmetic progression:'))
a2 = int(input('Enter the second member of arithmetic progression:'))
n = int(input('Enter the N:'))

unknownMember = a1 + (a2 -a1) * (n-1)

if n == 1:
    print(a1)
elif n == 2:
    print(a2)
else:
    print(unknownMember)