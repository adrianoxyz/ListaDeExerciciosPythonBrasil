# 24 - Faça um programa que calcule o mostre a média aritmética de N notas.

n = int(input("Digite a quantidade de notas: "))
contador = n + 1
soma = 0

for i in range (1,contador):
    notas = float(input("Digite as notas:\n "))
    soma += notas
    
media = soma / n
print(f"A média do aluno foi: {media}")

        

