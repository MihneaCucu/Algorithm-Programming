n = int(input("n este "))
v = [0]*100
v[0]= int(input("x este "))
d = v[0]
for i in range(n-1):
    v[i]= int(input("x este "))
    d = d^v[i]
print(d)