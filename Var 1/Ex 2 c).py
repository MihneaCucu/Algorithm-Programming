def citire_date(nume_fisier):
    info_echipe = {}
    echipa_curenta = ''
    with open(nume_fisier, "r") as f:
        for linie in f:
            if "Echipa" in linie:
                nume_echipa = linie.strip("Echipa").strip()
                info_echipe[nume_echipa] = []
                echipa_curenta = nume_echipa

            else:
                nume_membru, punctaj_membru = linie.split(":")
                nume_membru = nume_membru.strip()
                punctaj_membru = [int(element) for element in punctaj_membru.split()]
                info_membru = (nume_membru, punctaj_membru)
                info_echipe[echipa_curenta].append(info_membru)
    return info_echipe

info_echipe = citire_date("punctaje.in")

def stergere(info_echipe, nume_echipa, nume_membru):
    for membru in info_echipe.get(nume_echipa, []):
        if membru[0] == nume_membru:
            info_echipe[nume_echipa].remove(membru)
    jucatori_ramasi = [membru[0] for membru in info_echipe.get(nume_echipa, [])]
    if len(jucatori_ramasi) < 2:
        del info_echipe[nume_echipa]
        return f"Am sters si jucatorul 'X' si echipa '{nume_echipa}'."
    else:
        return jucatori_ramasi

echipa = input("Introdu numele echipei: ")
jucator = input("Introdu numele jucatorului: ")

rezultat = stergere(info_echipe, echipa, jucator)
print(rezultat)
print(info_echipe)


'''
Sintaxa functie lambda
lambda *lista_parametri*: *modificare_parametri*
Ex lambda a: a + 1
'''