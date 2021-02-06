n = int(input())
students = {}

for i in range(n):
    name = input().split()
    key = name[0]
    rating = name[1]
    students[key] = rating

print(students)

for name, rate in list(students.items()):
    if rate < '60':
        del students[name]

print(students)
