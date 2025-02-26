def citire_date(nume_fisier):
    date_cuburi = []
    with open(nume_fisier, "r") as f:
        linie = f.readline()
        for linie in f:
            cub = [int(element) for element in linie.strip().split()]
            date_cuburi.append(cub)
    return date_cuburi


info_date = citire_date("date.in")
print(info_date)


def cautare_turn_maxim(date_cuburi):
    date_cuburi.sort(key=lambda t: t[0])
    # O linie din tabel reprezinta datele despre turnul cu baza in cubul i: [lista cuburi, inaltimea turnului, nr turnuri posibile]
    tabel_aux = [([date_cuburi[0]], date_cuburi[0][0], 1)]
    for i in range(1, len(date_cuburi)):
        lungime_cub = date_cuburi[i][0]
        culoare_cub = date_cuburi[i][1]
        for turn in tabel_aux:

