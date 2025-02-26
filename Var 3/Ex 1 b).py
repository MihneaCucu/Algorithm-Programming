def citire_liste(nume_fisier):
    with open(nume_fisier, "r") as f:
        n = int(f.readline().strip())
        liste = [[] for _ in range(n)]
        for line in f:
            x, y = map(int, line.strip().split())
            liste[y].append(x)
        return liste

nume_fisier = "liste.in"
lista = citire_liste("liste.in")

def prelucrare_liste(L, x):
    for sublista in L:
        L[L.index(sublista)] =  [elem for elem in sublista if elem != x]
    L[:] = [sublista for sublista in L if len(sublista) > 1]

prelucrare_liste(lista, 0)

for sublista in lista:
    print(sublista)