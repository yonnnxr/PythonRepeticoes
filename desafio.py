nome = str(input("informe o seu nome: "))
while True:
    print(" ")
    print(f"Olá {nome}, Oque deseja fazer hoje")
    print("1. Adição")
    print("2. Substração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair do programa")
    fun = int(input("Qual a função desejada: "))
    if fun == 1:
            A = float(input("Digite um numero: "))
            B = float(input("Digite um numero: "))
            tot = A + B 
            while True:
                SN = str(input("Deseja Continuar: S/N? "))
                if SN == "s" or SN == "S":
                    C = float(input("Digite um numero: "))
                    tot = tot + C
                else:
                    print(tot)
                    break
    if fun == 2:
        A = float(input("Digite um numero: "))
        B = float(input("Digite um numero: "))
        tot = A - B 
        while True:
            SN = str(input("Deseja Continuar: S/N? "))
            if SN == "s" or SN == "S":
                C = float(input("Digite um numero: "))
                tot = tot - C
            else:
                print(tot)
                break
    if fun == 3:
        A = float(input("Digite um numero: "))
        B = float(input("Digite um numero: "))
        tot = A * B 
        while True:
            SN = str(input("Deseja Continuar: S/N? "))
            if SN == "s" or SN == "S":
                C = float(input("Digite um numero: "))
                tot = tot * C
            else:
                print(tot)
                break
    if fun == 4:
        A = float(input("Digite um numero: "))
        B = float(input("Digite um numero: "))
        tot = A / B 
        while True:
            SN = str(input("Deseja Continuar: S/N? "))
            if SN == "s" or SN == "S":
                C = float(input("Digite um numero: "))
                tot = tot / C
            else:
                print(tot)
                break
    if fun == 5:
        print("Obrigado por usar esse programa")
        break
    if fun != 1 or fun != 2 or fun != 3 or fun != 4 or fun != 5:
        print("Essa opção não é valida")