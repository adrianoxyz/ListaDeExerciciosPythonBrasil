# 24 - Faça um programa que calcule o mostre a média aritmética de N notas.

notas = int(input("Quantas notas a serem verificadas: "))
contadorNotas = notas + 1
soma = 0

for i in range(1,contadorNotas):
    nota = float(input("Digite a nota: "))
    soma += nota
    media = soma / notas

print(f"A média de notas foi: {media}")

