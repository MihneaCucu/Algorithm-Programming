def gaseste_submultime(data, M):
    n = len(data)
    dp = [[False] * (M + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, M + 1):
            dp[i][j] = dp[i - 1][j] or (j >= data[i - 1] and dp[i - 1][j - data[i - 1]])

    submultime = []
    i, j = n, M
    while i > 0 and j > 0:
        if dp[i][j] and not dp[i - 1][j]:
            submultime.append(data[i - 1])
            j -= data[i - 1]
        i -= 1

    return submultime[::-1]

with open("date.in", "r") as f:
    n = int(f.readline())
    numere = list(map(int, f.readline().split()))
    M_cautat = int(f.readline())

rezultat = gaseste_submultime(numere, M_cautat)

with open("date.out", "w") as f:
    if rezultat:
        f.write("Există o submulțime cu suma " + str(M_cautat) + ": " + " ".join(map(str, rezultat)))
    else:
        f.write("Nu există o submulțime cu suma " + str(M_cautat))
