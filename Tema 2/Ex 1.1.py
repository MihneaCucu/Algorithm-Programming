def anagrame (s1, s2):
    if len(s1) != len(s2):
        return False
    fr = [0]*256
    for char in s1:
        fr[ord(char)] += 1
    for char in s2:
        fr[ord(char)] -= 1
    for count in fr:
        if count != 0:
            return 0
    return 1
s1 = "ana are mere"
s2 = "erem rea naa"

if anagrame(s1, s2):
    print("Sirurile sunt anagrame")
else:
    print("Sirurile nu sunt anagrame")