# 17 - Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

ano = float(input("Qual o ano a ser verificado:\n "))

if ano % 4 == 0 and ano % 100 != 0:
    print ("Ano Bissexto")

else:
    print ("Ano não Bissexto")