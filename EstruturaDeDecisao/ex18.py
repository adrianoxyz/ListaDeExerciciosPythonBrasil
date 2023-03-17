# 18 - Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

dia = int(input("Qual o dia?\n"))
mes = int(input("Qual o mês?\n"))
ano = int(input("Qual o ano?\n"))

if dia > 0 and dia <= 31 and mes > 0 and mes <= 12 and ano > 0:
    print ("Data Válida!")
    print(str(dia) + '/' + str(mes) + '/' + str(ano))
else:
    print("Data Inválida!")