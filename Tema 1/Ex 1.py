sir = list(map(int, input().split()))
aparitii = {}
for valoare in sir:
    if valoare in aparitii:
        aparitii[valoare] += 1
    else:
        aparitii[valoare] = 1
for valoare, numar_aparitii in aparitii.items():
    if numar_aparitii % 2 == 1:
        valoare_impara = valoare
        break
print(valoare_impara)
