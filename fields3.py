n = int(input("Enter n: "))

import itertools

sums = []
mins = []
sumlist = []


def sum(x, y):
    sums.clear()
    i = 0
    while i < len(x):
        sums.append((x[i] + y[i]) % 3)
        i += 1
    return tuple(sums)


def minus(x):
    mins.clear()
    j = 0
    while j < len(x):
        if x[j] == 0:
            mins.append(x[j])
        else:
            mins.append((3 - x[j]))
        j += 1
    return tuple(mins)


f=[]
x = [0, 1, 2]
l = [p for p in itertools.product(x, repeat=n)]
for x in l:
    f.append(x)

l = []
r = 2
borders = []
while r < len(f):
    A = itertools.combinations(f, r)
    for x in A:
        i = 0
        count = 0
        l.clear()
        s = list(x)
        for a in s:
            for b in s:
                if a != b:
                    l.append(minus(sum(a, b)))
        while i < len(l):
            count += s.count(l[i])
            i += 1
        if count == 0:
            borders.append(r)
            break
    if r > max(borders):
        break
    r += 1
print("GF(9)=", f)
print(min(borders), "<=max|S|<=", max(borders))
