# 22 - Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).

num = int(input("Digite o número a ser verificado: "))
resultado = num % 2

if resultado == 0:
    print ("O número %i é par" %num)

elif resultado < 1:
    print ("O número %i é ímpar" %num)

else:
    print("O número %i é ímpar" %num)