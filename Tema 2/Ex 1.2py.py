def cuvinte_cu_aceeasi_lungime (sir, w):
    cuvinte = sir.split()
    l = len(w)
    cuvinte_distincte = set([c for c in cuvinte if len(c) == l])
    return cuvinte_distincte

sir = "exemplu acesta pentru cuvinte ab ba na ru tu le"
w = "ni"

rezultat = cuvinte_cu_aceeasi_lungime(sir, w)
for cuvant in rezultat:
    print(cuvant)