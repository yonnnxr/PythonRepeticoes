N = int(input("Digite o valor de N: "))
H = 0

for i in range(1, N + 1):
    termo = 1 / i
    if i % 2 == 0:  
        H -= termo
    else:            
        H += termo

print(f"O valor de H para N = {N} é: {H:.4f}")