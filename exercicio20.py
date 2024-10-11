angulo_graus = float(input("Digite o ângulo em graus: "))
pi = 3.14159
angulo_radianos = angulo_graus * pi / 180
seno = 0
numerador = angulo_radianos
denominador = 1
termos = 15
for n in range(termos):
    termo = numerador / denominador
    if n % 2 == 0:
        seno += termo
    else:
        seno -= termo
    numerador *= -1 * angulo_radianos * angulo_radianos
    denominador *= (2 * n + 2) * (2 * n + 3)
print(f"O seno de {angulo_graus} graus é aproximadamente: {seno:.4f}")