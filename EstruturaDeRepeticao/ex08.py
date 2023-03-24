# 08 - Faça um programa que leia 5 números e informe a soma e a média dos números.

contador = 0
soma = 0
while contador < 5:
    contador +=1
    numero = int(input("Informe um número: "))
    soma += numero
    media = soma / 5

print(f"A soma dos números é {soma}")
print(f"A média dos números é {media}")


    
