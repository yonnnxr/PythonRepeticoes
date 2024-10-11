pes = int(input("Qual o numero de pessoas: "))
for i in range(1, pes+1):
    if pes >= i:
        nome = str(input("Informe seu nome: "))
        sexo = str(input("Informe o seu sexo M/F: "))
        idade = int(input("Informe a idade: "))
        saude = int(input("Informe a condicão que esta a saude: 0/10: "))
        print(nome)
        print(sexo)
        print(idade)
        print(saude)
        if (saude >= 6 and idade >= 18 and sexo == "m" or sexo == "M"):
            print("Voce esta apto para o alistamento")
        else:
            print("Voce nao esta apto para o alistamento")
    else:
        print("O numero de pessoas foi excedido")