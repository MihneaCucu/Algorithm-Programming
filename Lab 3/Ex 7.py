m = int(input("Introduceți numărul de linii: "))
n = int(input("Introduceți numărul de coloane: "))

A = []
s = 0
for i in range(m):
    A.append([int(x) for x in input().split()])
for i in range(n):
    for j in range(m):
        A[i][j], A[j][i] = A[j][i], A[i][j]
for i in A:
    print('\t'.join(map(str,i)))
