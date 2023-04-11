# 25 - Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

n = int(input("Digite a quantidade de alunos a serem verificadas a idade: "))
alunos = n + 1
soma = 0

for i in range(1,alunos):
    idade = int(input("Digite a idade do aluno: "))
    soma += idade
    media = soma / alunos

if media > 0 and media <= 25:
    print("Turma Jovem!")

elif media > 25 and media <=60:
    print("Turma Adulta!")

elif media > 60:
    print("Turma Idosa!")

else:
    print("Média Inválida!")