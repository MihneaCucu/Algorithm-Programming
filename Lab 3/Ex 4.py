m = int(input("Introduceți numărul de linii: "))
n = int(input("Introduceți numărul de coloane: "))

A = []

for i in range(m):
    linie = input("Introduceti elementele ").split()
    linie = [int(element) for element in linie]
    A.append(linie)
maxime_pe_linii = []
for linie in A:
    maxim_linie = max(linie)
    maxime_pe_linii.append(maxim_linie)
print(maxime_pe_linii)