def select_activ(activitati):
    activitati.sort(key=lambda x: x[2], reverse=True)
    activitati_selectate = []
    activitati_selectate.append(activitati[0])

    for i in range(1, len(activitati)):
        activitatea_curenta = activitati[i]
        activitatea_trecuta = activitati_selectate[-1]

        if activitatea_curenta[0] >= activitatea_trecuta[1]:
            activitati_selectate.append(activitatea_curenta)

    return activitati_selectate

def calcul_profit_total(activitati_selectate):
    profit_total = sum(activitate[2] for activitate in activitati_selectate)
    return profit_total

with open("date.in", "r") as f:
    n = int(f.readline())
    activitati = [list(map(float, linie.strip().split())) for linie in f]

activitati_selectate = select_activ(activitati)

with open("date.out", "w") as f:
    f.write(f"Profit total: {calcul_profit_total(activitati_selectate)}\n")
    f.write("Activități selectate: \n")
    for activitate in activitati_selectate:
        f.write(f"{activitate}\n")