# 20 - Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
# A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
# A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
# A mensagem "Aprovado com Distinção", se a média for igual a 10.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a primeira nota: "))
nota3 = float(input("Digite a primeira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print("Aprovado!\n Nota: %.2f" %media)

elif media < 7:
    print("Reprovado!\n Nota: %.2f" %media)

elif media == 10:
    print("Aprovado com distinção!\n Nota: %.2f" %media)

else:
    print("Nota Inválida!")

