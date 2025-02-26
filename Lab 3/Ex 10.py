m = int(input("Introduceți numărul de linii: "))
n = int(input("Introduceți numărul de coloane: "))
A = []
for i in range(m):
    A.append([int(x) for x in input().split()])
rezultate = [min(sum(linie) - linie[i] for i in range(n)) for linie in A]
for i in range(m):
    for j in range(0, m - i - 1):
        if A[j][0] > A[j + 1][0]:
            A[j], A[j + 1] = A[j + 1], A[j]
for linie in A:
    for element in linie:
        print(f'{element:4}', end=' ')
    print()