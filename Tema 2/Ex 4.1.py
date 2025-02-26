def mini_maxi():
    with open("numere.txt", "r") as file:
        numere = file.read().replace("\n", " ")

    cifre = [c for c in numere if c.isdigit()]

    cifre_cresc = sorted(cifre)
    cifre_cresc = [int(cifra) for cifra in cifre_cresc]

    if cifre_cresc[0] == 0:
        # cifra_minima_nenula = min([c for c in cifre_cresc if c != 0])

        for cifra in cifre_cresc:
            if cifra != 0:
                cifra_minima_nenula = cifra
                break

        # Cum construim nr min = cifra_minima_nenula + toate_zerourile + restul_din_cifre_cresc (sarim peste prima
        # cifra)
        poz_cifra_nenula = cifre_cresc.index(cifra_minima_nenula)

        l_cifre_cresc = len(cifre_cresc)
        numar_minim = [cifra_minima_nenula] + [cifre_cresc[i] for i in range(l_cifre_cresc) if i != poz_cifra_nenula]

        # numar_minim = [str(numar_minim[i]) for i in range(len(numar_minim))]
        cifre_cresc = [str(cifra) for cifra in numar_minim]

    cifre_decr = sorted(cifre, reverse=True)

    maxi = ''.join(cifre_decr)
    mini = ''.join(cifre_cresc)

    print(f"Minim este {mini}")
    print(f"Maxim este {maxi}")


mini_maxi()