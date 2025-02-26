n = int(input("n este "))
def ciur(n):
    prim = [True for i in range(n+1)]
    p = 2
    while(p*p<=n):
        if prim[p] == True:
            for i in range(p * p, n + 1, p):
                prim[i] = False
        p = p + 1
    for p in range(2, n + 1):
        if prim[p]:
            print(p)
ciur(n)
