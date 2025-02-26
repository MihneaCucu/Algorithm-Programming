def main():
    s1 = input()
    s2 = input()
    s = ""
    for i in range(len(s1)):
        if s1[i] in "aeiou" and s2[i] in "aeiou":
            s += "*"
        elif s1[i] not in "aeiou" and s2[i] not in "aeiou":
            s += "#"
        else:
            s += "?"
    print(s)

if __name__ == "__main__":
    main()
Copy