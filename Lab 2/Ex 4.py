s = input("s este ")
t = input("t este ")
pozitii = []
start = 0
while True:
    pozitie = s.find(t, start)
    if pozitie == -1:
        break
    pozitii.append(pozitie)
    start = pozitie + 1
if pozitii:
    print(f"Șirul '{t}' apare ca subșir în șirul '{s}' la pozițiile: {pozitii}")
else:
    print(f"Șirul '{t}' nu apare ca subșir în șirul '{s}'.")