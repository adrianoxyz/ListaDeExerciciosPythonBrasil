# 14 - Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

for i in range (1,11):
    numero = int(input("Entre com o número: "))
    if numero % 2 == 0:
        par = numero
        print("Número Par")

    else:
        impar = numero 
        print("Número Impar")