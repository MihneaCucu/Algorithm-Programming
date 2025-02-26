n = int(input("n este "))
v = [0]*10
while n > 0:
    v[n % 10] = v[n % 10]+1
    n = n//10
for i in range(9, 0, -1):
    for j in range(v[i]):
        print(i, end="")
print("\n")
if v[1] != 0:
    for j in range(v[1]):
        print(1, end="")
if v[0] != 0:
    for j in range(v[0]):
        print(0, end="")
for i in range(2, 9):
    for j in range(v[i]):
        print(i, end="")