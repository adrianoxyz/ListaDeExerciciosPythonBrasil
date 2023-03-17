# 9 - Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

grausFarenheit = float(input("Qual o valor em graus Farenheit: "))
celsius = 5 * ((grausFarenheit - 32) / 9)
print("O valor em Graus Celsius é: %.3f" %celsius)