num = int(input("Insira o numero de repetiçoes: "))
if num <= 0:
    print("não é um numero valido")
for i in range(1,num+1):
    n = int(input("Insira o numero: "))

    if i == 1:
        tot = n
    if i >= num:
        tot = tot + n
soma = tot / num
print(soma)