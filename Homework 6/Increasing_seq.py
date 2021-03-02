def combinations(vals, size=None):
    if size is None:
        size = k
    if size == 1:
        return [[i] for i in vals]
    res = []
    c = combinations(vals, size - 1)
    for i in vals:
        for e in c:
            tmp = [i]
            if i <= e[0]:
                tmp.extend(e)
                res.append(tmp)

    return res


n = int(input())
k = int(input())
vals = [int(x) for x in range(1, n + 1)]
print(combinations(vals))

Total = 0
lists = combinations(vals)
for seq in lists:
    Total += 1
print(Total)
