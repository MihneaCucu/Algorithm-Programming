def citire_date(nume_fisier):
    info_concurenti = {}
    concurent_curent = ''
    with open(nume_fisier, "r") as f:
        for linie in f:
            if len(linie.split()) == 1:
                nume_concurent = linie.strip()
                info_concurenti[nume_concurent] = []
                concurent_curent = nume_concurent
            else:
                data = linie.split()
                nume_proba = data[0].strip()
                if "trambulina" in nume_proba:
                    punctaj_proba = [int(element) for element in data[1:]]
                else:
                    punctaj_proba = [float(element) for element in data[1:]]
                info_proba = (nume_proba, punctaj_proba)
                info_concurenti[concurent_curent].append(info_proba)
    return info_concurenti

info_concurenti = citire_date("concurs.in")
print(info_concurenti)