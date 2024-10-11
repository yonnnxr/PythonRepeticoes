n = int(input("Digite o valor de N (número de termos desejado): "))
a, b = 0, 1
print("Sequência de Fibonacci:")
for _ in range(n):
    print(b, end=" ")
    a, b = b, a + b