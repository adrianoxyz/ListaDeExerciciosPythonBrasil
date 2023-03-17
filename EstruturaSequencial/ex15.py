# 15 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.

impostoDeRenda = 0.11
inss = 0.08
sindicato = 0.05
salarioHora=float(input("Quanto ganha por hora? "))
horasTrabalhadasMes=float(input("Quantas horas trabalha por mês? "))

salarioBruto = salarioHora * horasTrabalhadasMes
pagInss = salarioBruto * inss
pagImpostoDeRenda = salarioBruto * impostoDeRenda
pagSindicato = salarioBruto * sindicato

print("O salário bruto é: %.3f" %salarioBruto)
print("O desconto do INSS é: %.2f" %pagInss)
print("O desconto do Imposto de Renda é: %.2f" %pagImpostoDeRenda )
print("O desconto do Sindicato é: %.2f" %pagSindicato)