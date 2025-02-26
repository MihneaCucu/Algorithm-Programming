n = int(input("n este "))
d = 0
for i in range(n-1):
    x = int(input("x este "))
    d = d^x^(i+1)
d = d^n
print(d)

