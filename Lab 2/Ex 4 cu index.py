s = input("s este ")
t = input("t este ")
pozitii = []
start = 0
while start < len(s):
    try:
        pozitie = s.index(t, start)
        pozitii.append(pozitie)
        start = pozitie + len(t)
    except ValueError:
        break
if pozitii:
    print(f"Șirul '{t}' apare ca subșir în șirul '{s}' la pozițiile: {pozitii}")
else:
    print(f"Șirul '{t}' nu apare ca subșir în șirul '{s}'.")