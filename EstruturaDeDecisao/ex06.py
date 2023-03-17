# 6 - Faça um Programa que leia três números e mostre o maior deles.

num1 = int(input("Digite o primeiro número a ser comparado:\n"))
num2 = int(input("Digite o segundo número a ser comparado:\n "))
num3 = int(input("Digite o terceiro número a ser comparado\n"))

if num1 > num2 and num1 > num3:
    print("O número %i é o maior" %num1)

elif num2 > num1 and num2 > num3:
    print("O número %i é o maior" %num2)

else:
    print("O número %i é o maior" %num3)