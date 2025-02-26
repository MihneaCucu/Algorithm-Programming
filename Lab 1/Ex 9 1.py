'''Se citesc două numere întregi n și k și o valoare binară b (0 sau 1). Să se afișeze numărul obținut din n
setând al k-lea bit (din dreapta) din reprezentarea binară a lui n la valoarea b. De exemplu, reprezentarea binară a
numărului 600 este 0b1001011000. Pentru n=600,  k=2 și b=1 se obține 0b1001011010, adică numărul 602. Pentru n=600,
k=2 și b=0 numărul rămâne neschimbat, deoarece al doilea bit al lui n avea deja valoarea 0.'''
n = int(input("n este "))
k = int(input("k este "))
b = int(input("b este "))
def setare_bit(n, k, b):
    #Creare masca biti
    masca = b << (k-1)
    #Operatie sau
    rez = n | masca
    return rez
print(setare_bit(n, k, b))

