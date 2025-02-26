def anagrame(s, t):
    if len(s) != len(t):
        return False

    permutare_p = {i: i for i in range(len(s))}

    for i in range(len(s)):
        poz_litera_s = t.find(s[i])
        if poz_litera_s == -1:
            return False
        else:
            # Modificam permutarea_p
            permutare_p[i] = poz_litera_s

            # Inlocuim litera gasita in t cu un spatiu
            poz_litera_t = permutare_p[poz_litera_s]
            t = t[:poz_litera_t] + ' ' + t[poz_litera_t + 1:]

    permutare_q = dict(sorted({v: k for k, v in permutare_p.items()}.items()))

    return permutare_p, permutare_q