# 24 - Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# par ou ímpar;
# positivo ou negativo;

num1 = float(input("Digite o primeiro número a ser verificado: "))
num2 = float(input("Digite o segundo número a ser verificado: "))
operacao = int(input("Qual operação deseja realizar\n 1 - Par ou Ímpar\n 2 - Positivo ou Negativo: "))

if operacao == 1:
    if num1 % 2 == 0:
        print("Número par")
    else:
        print("Número Ímpar")
    if num2 % 2 == 0:
        print("Número Par")
    else:
        print("Número Impar")

elif operacao == 2:
    if num1 > 0:
        print("Número Positivo")
    elif num1 == 0:
        print("Número Neutro")
    else:
        print("Número negativo")
    if num2 > 0:
        print("Número positivo")
    elif num2 == 0:
        print("Número Neutro")
    else:
        print("Número Negativo")
else:
    print("Operação Inválida")    