# 14 - Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#Média de Aproveitamento  Conceito
#Entre 9.0 e 10.0        A
#Entre 7.5 e 9.0         B
#Entre 6.0 e 7.5         C
#Entre 4.0 e 6.0         D
#Entre 4.0 e zero        E

nota1 = float(input("Nota do 1º Bimestre: \n"))
nota2 = float(input("Nota do 2º Bimestre: \n"))
nota3 = float(input("Nota do 3º Bimestre: \n"))
nota4 = float(input("Nota do 4º Bimestre: \n"))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media > 0 and media < 4:
    print("Nota: E\n")
    print("Reprovado")

elif media > 4 and media < 6:
    print("Nota: D\n")
    print("Reprovado")

elif media > 6 and media < 7.5:
    print("Nota: C\n")
    print("Aprovado")

elif media > 7.5 and media < 9.0:
    print("Nota: B\n")
    print("Aprovado")

elif media > 9 and media < 10:
    print("Nota: A\n")
    print("Aprovado")

else:
    print("Nota Inválida")