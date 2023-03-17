# 1 - Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

num = int(input("Digite um número: "))
if num > 0:
    print("Número positivo")
elif num == 0:
    print("Número neutro")
else:
    print("Número negativo")