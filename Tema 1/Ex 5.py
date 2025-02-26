def f(n):
    nr = 0
    while n > 0:
        if n & 1 == 0:
            nr += 1
        n >>= 1
    return nr

n = int(input("n este "))
print(f(n))