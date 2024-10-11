num =  int(input("Insira o numero para saber a tabuada: "))
if num <= 0:
    print("Esse numero nao e valido")
controle = 10
for i in range(1, controle+1):
    if i == 1:
        tot = num
        print(tot)
    if i < controle:
        tot = tot + num
        print(tot)