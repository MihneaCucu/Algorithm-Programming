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


def rezultate(info_concurenti, *nume_probe, N):
    rezultate_probe = []
    for concurent, info_concurent in info_concurenti.items():
        for nume_proba, puncte in info_concurent:
           if nume_proba in nume_probe and len(puncte) >= N:
               valori_ramase = sorted(puncte)[1:-1]
               medie = round(sum(valori_ramase) /  len(valori_ramase), 2)
               rezultate_probe.append((nume_proba, concurent, medie, valori_ramase))
    rezultate_probe.sort(key=lambda x: (x[0], -x[2], x[1]))
    return rezultate_probe

print(rezultate(info_concurenti, "trambulina", "greutati", N = 5))


