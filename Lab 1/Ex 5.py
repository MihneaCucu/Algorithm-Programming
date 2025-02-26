a = int(input("a este "))
b = int(input("b este "))
x = 0
y = 1
z = x+y
while z<a:
    x=y
    y=z
    z=x+y
if z<=b:
    print(z)
else:
    print("Nu exista")