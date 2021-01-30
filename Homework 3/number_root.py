def digital_root(num):
    sum = 0
    for i in str(num):
        a = int(num) % 10
        sum = sum + a
        num = num / 10
    if sum < 10:
        print(sum)
    else:
        digital_root(sum)


num = int(input('Enter the number '))
digital_root(num)
