'''x > 1
coeficienti descrescator

0 < x <= 1
coeficienti crescator

x <= -1
A are nr par de elemente -> cea mai mare putere impara
A {1 2 3 4}
st dr st+1 dr-1 ... pana st = dr


A are nr impar de elemente -> cea mai mare putere para
A {1 2 3 4 5}
dr st dr-1 st+1 pana st = dr
vedem cum facem cu cel din mijloc

-1 < x < 0
A are nr par de elemente -> cea mai mare putere impara
A 1 2 3 4
int st [1 2]
int dr [3 4]
2 3 1 4

int st [1 2 3]
int dr [4 5 6]

3 4 2 5 1 6

A are nr impar de elemente -> cea mai mare putere para
int st [1 2]
int dr [4 5 6]
4 2 5 1 6
'''


def polmax(A, x):
    n = len(A)
    A = sorted(A)
    coeficienti = []
    if x > 1:
        coeficienti = sorted(A, reverse=True)
    elif 0 < x <= 1:
        coeficienti = A
    elif x <= -1:
        if n % 2 == 0:
            st = 0
            dr = n-1
            while st < dr:
                coeficienti.append(A[st])
                coeficienti.append(A[dr])
                st += 1
                dr -= 1
        else:
            st = 0
            dr = n - 1
            while st < dr:
                coeficienti.append(A[dr])
                coeficienti.append(A[st])
                st += 1
                dr -= 1
            coeficienti.append(A[dr])
    else:
        interval1 = A[n//2-1::-1]
        interval2 = A[n//2::]
        k = n//2
        for i in range(k):
            if n % 2 == 0:
                coeficienti.append(interval1[i])
                coeficienti.append(interval2[i])
            else:
                coeficienti.append(interval2[i])
                coeficienti.append(interval1[i])
        if n % 2 != 0:
            coeficienti.append(interval2[-1])
    return coeficienti

print(polmax([2,-1,7,3],2))










