ap = [0]*100
V = [int(x) for x in input().split()]
n = V[0]
nr = 0
for x in range(1, n):
    ap[V[x]] += 1
for x in range(1, 100):
    nr = nr + ap[x]//2
print(nr)
