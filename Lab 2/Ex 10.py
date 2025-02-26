def este_nume_complet_corect(nume_complet):
    # Eliminăm spațiile în exces
    nume_complet = nume_complet.strip()
    nume_complet = ' '.join(nume_complet.split())

    # Verificăm dacă numele complet conține doar litere, cratime și spații
    if not all(caracter.isalpha() or caracter == '-' or caracter == ' ' for caracter in nume_complet):
        return False

    # Separăm numele complet în prenume și nume de familie
    nume = nume_complet.split('-')

    # Verificăm dacă numărul corect de prenume (0, 1 sau 2)
    if len(nume) > 2:
        return False

    for parte in nume:
        parte = parte.strip()
        # Verificăm dacă fiecare nume respectă regulile
        if len(parte) < 3 or not parte[0].isupper() or parte.count('-') > 1:
            return False

    return True

# Exemple de test:
nume1 = "Ionescu-Cherea Mihai-Adrian"
nume2 = "Popescu Elena-Maria"
nume3 = "Vlad Matei"
nume4 = "Ionescu - Cherea Mihai"
nume5 = "Vlad Matei Alexandru"

print(f"{nume1}: {este_nume_complet_corect(nume1)}")
print(f"{nume2}: {este_nume_complet_corect(nume2)}")
print(f"{nume3}: {este_nume_complet_corect(nume3)}")
print(f"{nume4}: {este_nume_complet_corect(nume4)}")
print(f"{nume5}: {este_nume_complet_corect(nume5)}")
