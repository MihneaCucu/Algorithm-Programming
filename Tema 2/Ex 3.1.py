def grupuri_cuvinte():
    with open("exemplu.txt", "r") as file:
        text = file.read()

    cuvinte = text.split()

    semne_punctuatie = '.,?!:;\'"'
    for semn in semne_punctuatie:
        cuvinte = [cuvant.strip(semn) for cuvant in cuvinte]

    cuvinte = [cuvant.lower() for cuvant in cuvinte]
    grup = {}
    for cuvant in cuvinte:
        lungime = len(cuvant)

        if lungime not in grup:
            grup[lungime] = set()

        grup[lungime].add(cuvant)

    grup = dict(sorted(grup.items(), reverse=True))

    for lungime in grup:
        grup[lungime] = sorted(grup[lungime])

    print(grup)

    with open('grupe_cuvinte.txt', 'w') as file_out:
        for k, v in grup.items():
            file_out.write(f"Lungime {k}: {', '.join(v)}\n")
