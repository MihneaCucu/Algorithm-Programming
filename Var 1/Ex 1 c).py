def prelucrare_matrice(matrice):
    n = len(matrice)
    for i in range(n):
        element_diagonala = matrice[i][i]
        matrice[i] = [element - element_diagonala for element in matrice[i]]
        del matrice[i][i]
    return matrice

matrice_originala = [[25, 600, 1105], [5011, 270, 9], [1105, 304, 700]]
matrice_prelucrata = prelucrare_matrice(matrice_originala)
for linie in matrice_prelucrata:
   print(' '.join(map(str, linie)))