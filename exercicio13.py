#while True:
#    n = int(input("insira um numero: "))
#    if n >= 0:
#        if (int(n**0.5)) == (n**0.5):
#            print("O número é um quadrado perfeito.")
#        else:
#            print("O número não é um quadrado perfeito.")
#    else:
#        print("O programa foi encerrado")

while True:
    n = int(input("insira um numero: "))
    if n >= 0:
        for i in range(1, n):
           print("O número é um quadrado perfeito.")
        else:
            print("O número não é um quadrado perfeito.")
    else:
        print("O programa foi encerrado")
