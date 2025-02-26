n = int(input("n este "))
for i in range(1, 2 ** n):
    v = []
    for j in range(n):
        if (i >> j) & 1:
            v.append(j + 1)
    print(v)