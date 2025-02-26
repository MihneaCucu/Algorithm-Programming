def scrie_in_fisier(nume_fisier, cuvinte):
    with open(nume_fisier, 'w') as f:
        f.write(' '.join(sorted(set(cuvinte))))
def citire_siruri(nume_fisier):
    with open(nume_fisier, "r") as f:
        subliste = [linie.strip().split() for linie in f]
        return subliste
nume_fisier = "cuvinte.in"
subliste = citire_siruri(nume_fisier)
w = input("cuvantul este ")
cuvinte_potrivite = sorted(set([cuvant for sublista in subliste for cuvant in sublista if w in cuvant]))
if cuvinte_potrivite:
        scrie_in_fisier("cuvinte.out", cuvinte_potrivite)
else:
    scrie_in_fisier("cuvinte.out", ["Imposibil!"])