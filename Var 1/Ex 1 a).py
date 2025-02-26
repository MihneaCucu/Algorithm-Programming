import math
def citire_matrice(nume_fisier):
    with open(nume_fisier,'r') as f:
        matrice = []
        n = int(f.readline().strip())
        k = int(math.sqrt(n))
        for i in range(k):
            linie = []
            for j in range(k):
                element = int(f.readline().strip())
                linie.append(element)
            matrice.append(linie)

        return matrice

nume_fisier = "matrice.in"
matrice_citita = citire_matrice(nume_fisier)
for linie in matrice_citita:
    print(linie)
