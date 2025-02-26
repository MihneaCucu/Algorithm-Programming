def nr_max(n):
    numar_max = 1
    for i in range(2, n + 1):
        numar_max = numar_max * 10 + 1
    return numar_max
n = int(input("Introduceti n: "))
c = len(str(nr_max(n)))
for i in range(n):
        numar = 1
        for j in range(i + 1):
            print(f'{numar:{c + 1}}', end=' ')
            numar = numar * (i - j) // (j + 1)
        print()