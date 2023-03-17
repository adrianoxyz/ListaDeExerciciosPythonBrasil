# 5- Faça um programa para a leitura de duas notas parciais de um aluno. 
# O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete; 

nota1=float(input("Digite a nota do 1º Bimestre: "))
nota2=float(input("Digite a nota do 2º Bimestre: "))
nota3=float(input("Digite a nota do 4º Bimestre: "))
nota4=float(input("Digite a nota do 5º Bimestre: "))

mediaFinal = (nota1 + nota2 + nota3 + nota4) / 4

if mediaFinal >= 5:
    print ("Aprovado!")
else:
    print("Reprovado!")

print("Nota Final: %.2f" %mediaFinal)