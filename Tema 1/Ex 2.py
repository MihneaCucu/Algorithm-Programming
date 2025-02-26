def f(A):
    n = len(A)
    if n == 1:
        return A[0]
    return 0

A = list(map(int, input().split()))
d = f(A)
print(d)

#XOR din toate submultimile va da intotdeauna 0. In cazul in care n e 1, atunci XOR nu se aplica.