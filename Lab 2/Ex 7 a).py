text = input ("textul este ")
k = int(input("cheia este "))
rez = ""
for i in text:
    if i.isalpha():
        if i.islower():
            cod_i = ord(i) - ord('a')
            nou_cod = (cod_i + k) % 26
            i_cifrat = chr(nou_cod + ord('a'))
            rez += i_cifrat
        elif i.isupper():
            cod_i = ord(i) - ord('A')
            nou_cod = (cod_i + k) % 26
            i_cifrat = chr(nou_cod + ord('A'))
            rez += i_cifrat
    else:
        rez += i
print(rez)