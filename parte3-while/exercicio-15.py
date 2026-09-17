numero = int(input("digite um número: "))
positivos = 0
while numero != 0:
    if numero > 0:
        positivos += 1
    numero = int(input("digite um número: "))
print("os valores positivos são:", positivos)