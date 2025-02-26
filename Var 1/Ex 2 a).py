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

