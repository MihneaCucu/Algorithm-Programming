def citire_liste(nume_fisier):
    with open(nume_fisier, "r") as f:
        n = int(f.readline().strip())
        liste = [[] for _ in range(n)]
        for linie in f:
            x, y = map(int, linie.strip().split())
            liste[y].append(x)
        return liste

nume_fisier = "liste.in"
lista = citire_liste("liste.in")
for sublista in lista:
    print(sublista)