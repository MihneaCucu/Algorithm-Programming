def f(x, y):
    result = x ^ y
    nr = 0
    while result > 0:
        nr += result & 1
        result >>= 1
    return nr

x = int(input("x este "))
y = int(input("y este "))

n = f(x, y)

print(n)
