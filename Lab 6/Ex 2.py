with open("date.in", "r") as fisier:
    matrice = []
    linie = fisier.readline()
    linie = linie.split()
    n, m = [int(element) for element in linie]
    for linie in fisier:
        linie = linie.split()
        linie = [int(element) for element in linie]
        matrice.append(linie)


def suma_maxima_matrice(n, m, matrice):
    suma_matrice = []
    linie = []
    linie.append(matrice[0][0])
    for i in range(1, m):
        linie.append(linie[i - 1] + matrice[0][i])
    suma_matrice.append(linie)
    for i in range(1, n):
        linie = []
        linie.append(suma_matrice[i - 1][0] + matrice[i][0])
        suma_matrice.append(linie)
    for i in range(1, n):
        for j in range(1, m):
            k = max(suma_matrice[i - 1][j], suma_matrice[i][j - 1])
            suma_matrice[i].append(matrice[i][j] + k)
    suma = suma_matrice[n - 1][m - 1]
    i = n - 1
    j = m - 1
    rez = []
    rez.append((n, m))
    while i + j != 0:
        if i == 0:
            j = j - 1
        elif j == 0:
            i = i - 1
        elif suma_matrice[i - 1][j] > suma_matrice[i][j - 1]:
            i = i - 1
        else:
            j = j - 1
        rez.insert(0, (i + 1, j + 1))
    return suma, rez


suma, rez = suma_maxima_matrice(n, m, matrice)
with open("date.out", "r") as fisier:
    suma = str(suma)

'''
2 1 4
1 3 2
1 6 1

2 3 7
3 6 9
4 12 13
'''
