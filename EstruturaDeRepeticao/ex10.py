# 10 - Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

a = int(input("Informe um número: "))
b = int(input("Informe outro número: "))

for i in range(a+1,b):
    print(i)