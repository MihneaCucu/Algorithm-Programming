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
print(date_spiridusi)

def adauga_bucati(date_spiridusi, nume_spiridus, nume_jucarie='', nr_bucati=1):
    if nume_spiridus not in date_spiridusi:
        return 0

    if nume_jucarie != '':
        if nume_jucarie in date_spiridusi[nume_spiridus]:
            date_spiridusi[nume_spiridus][nume_jucarie] += nr_bucati
        else:
            date_spiridusi[ nume_spiridus][nume_jucarie] = nr_bucati
    else:
        for jucarie in date_spiridusi[nume_spiridus]:
            date_spiridusi[nume_spiridus][jucarie] += nr_bucati

    cantitate_totala = sum(date_spiridusi[nume_spiridus].values())

    return cantitate_totala

print(adauga_bucati(date_spiridusi, "Spiridus Poznas", "ponei"))
print(date_spiridusi)