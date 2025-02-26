def palindrom(text):
    return text == text[::-1]
cuv = input("cuvantul este ")
prefmax = ""
sufmax = ""
for i in range(len(cuv)):
    prefix = cuv[:i+1]
    sufix = cuv[-(i+1):]
    if palindrom(prefix) and len(prefix) > len(prefmax):
        prefmax = prefix
    if palindrom(sufix) and len(sufix) > len(sufmax):
        sufmax = sufix
if len(prefmax)>0:
    print(prefmax)
else:
    print("Nu exista prefix palindrom")
if len(sufmax)>0:
    print(sufmax)
else:
    print("Nu exista sufix palindrom")