# 13 - Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

altura = float(input("Digite a sua altura: "))
sexo = input("Qual o seu sexo? Digite h para homem / m para mulher: ")

pesoIdealMulher = (62.1 * altura) - 44.7
pesoIdealHomem = (72.7 * altura) - 58

if sexo == 'm':
    print(pesoIdealMulher)

else:
    print(pesoIdealHomem)