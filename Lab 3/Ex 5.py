m = int(input("Introduceți numărul de linii: "))
n = int(input("Introduceți numărul de coloane: "))
k = int(input("Introduceti k: "))

A = []

for i in range(k+1):
    linie = input("Introduceti elementele ").split()
    linie = [int(element) for element in linie]
    A.append(linie)
linie = [0]*n
A.append(linie)
for i in range(k+2,m+1):
    linie = input("Introduceti elementele ").split()
    linie = [int(element) for element in linie]
    A.append(linie)
print(A)