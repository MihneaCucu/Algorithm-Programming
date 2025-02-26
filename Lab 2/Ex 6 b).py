import re

# Citirea propoziției, cuvântului de înlocuit și cuvântului cu care să fie înlocuit
propozitie = input("Introduceți propoziția: ")
cuvant_s = input("Introduceți cuvântul de înlocuit: ")
cuvant_t = input("Introduceți cuvântul cu care să fie înlocuit: ")

# a) și b) - Înlocuirea cuvintelor (cu sau fără semne de punctuație)
def inlocuieste_cuvinte(propozitie, cuvant_s, cuvant_t):
    pattern = re.compile(r'\b' + re.escape(cuvant_s) + r'\b', re.IGNORECASE)
    propozitie_inlocuita = pattern.sub(cuvant_t, propozitie)
    return propozitie_inlocuita

propozitie_inlocuita = inlocuieste_cuvinte(propozitie, cuvant_s, cuvant_t)

print("Propoziția modificată este:")
print(propozitie_inlocuita)
