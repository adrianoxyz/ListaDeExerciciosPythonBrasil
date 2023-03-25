# 13 - Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.

num1 = int(input("Digite a base: "))
num2 = int(input("Digite o expoente: "))

resultado = num1 ** num2
print(f"O {num1} elevado a {num2} é: {resultado}")

