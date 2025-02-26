def citeste_lista():
    nr = int(input("Nr este "))
    lista = []
    for i in range(nr):
        element = int(input("Elementul este "))
        lista.append(element)
    return lista

def gaseste (s, x, i = None, j = None):
    subsecventa = s[i:j]
    for index, element in enumerate(subsecventa):
        if element > x:
            return index + (i if i is not None else 0)
    return -1

def este_sortata_descresc (lista):
    for i in range(len(lista)-1):
        if gaseste(lista, lista[i], i+1) != -1:
            return False
    return True

lista = citeste_lista()

if este_sortata_descresc(lista):
    print("DA")
else:
    print("NU")