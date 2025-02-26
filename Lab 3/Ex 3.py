V1 = [int(x) for x in input().split()]
V2 = [int(x) for x in input().split()]
reun = []
inter = []
i = 0
j = 0
while i < len(V1) and j < len(V2):
    if V1[i] < V2[j]:
        reun.append(V1[i])
        while i < len(V1) - 1 and V1[i] == V1[i + 1]:
            i += 1
        i += 1
    elif V2[j] < V1[i]:
        reun.append(V2[j])
        while j < len(V2) - 1 and V2[j] == V2[j + 1]:
            j += 1
        j += 1
    else:
        reun.append(V1[i])
        inter.append(V1[i])
        while i < len(V1)-1 and V1[i] == V1[i+1]:
            i += 1
        while j < len(V2) - 1 and V2[j] == V2[j + 1]:
            j += 1
        i += 1
        j += 1

while i < len(V1):
    reun.append(V1[i])
    while i < len(V1)-1 and V1[i] == V1[i + 1]:
        i += 1
    i+= 1
while j < len(V2):
    reun.append(V2[j])
    while j < len(V2)-1 and V2[j] == V2[j + 1] :
        j += 1
    j+= 1

print(reun, '\n')
print(inter)