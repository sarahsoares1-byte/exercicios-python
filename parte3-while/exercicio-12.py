soma = 0
numero = int(input("digite um número (ou 0 para sair): "))
while numero != 0:
    soma += numero
    numero = int(input("digite um número (ou 0 para sair): "))
print("a soma dos números digitados é:", soma)