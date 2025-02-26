def citire_liste(nume_fisier):
    with open(nume_fisier, "r") as f:
        n = int(f.readline().strip())
        liste = [[] for _ in range(n)]
        for line in f:
            x, y = map(int, line.strip().split())
            liste[y].append(x)
        return liste

def scrie_in_fisier(nume_fisier, elemente):
    with open(nume_fisier, 'w') as f:
        for elem in sorted(set(elemente), reverse=True):
            f.write(str(elem) + '\n')

def numar_divizori(numar):
    return sum(1 for i in range(1, numar + 1) if numar % i == 0)

nume_fisier = "liste.in"
L = citire_liste("liste.in")

k = int(input("k este "))

elemente_potrivite = [elem for sublista in L for elem in sublista if numar_divizori(elem) == k]

if elemente_potrivite:
    scrie_in_fisier("divizori.out", elemente_potrivite)
else:
     scrie_in_fisier("divizori.out", ["Imposibil!"])