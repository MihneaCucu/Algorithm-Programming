import random
def generare_matrice(n,m):
    with open("matrice.in", "w") as fisier:
        for i in range(n):
            linie = [random.randrange(1,100) for j in range(m)]
            linie_formatata = " ".join(str(linie[j]) for j in range(m))
            fisier.write(f"{linie_formatata}\n")

generare_matrice(4,5)

def citire_matrice(nume_fisier="matrice.in"):
    matrice = []
    with open(nume_fisier, "r") as fisier:
        for linie in fisier:
            linie = [int(nr) for nr in linie.split()]
            matrice.append(linie)
    return matrice

def transpusa(matrice):
    tr = []
    m = len(matrice[0])
    n = len(matrice)
    for j in range(m):
        linie = []
        for i in range(n):
            linie.append(matrice[i][j])
        tr.append(linie)
    return tr

def matrice_ord(matrice):
    matrice = sorted(matrice, key=lambda linie: linie[-1])
    return matrice

def afisare(*lista_matrice):
    with open("matrice.out", "w") as fisier:
        for matrice in lista_matrice:
            for linie in matrice:
                linie = " ".join(str(i) for i in linie)
                fisier.write(f"{linie}\n")
            fisier.write("\n")

matrice_tr = transpusa(citire_matrice())
matrice_ordonata = matrice_ord(citire_matrice())
afisare(matrice_tr, matrice_ordonata)
'''Sintaxa functie lambda 
lambda [lista de parametri]: [lista de parametri modificati]
lambda a,b: a+b
'''