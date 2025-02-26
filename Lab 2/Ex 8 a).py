vocala = "aeiouAEIOU"
s = input("textul este ")
rez = ""
for i in s:
    if i in vocala:
        rez = rez + i + 'p' + i.lower()
    else:
        rez = rez + i
print(rez)