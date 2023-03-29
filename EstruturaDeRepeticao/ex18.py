# 18 - Faça um programa que, dado um conjunto de N números, determine a soma dos valores.

n = int(input("Digite a quantida de número desejados: "))
n1 = n + 1
soma = 0

for i in range (1,n1):
    numero = int(input("Digite o número: "))
    soma += numero
    print("A soma dos números foi: ", soma)