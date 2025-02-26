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


def adaugare(info_concurenti, nume_proba, nume_concurent, lista_nr):
    if nume_concurent not in info_concurenti:
        return "Numele probei sau al concurentului nu exista!"

    probe_mapate = map(lambda t: t[0], info_concurenti[nume_concurent])

    if nume_proba not in probe_mapate:
        return "Numele probei sau al concurentului nu exista!"

    for i, (nume_proba_existent, rezultate_existente) in enumerate(info_concurenti[nume_concurent]):
        if nume_proba_existent == nume_proba:
            info_concurenti[nume_concurent][i] = (nume_proba, rezultate_existente + lista_nr)
            return len(info_concurenti[nume_concurent][i][1])

    info_concurenti[nume_concurent].append((nume_proba, lista_nr ))
    return len(lista_nr)

nume_proba = input("Introduceti numele probei: ")
nume_concurent = input("Introduceti numele concurentului: ")
lista_nr = [float(val) if float(val) != int(val) else int(val) for val in input("Introduceti valori numerice separate prin spatiu: ").split()]

rezultat = adaugare(info_concurenti, nume_proba, nume_concurent, lista_nr)

print(rezultat)
print(info_concurenti)
'''functia map are 2 parametri 
primul parametru este o functie
al doilea este un iterabil
functia se aplica fiecarui element din iterabil
'''
