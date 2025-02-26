cuvant = input("cuvantul este ")
n = len(cuvant)
c = cuvant.center(10)
print(c)
for i in range(1, len(cuvant)):
    cuvant_taiat = cuvant[i:-i]  #Taie prima si ultima litera
    cuvant_nou = cuvant_taiat.center(10)
    print(cuvant_nou)