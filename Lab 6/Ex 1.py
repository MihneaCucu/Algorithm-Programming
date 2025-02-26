with open("date.in", "r") as fisier:
    linie = fisier.readline()
    linie = linie.split()
    linie = [int(element) for element in linie]


def subsecventa_maxima(lista):
    subsecv = []
    subsecv.append(lista[0])
    n = len(lista)
    for i in range(1, n):
        subsecv.append(max(subsecv[i - 1] + lista[i], lista[i]))
    smaxi = max(subsecv)
    indexmax = subsecv.index(smaxi)

    # range(inceput_inclusiv,sfarsit_exclusiv, pas)
    rezultat = []
    s = 0
    for i in range(indexmax, -1, -1):
        if s == smaxi:
            break
        s += lista[i]
        rezultat.insert(0, lista[i])
    return rezultat


'''Join se aplica numai stringurilor.
    In cazul nostru spatiul reprezinta ce se pune intre elemente.
    Join  primeste ca parametru un iterabil care contine stringuri.
'''

with open("date.out", "w") as fisier:
    rezultat = subsecventa_maxima(linie)
    rezultat = ' '.join(str(element) for element in rezultat)
    fisier.write(rezultat)

'''
1 -2 3 -1 5 2 -6 1 3
1 -1 3 2 7 9 3 4 7
'''
