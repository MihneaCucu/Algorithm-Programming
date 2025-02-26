s = 1
with open("test.in", "r") as fisier:
    for linie in fisier:
        numere = linie.split("=")
        rezultat = numere[1].strip()
        op1,op2 = numere[0].split("*")
        rezultat = int(rezultat)
        op1 = int(op1)
        op2 = int(op2)
        rez_c = op1*op2
        with open("test.out", "a") as fisier2:
            if rez_c == rezultat:
                fisier2.write(f"{op1}*{op2}={rezultat} Corect\n")
                s +=1
            else:
                fisier2.write(f"{op1}*{op2}={rezultat} Gresit {rez_c}\n")
with open("test.out", "a") as fisier2:
    fisier2.write(f"Nota {s}")

