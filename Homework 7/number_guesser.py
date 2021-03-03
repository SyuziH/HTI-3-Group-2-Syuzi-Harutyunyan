numbers = [int(x) for x in range(0, 1001)]
start = 0
current = 500
end = 1000
count = 0
print(current)

while count < 11:
    count += 1
    n = int(input())

    if n == 1:
        start = current
        current = (current + end) // 2

    elif n == -1:
        end = current
        current = (current + start) // 2

    elif n == 0:
        print("You Guessed")

    print('result', current)
