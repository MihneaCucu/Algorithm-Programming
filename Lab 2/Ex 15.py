def contine_litera(cuv):
    for c in cuv:
        if c.isalpha():
            return True

    return False


def oglindit(cuv):
    return cuv[::-1]


def inversmax(propozitie):
    cuvinte = propozitie.split(' ')
    cuvinte_oglindite = [oglindit(cuvant) if contine_litera(cuvant) else cuvant for cuvant in cuvinte ]

    return ' '.join(cuvinte_oglindite)

print(inversmax('Mara  23a4 1234 %&a* %&*( are mere'))