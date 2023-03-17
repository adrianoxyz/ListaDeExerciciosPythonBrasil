# 13 - Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

numeroDia = int(input("Qual o número da semana:\n"))

if numeroDia == 1:
    print("Domingo")

elif numeroDia == 2:
    print("Segunda-Feira")

elif numeroDia == 3:
    print("Terça-Feira")

elif numeroDia == 4:
    print("Quarta-Feira")

elif numeroDia == 5:
    print("Quinta-Feira")

elif numeroDia == 6:
    print("Sexta-Feira")

elif numeroDia == 7:
    print("Sabado")

else:
    print("Data Inexistente")


