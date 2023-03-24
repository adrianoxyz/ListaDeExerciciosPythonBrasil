# 07 - Faça um programa que leia 5 números e informe o maior número.

maior = -99999999999999999
i = 1

while i <= 5:
    n=float(input("Digite o número: "))
    if n > maior:
        maior = n
    
    i += 1

print(f"O maior número é o {maior}")