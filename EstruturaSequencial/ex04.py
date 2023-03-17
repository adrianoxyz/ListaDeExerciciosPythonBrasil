# 4 - Faça um Programa que peça as 4 notas bimestrais e mostre a média.
nota1=float(input("Digite a nota do 1º bimestre: "))
nota2=float(input("Digite a nota do 2º bimestre: "))
nota3=float(input("Digite a nota do 3º bimestre: "))
nota4=float(input("Digite a nota do 4º bimestre: "))

mediaFinal = (nota1 + nota2 + nota3 + nota4) / 4
print("A nota final é: %.2f" %mediaFinal)