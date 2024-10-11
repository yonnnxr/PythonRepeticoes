frase = input("Insira a frase: ")

tam = len(frase)
for i in range(1, tam + 1):
    finv = frase[-i]

    print(finv,end="")

