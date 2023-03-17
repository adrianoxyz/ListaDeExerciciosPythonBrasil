# 8 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês.

salarioHora = float(input("Quanto você ganha por hora: "))
horasTrabalhadasMes = float(input("Quantas horas trabalhadas no mês: "))

salarioFinal = salarioHora * horasTrabalhadasMes

print("O salário final é: %.3f" %salarioFinal)
