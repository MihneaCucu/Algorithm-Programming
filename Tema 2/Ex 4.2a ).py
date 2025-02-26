propozitie = input("Introduceți propoziția: ")

litere_mici = 0
litere_mari = 0
semne_punctuatie = 0

for caracter in propozitie:
    if caracter.islower():
        litere_mici += 1
    elif caracter.isupper():
        litere_mari += 1
    elif caracter in string.punctuation:
        semne_punctuatie += 1

print("Numărul de litere mici:", litere_mici)
print("Numărul de litere mari:", litere_mari)
print("Numărul de semne de punctuație:", semne_punctuatie)
