# 27 - Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

turmas = int(input("Digite a quantidade de turmas: "))
turmas +=1
contador = 0

for i in range(1,turmas):
    qtdAlunos = int(input("Digite a quantidade de alunos: "))
    contador += qtdAlunos

turmas -= 1
media = contador / turmas

print(f"A média de alunos por turma é: {media}")