# 11 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

prod = (num1 * num1) + (num2 / 2)
soma = (num1 * 3) + prod
cubo = prod ** 3

print(prod)
print(soma)
print(cubo)