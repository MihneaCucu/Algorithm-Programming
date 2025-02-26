l1 = int(input("lungimea este "))
l2 = int(input("latimea este "))
p = l1*l2
r = l1%l2
while r != 0:
    l1=l2
    l2=r
    r=l1%l2
print(f"mesterul are nevoie de {p//(l2*l2)} placi de gresie cu lungimea {l2}")