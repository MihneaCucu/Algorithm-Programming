def partiti(valori):
    suma_totala = sum(valori)
    suma_target = suma_totala // 2
    n = len(valori)
    dp = [[0] * (suma_target + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(suma_target + 1):
            if valori[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - valori[i - 1]] + valori[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]

    subset = []
    i, j = n, suma_target
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            subset.append(valori[i - 1])
            j -= valori[i - 1]
        i -= 1

    for valoare in subset:
        valori.remove(valoare)
    return subset, valori

cadouri = [28, 7, 11, 8, 9, 7, 27]
rez = partiti(cadouri)

print("Fratele 1: ", rez[0])
print("Fratele 2: ", rez[1])