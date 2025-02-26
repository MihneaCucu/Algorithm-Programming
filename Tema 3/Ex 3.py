def functie(lungime_autostrada, info_soferi):
    avarii = []
    bune = []
    total_avariat = 0
    avarii.append(info_soferi[0])
    for info in info_soferi:
        x,y = info
        este_adaugat = False
        for avariat in avarii:
            a,b = avariat
            if x < a <= y <= b:
                avariat[0] = x
                este_adaugat = True
                break
            elif x < a < b < y:
                avariat[0] = x
                avariat[1] = y
                este_adaugat = True
                break
            elif a <= x <= b < y:
                avariat[1] = y
                este_adaugat = True
                break
            elif a <= x < y <= b:
                este_adaugat = True
                break

        if not este_adaugat:
            avarii.append([x,y])

    print(avarii)
    st = 0
    dr = avarii[0][0]
    for avariat in avarii:
        total_avariat += avariat[1] - avariat[0]
        if len(bune) == 0 and dr != 0:
            bune.append([st, dr])
        elif dr == 0:
            continue
        else:
            dr = avariat[0]
            bune.append([st, dr])
        st = avariat[1]
    if st != lungime_autostrada:
        bune.append([st, lungime_autostrada])

    print(bune)

    grad_uzura = int(total_avariat / lungime_autostrada * 100)
    return avarii, bune, grad_uzura
def citire_fisier(nume_fisier):
    with open(nume_fisier, 'r') as file:
        linii = file.readlines()
        info_soferi = [list(map(int, linie.strip().split())) for linie in linii]
    return info_soferi

def afisare_fisier(nume_fisier, avarii, bune, grad_uzura):
    with open(nume_fisier, 'w') as file:
        file.write("Portiunile avariate: " + str(avarii) + "\n")
        file.write("Portiunile in buna stare: " + str(bune) + "\n")
        file.write("Gradul de uzura: " + str(grad_uzura) + "%" + "\n")

lungime = 200
info_soferi = citire_fisier('autostrada.in')
avarii, bune, grad_uzura = functie(lungime, info_soferi)
afisare_fisier('autostrada.out', avarii, bune, grad_uzura)