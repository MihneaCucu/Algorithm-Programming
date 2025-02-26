def cautare_cuvant (cuv, nume_fis_out, *nume_fis_in):
    with open(nume_fis_out, "w") as rezultat_fisier:
        for nume_fisier in nume_fis_in:
            with open(nume_fisier, 'r', encoding='utf-8') as fisier:
                linii_cu_cuvant = [str(i + 1) for i, linie in enumerate(fisier) if cuv.lower() in linie.lower()]
                if linii_cu_cuvant:
                    rezultat_fisier.write(f"{nume_fisier} {' '.join(linii_cu_cuvant)}\n")
                else:
                    rezultat_fisier.write(f"{nume_fisier} - nu exista cuvantul\n")
cautare_cuvant("floare", "rez.txt", "eminescu.txt", "paunescu.txt")
