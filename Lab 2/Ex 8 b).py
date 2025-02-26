textp = input("textul in pasareasca este ")
text = ""
i = 0
vocala = "aeiouAEIOU"
while i < len(textp):
    if i < len(textp)-2 and textp[i] in vocala and textp[i+1] == 'p' and textp[i+2].lower() == textp[i].lower():
        text += textp[i]
        i = i+3
    else:
        text += textp[i]
        i = i+1
print(text)
