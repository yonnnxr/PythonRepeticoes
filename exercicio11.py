num = int(input("Informe a quantidade de numeros: "))
for i in range(1, num + 1):
    n = int(input("Insira o numero: "))
    if i <= num:
        if n > 0:
            print("Esse numero é positivo")
        elif n < 0:
            print("Esse numero é negativo")
        else:
            print("Esse numero é zero")