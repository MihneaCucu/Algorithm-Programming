import math
def frecventa_cuv(*nume_fisiere):
    dictionar = {}
    for nume_fisier in nume_fisiere:
        with open(nume_fisier, "r") as fisier:
            for linie in fisier:
                cuvinte = linie.split()
                for cuvant in cuvinte:
                    if cuvant not in dictionar.keys():
                        dictionar[cuvant] = 1
                    else:
                        dictionar[cuvant] += 1
    return dictionar

dictionar = frecventa_cuv("cuvinte1.in", "cuvinte2.in")
#print(dictionar)

lista_cuvinte_sortata = sorted(dictionar)
for cuvant in lista_cuvinte_sortata:
    pass#print(cuvant, end=" ")
#print()

dictionar2 = frecventa_cuv("cuvinte1.in")
lista_frecvente_sortate = sorted(dictionar2.items(), key=lambda d: d[1], reverse=True)
#print(lista_frecvente_sortate)

'''
dictionar.items() = lista de tupluri cheie valoare
NU E DICTIONAR!!!
Definirea unei functii lambda
lambda [lista_de_parametri]: prelucrarea parametrilor
Functiile lambda nu sunt pastrate in memorie si se folosesc o singura data
In cazul de mai sus, functia lambda se aplica fiecarui element iterabil
'''


dictionar3 = frecventa_cuv("cuvinte2.in")
def cuvant_max_frecventa(nume_fisier):
    d_frecv = frecventa_cuv(nume_fisier)
    print(d_frecv)
    cuvinte = sorted(d_frecv.items(), key=lambda x: x[0])
    cuvant_max = max(cuvinte, key=lambda x: x[1])
    return cuvant_max[0]
print(cuvant_max_frecventa("cuvinte2.in"))
def dcos(nume_fisier1, nume_fisier2):

#Intersectia a doua tupluri se face cu &
#inters = set(dictionar2) & set(dictionar3)
    s1 = 0
    for cuvant in dictionar:
        p = dictionar2.get(cuvant,0)*dictionar3.get(cuvant,0)
        s1 += p
    s2 = 0
    for cuvant in dictionar2:
        p = dictionar2[cuvant]**2
        s2 += p
    s2 = math.sqrt(s2)
    s3 = 0
    for cuvant in dictionar3:
        p = dictionar3[cuvant]**2
        s3 += p
    s3 = math.sqrt(s3)
    s2 = s2*s3
    return s1/s2
rez = dcos("cuvinte1.in", "cuvinte2.in")
#print(f"{rez:.2f}")

