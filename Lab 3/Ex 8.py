m = int(input("Introduceți numărul de linii: "))
n = int(input("Introduceți numărul de coloane: "))

A = []
s = 0
for i in range(m):
    A = [int(x) for x in input().split() if int(x)%2 ==0]
    s += len(A)
print(s)
