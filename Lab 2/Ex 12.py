def f(text):
    cuv = text.split()
    cuv1 = [cuv.capitalize() for cuv in cuv]
    text1 = ' '.join(cuv1)
    return text1
text = input("textul este ")
print(f(text))