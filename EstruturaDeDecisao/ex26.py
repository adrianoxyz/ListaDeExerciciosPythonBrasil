# 26 - Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool:
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro
# Gasolina:
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

combustivel = input("Qual gasolina deseja abastecer:\n G-Gasolina\n A-Álcool:\n")
quantidade = float(input("Qual a quantidade de combustível em litros: "))
precoGasolina = 2.5
precoAlcool = 1.9


if combustivel == 'A' or combustivel == 'a':
    if quantidade <= 20:
        quantidadeAlcool = quantidade * precoAlcool
        percentual = (quantidade * precoAlcool) * 0.03
        valorComDesconto = quantidadeAlcool - percentual
        print("Valor total: %.2f" %valorComDesconto,"R$")
    elif quantidade > 20:
        quantidadeAlcool = quantidade * precoAlcool
        percentual = (quantidade * precoAlcool) * 0.05
        valorComDesconto = quantidadeAlcool - percentual
        print("Valor total: %.2f" %valorComDesconto,"R$")
    else:
        print("Opção Inválida!")

if combustivel == 'G' or combustivel == 'g':
    if quantidade <= 20:
        quantidadeGasolina = quantidade * precoGasolina
        percentual = (quantidade * precoGasolina) * 0.04
        valorComDesconto = quantidadeGasolina - percentual
        print("Valor total: %.2f" %valorComDesconto, "R$")
    elif quantidade > 20:
        quantidadeGasolina = quantidade * precoGasolina
        percentual = (quantidade * precoGasolina) * 0.06
        valorComDesconto = quantidadeGasolina - percentual
        print("Valor total: %.2f" %valorComDesconto, "R$")
    else:
        print("Opção Inválida!")