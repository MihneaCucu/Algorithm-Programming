import string
def nr_cuv_distincte(propozitie):
    for semn in string.punctuation:
        propozitie = propozitie.replace(semn, ' ')
    cuvinte = propozitie.split()
    cuvinte_distincte = set(cuvinte)
    print(cuvinte_distincte)
    numar = len(cuvinte_distincte)
    return numar
prop = "Ana are prune si gutui verzi, dar mai multe prune decat gutui!"
rezultat = nr_cuv_distincte(prop)
print(rezultat)
