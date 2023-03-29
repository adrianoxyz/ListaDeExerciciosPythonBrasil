# 17 - Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

n = int(input("Qual o termo que deseja encontrar fatorial:\n "))

for i in range (1,n-1):
    print(f"{n} x {i}  = ", n ** i )