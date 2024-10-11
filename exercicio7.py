num =  int(input("Insira o numero de tentativas: "))
if num <=0:
    print("Não é um numero valido")
for i in range(1, num + 1 ):
    n = int(input("Insira um numero: "))
    
    if i == 1:
        menor = n
    if n < menor:
        menor = n
print(menor)