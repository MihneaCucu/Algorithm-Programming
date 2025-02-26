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

k = int(input("k este "))

def sumcif(n):
    s = 0
    while n != 0:
        s = s + n % 10
        n = n //10
    return s

lista_rezultat = []

for linie in matrice_citita:
    for element in linie:
        if sumcif(element) == k:
            lista_rezultat.append(element)

if len(lista_rezultat) == 0:
    print("Impsoibil!")
else:
    lista_rezultat = set(lista_rezultat)
    lista_rezultat = sorted(lista_rezultat)
    for element in lista_rezultat:
        print(element, end=' ')