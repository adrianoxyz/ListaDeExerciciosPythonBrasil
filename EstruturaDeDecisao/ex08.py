# 8 - Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

preco1 = float(input("Digite o valor do primeiro produto a ser comparado: "))
preco2 = float(input("Digite o valor do segundo produto a ser comparado: "))
preco3 = float(input("Digite o valor do terceiro produto a ser comparado: "))

menor = preco1

if preco2 < preco1 and preco2 < preco3:
    menor = preco2

if preco3 < preco1 and preco3 < preco2:
    menor = preco3

print ("O valor do menor produto é: %.2f" %menor)