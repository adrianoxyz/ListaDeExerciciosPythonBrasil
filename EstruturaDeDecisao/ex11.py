# 11 - As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:

# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

salarioColaborador = float(input("Qual o salário do colaborador: "))

if salarioColaborador >= 280:
    aumentoSalarial = salarioColaborador + (salarioColaborador * 0.2)
    print ("O novo salário é: %.2f" %aumentoSalarial)

elif salarioColaborador > 280 and salarioColaborador < 700:
    aumentoSalarial = salarioColaborador + (salarioColaborador * 0.15)
    print ("O novo salário é: %.2f" %aumentoSalarial)

elif salarioColaborador > 700 and salarioColaborador < 1500:
    aumentoSalarial = salarioColaborador + (salarioColaborador * 0.1)
    print("O novo salário é: %.2f" %aumentoSalarial)

elif salarioColaborador > 1500:
    aumentoSalarial = salarioColaborador + (salarioColaborador * 0.05)
    print ("O novo salário é: %.2f" %aumentoSalarial)
else:
    print("Salário Inválido")

