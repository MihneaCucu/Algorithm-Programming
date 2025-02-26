def cifre_maxime (*numere):
    if not numere:
        return None
    cifre_maxime = []
    for numar in numere:
        cifre = str(numar)
        cifre_maxime.append(max(cifre))
    rezultat = int(''.join(cifre_maxime))
    return rezultat

def baza (a, b, c):
    max_a = cifre_maxime(a)
    max_b = cifre_maxime(b)
    max_c = cifre_maxime(c)
    return max_a <= 1 and max_b <= 1 and max_c <= 1

print(baza(1001, 11, 100))
print(baza(1001, 17, 100))