import random

def gen_matrice(m, n):
    matrice = []
    for i in range(m):
        linie = [random.randint(1,100) for j in range(n)]
        linie.sort()
        matrice.append(linie)
    for j in range(n):
        coloana = [matrice[i][j] for i in range(m)]
        coloana.sort()
        for i in range(m):
            matrice[i][j] = coloana[i]

    return matrice


m = 3
n = 4
rezultat = gen_matrice(m, n)
for linie in rezultat:
    print(linie)

matrice = [
    [1, 4, 7, 11],
    [2, 5, 8, 12],
    [3, 6, 9, 16],
    [10, 13, 14, 17]
]

def cautare_1(matrice, x):
    m = len(matrice)
    n = len(matrice[0])
    for i in range(m):
        for j in range(n):
            if matrice[i][j] == x:
                return (i,j)
    return None

x = 6
rez1 = cautare_1(matrice,x)
print(f'O(mn): {rez1}')

def cb(linie, x):
    st = 0
    dr = len(linie)-1
    while st <= dr:
        k = (st+dr)//2
        if linie[k] == x:
            return k
        elif linie[k] < x:
            st = k + 1
        else:
            dr = k - 1
    return None

def cautare_2(matrice, x):
    m = len(matrice)
    n = len(matrice[0])
    for i in range(m):
        index = cb(matrice[i], x)
        if index is not None:
            return (i, index)
    return None

rez2 = cautare_2(matrice,x)
print(f'O(mlogn): {rez2}')

def cautare_3(matrice, x):
    m = len(matrice)
    n = len(matrice[0])
    i = 0
    j = n-1
    while i < m and j >= 0:
        if matrice[i][j] >= 0:
            return (i, j)
        elif matrice[i][j] < x:
            i = i + 1
        else:
            j = j - 1
    return None

rez3 = cautare_3(matrice, x)
print(f'O(m + n): {rez3}')