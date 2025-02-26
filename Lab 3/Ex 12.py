n = int(input("n este "))

matrice = [[j + i*n +1 for j in range(n)] for i in range(n)]

for rand in matrice:
    print(rand)