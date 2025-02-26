m = int(input("Introduceți numărul de linii: "))
n = int(input("Introduceți numărul de coloane: "))
k = int(input("Introduceti k: "))
A = []
for i in range(m):
    A.append([int(x) for x in input().split()])
for i in range(m):
    linie = A[i]
    linie_permutata = [0]*n
    for j in range(n):
        linie_permutata[(j + k) % n] = linie[j]
    A[i] = linie_permutata
for i in A:
    print('\t'.join(map(str,i)))