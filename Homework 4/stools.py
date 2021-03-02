nums = input()
high = [int(x) for x in nums.split()]

maximum = max(high)
sum = 0

for i in high:
    stool = maximum - i
    sum = sum + stool
print(sum)
