n = int(input("nr elem este "))
if n%2==0:
    x = int(input("x este "))
    y = int(input("x este "))
    if x<y:
        mini=x
        maxi=y
    else:
        mini=y
        maxi=x
    for i in range((n-2)//2):
        x = int(input("x este "))
        y = int(input("x este "))
        if x<y:
            if x<mini:
                mini=x
            if y>maxi:
                maxi=y
        else:
            if y<mini:
                mini=y
            if x>max:
                maxi=x
    print(f"mini este {mini} si maxi este {maxi}")
else:
    x = int(input("x este "))
    mini=x
    maxi=x
    for i in range((n-1)//2):
        x = int(input("x este "))
        y = int(input("x este "))
        if x<y:
            if x<mini:
                mini=x
            if y>maxi:
                maxi=y
        else:
            if y<mini:
                mini=y
            if x>maxi:
                maxi=x
    print(f"mini este {mini} si maxi este {maxi}")