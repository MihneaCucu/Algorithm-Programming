v = [0]*100
n = int(input("Numarul elementelor este: "))
d = 0
v[0] = 0
for i in range(n):
    v[i+1] = float(input("x este: "))
    d1 = v[i+1]-v[i]
    if i>0 and d1>d:
        d = d1
        i1 = i
print(f"Cea mai mare crestere a fost de {d} si zilele au fost {i1} si {i1+1}")