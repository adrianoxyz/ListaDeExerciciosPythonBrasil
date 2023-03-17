# 23 - Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.

num = float(input("Digite o número a ser verificado: "))
tipoNum = type(num)

if tipoNum == int:
    print("Número inteiro!")

elif tipoNum == float:
    print("Número Decimal!")

else:
    print("Tipo Inválido!")
