m = int(input("Introduceți numărul de linii: "))
n = int(input("Introduceți numărul de coloane: "))
A = []
for i in range(m):
    A.append([int(x) for x in input().split()])
rezultate = [min(sum(linie) - linie[i] for i in range(n)) for linie in A]
for i in rezultate:
    print(i)