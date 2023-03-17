# 1 - Faça um Programa que peça dois números e imprima o maior deles.

num1 = int(input("Digite um número: "))
num2 = int(input("Digite um segundo número: "))

if num1 > num2:
    print("O número %i é maior" %num1)
else:
    print("O número %i é maior" %num2)