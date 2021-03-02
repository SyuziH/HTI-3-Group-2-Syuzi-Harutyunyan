a = input()

sequance = a.split()
new_sequance = []
prev_int = 1

for i in range(0, len(sequance)):
    sequance[i] = int(sequance[i])

    new_sequance.append(sequance[i] * prev_int)
    prev_int = sequance[i]

print(max(new_sequance))
