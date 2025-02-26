f = open("cuvinte.txt", "r")
f2 = open("rime.txt", "w")
d ={}
s = f.readline()
p = int(input("p = "))
while s != "":
    L = s.strip("\n").split()
    for x in L:
        z = x[len(x)-p:]
        if z in d:
            d[z].append(x)
        else:
            d1 = {z:[x]}
            d.update(d1)
    s = f.readline()
f.close()
f2.close()