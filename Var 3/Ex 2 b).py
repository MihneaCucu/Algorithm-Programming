def citire_date(nume_fisier):
    date_spiridusi = {}
    with open(nume_fisier, "r") as f:
        for linie in f:
            parti = linie.strip().split(":")
            nume_spiridus = parti[0].strip()
            restul_liniei = parti[1].strip().split()
            nume_jucarie = ' '.join(restul_liniei[:-1])
            nr_bucati = int(restul_liniei[-1])

            if nume_spiridus not in date_spiridusi:
                date_spiridusi[nume_spiridus] = {}

            if nume_jucarie not in date_spiridusi[nume_spiridus]:
                date_spiridusi[nume_spiridus][nume_jucarie] = 0

            date_spiridusi[nume_spiridus][nume_jucarie] += nr_bucati

    return date_spiridusi

date_spiridusi = citire_date("spiridusi.in")


def top_spiridusi(date_spiridusi, *nume_spiridusi, nr_minim):
    lista_rezultat = []
    for nume_spiridus in nume_spiridusi:
        cantitate_totala = 0
        multime_jucarii = set()

        for nume_jucarie in date_spiridusi[nume_spiridus]:
            if date_spiridusi[nume_spiridus][nume_jucarie] >= nr_minim:
                multime_jucarii.add(nume_jucarie)
                cantitate_totala += date_spiridusi[nume_spiridus][nume_jucarie]

        if cantitate_totala > 0:
            lista_rezultat.append((nume_spiridus, multime_jucarii, cantitate_totala))

    lista_rezultat = sorted(lista_rezultat, key=lambda t: (-len(t[1]), -t[2], t[0]))
    return lista_rezultat

nume_spiridusi = "Spiridus Harnic", "Spiridus Poznas", "Spiridus Jucaus"

print(top_spiridusi(date_spiridusi, *nume_spiridusi, nr_minim=3))
