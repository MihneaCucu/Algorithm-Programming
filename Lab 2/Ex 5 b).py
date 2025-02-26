
propozitie = input("Introduceți propoziția: ")
corect = input("Introduceți șirul corect: ")
gresit = input("Introduceți șirul greșit: ")

# a) Corectarea primei greșeli
propozitie_corectata = propozitie.replace(gresit, corect)


print("Propoziția corectată este:")
print(propozitie_corectata)

# b) Corectarea a maxim p greșeli (care nu se suprapun)
p = int(input("Introduceți numărul maxim de greșeli de corectat: "))

def corecteaza_greseli(propozitie, corect, gresit, p):
    propozitie_corectata = propozitie
    count = 0
    while p > 0 and gresit in propozitie_corectata:
        propozitie_corectata = propozitie_corectata.replace(gresit, corect, 1)
        p -= 1
        count += 1
    return propozitie_corectata, count

propozitie_corectata, gresele_corectate = corecteaza_greseli(propozitie, corect, gresit, p)

if gresele_corectate == p:
    print(f"{gresele_corectate} greșeli au fost corectate:")
    print(propozitie_corectata)
elif gresele_corectate < p:
    print(f"Textul conține prea puține greșeli, doar {gresele_corectate} au fost corectate.")
else:
    print(f"Textul conține prea multe greșeli, doar {gresele_corectate} au fost corectate.")
