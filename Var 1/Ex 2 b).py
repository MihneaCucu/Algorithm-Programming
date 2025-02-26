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

def premianti(info_echipe, *scoruri, k):
    jucatori_premianti = []
    for echipa, info_echipa in info_echipe.items():
        for jucator in info_echipa:
            nume_jucator , puncte = jucator
            puncte_comune = [punct for punct in puncte if punct in scoruri]
            puncte_comune = sorted(puncte_comune)
            n = len(puncte_comune)
            if n >= k:
                media = round(sum(puncte_comune) / n, 2)
                jucator_premiant = (echipa, nume_jucator, puncte_comune, media)
                jucatori_premianti.append(jucator_premiant)

    jucatori_premianti.sort(key=lambda t : (-t[3], t[0], t[1]))
    return jucatori_premianti

scoruri = 50, 25, 40, 60, 30, 45
jucatori_premianti = premianti(info_echipe, *scoruri, k = 3)
print(jucatori_premianti)



'''
Sintaxa functie lambda
lambda *lista_parametri*: *modificare_parametri*
Ex lambda a: a + 1
'''