num = input()
the_first_half = []
the_second_half = []

for i in range(0, int(len(num) / 2)):
    the_first_half.append(int(num[i]))
for j in range(int(len(num) / 2), int(len(num))):
    the_second_half.append(int(num[j]))

if (sum(the_first_half) == sum(the_second_half)):
    print('Yes')
else:
    print('No')
