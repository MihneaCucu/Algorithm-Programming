n = int(input("n este "))
k = int(input("k este "))
b = int(input("b este "))

mask = 1 << k

if (n & mask) >> k == b:
    print(f"Numarul ramane neschimbat: {n}")
else:
    n = n ^ mask
    print(f"Numarul obtinut: {n}")