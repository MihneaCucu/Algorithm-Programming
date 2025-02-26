def nr_min_monede(monede, suma):
    monede_min = [float('inf')] * (suma + 1)
    monede_min[0] = 0

    for i in range(1, suma + 1):
        for moneda in monede:
            if i - moneda >= 0:
                monede_min[i] = min(monede_min[i], monede_min[i - moneda] + 1)

    if monede_min[suma] == float('inf'):
        return None

    monede_folosite = []
    suma_curenta = suma

    while suma_curenta > 0:
        for moneda in monede:
            if suma_curenta - moneda >= 0 and monede_min[suma_curenta - moneda] == monede_min[suma_curenta] - 1:
                monede_folosite.append(moneda)
                suma_curenta -= moneda
                break

    return monede_folosite

monede = [7, 5, 1]
suma = 11
rez = nr_min_monede(monede, suma)

if rez is not None:
    print(f"Numărul minim de monede pentru a obține suma {suma} este: {len(rez)}")
    print(f"Monedele folosite sunt: {rez}")
else:
    print(f"Nu există soluție pentru a obține suma {suma} cu monedele date.")