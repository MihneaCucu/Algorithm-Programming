s = input("Numele este: ")
n = len(s)
if s[0].isupper():
    print(s[0], end="")
for i in range(1, n):
    if s[i].isupper() and s[i - 1] == ' ':
        print(s[i], end="")