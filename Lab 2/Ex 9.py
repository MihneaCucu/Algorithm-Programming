prop = input("propozitia este ")
s = 0
i = 0
while i<len(prop):
    if prop[i]>='0' and prop[i]<='9':
        x = 0
        while prop[i]>='0' and prop[i]<='9' and i<len(prop):
            x = x*10 + int(prop[i])
            i = i +1
        s = s + x
    else:
        i = i + 1
print(f"{s} RON")
