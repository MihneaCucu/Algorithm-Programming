def citire_siruri(nume_fisier):
    with open(nume_fisier, "r") as f:
        subliste = [linie.strip().split() for linie in f]
        return subliste
nume_fisier = "cuvinte.in"
subliste = citire_siruri(nume_fisier)
for sublista in subliste:
    print(sublista)