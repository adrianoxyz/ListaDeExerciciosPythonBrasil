# 25 - Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

print("########### RESPOSTAS SOBRE O CRIME ##############")
telefonou=input(("Telefonou para vitima:\n S- Sim\n N - Não\n"))
soma = 0

if telefonou == 'S' or telefonou == 's':
    soma = soma + 1
elif telefonou == 'N' or telefonou =='n':
    soma = soma + 0
else:
    print("Reposta Inválida!")

local = input(("Esteve no local do crime:\n S-SIM\n N-NÃO\n"))

if local == 's' or local == 'S':
    soma = soma + 1

elif local == 'n' or local == 'n':
    soma = soma + 0

else:
    print("Resposta Inválida")

moradia = input("Mora perto da vítima:\n S-SIM\n N-Não\n")

if moradia == 's' or moradia == 'S':
    soma = soma + 1

elif moradia == 'n' or moradia == 'N':
    soma = soma + 0

else:
    print("Resposta Inválida!")

devia = input("Devia para a vítima:\n S-SIM\n N-Não\n")

if devia == 's' or devia == 'S':
    soma = soma + 1

elif devia == 'n' or devia == 'N':
    soma = soma + 0

else:
    print("Resposta Inválida!")

trabalhou = input("Já trabalhou com a vítima:\n S-SIM\n N-NÃO\n")

if trabalhou == 'S' or trabalhou == 's':
    soma = soma + 1

elif trabalhou == 'n' or trabalhou == 'N':
    soma = soma + 0

else:
    print("Resposta Inválida")

if soma == 2:
    print("Pessoa Suspeita!")

elif soma == 3 or soma == 4:
    print("Pessoa Cúmplice")

elif soma == 5:
    print("Assassino")

else:
    print("Soma Inválida!")