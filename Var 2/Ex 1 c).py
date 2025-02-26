def citire_siruri(nume_fisier):
    with open(nume_fisier, "r") as f:
        subliste = [linie.strip().split() for linie in f]
        return subliste
nume_fisier = "cuvinte.in"
subliste = citire_siruri(nume_fisier)
def prelucrare_siruri(L, n):
    for sublista in L:
        sublista.append(''.join([c[-1] for c in sublista]))
        sublista[:] = [cuvant for cuvant in sublista if sum(1 for litera in cuvant if litera in 'aeiou') >= n]

prelucrare_siruri(subliste, 3)
for sublista in subliste:
    print(' '.join(sublista))