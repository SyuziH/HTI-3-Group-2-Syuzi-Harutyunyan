n = int(input())
k = int(input())
lis = [int(x) for x in range(1, n + 1)]

if n == k:
    for i in lis:
        print(i, end='')
print(" ")
if k <= 2:
    for i in range(0, len(lis)):
        for j in range(0, n):
            if i <= j:
                print((k - 1) * str(lis[i]) + str(lis[j]))
