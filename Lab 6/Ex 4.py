def cel_mai_lung_subsir(sir_cuvinte):
    cuvinte = sir_cuvinte.split()
    lungimi = [1] * len(cuvinte)
    for i in range(1, len(cuvinte)):
        for j in range(0, i):
            if cuvinte[i][:2] == cuvinte[j][-2:]:
                lungimi[i] = max(lungimi[i], lungimi[j] + 1)

    max_lungime = max(lungimi)
    index_final = lungimi.index(max_lungime)

    subsir = [cuvinte[index_final]]
    index_curent = index_final

    for i in range(index_final - 1, -1, -1):
        if cuvinte[i][-2:] == cuvinte[index_curent][:2] and lungimi[i] == lungimi[index_curent] - 1:
            subsir.insert(0, cuvinte[i])
            index_curent = i

    return subsir

with open("date.in", "r") as f:
    sir = f.read()

rez = cel_mai_lung_subsir(sir)

with open("date.out", "w") as f:
    for cuvant in rez:
        f.write(cuvant + "\n")
