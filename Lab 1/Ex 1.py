x = int(input("x este "))
c = x
ogl = 0
while x != 0:
    ogl = ogl*10+x%10
    x = x//10
if ogl == c:
    print("DA")
else:
    print("NU")