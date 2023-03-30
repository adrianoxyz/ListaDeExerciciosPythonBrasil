# 21 - Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.

n = int(input("Digite o número:\n"))

if n != 1:
    if n % 2 != 0:
        print("Número primo! ")

    elif n == 2:
        print("Número primo!")

    else:
        print("Número composto!")

else:
    print("Número primo")