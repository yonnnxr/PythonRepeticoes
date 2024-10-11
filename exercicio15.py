num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

maior = max(num1, num2)
mmc = maior

while True:
    if mmc % num1 == 0 and mmc % num2 == 0:
        break
    mmc += maior

print(f"O MMC entre {num1} e {num2} é: {mmc}")