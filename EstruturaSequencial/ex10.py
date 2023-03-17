# 10 - Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

grausCelsius = float(input("Qual a temperatura em Celsius: "))
grausFarenheit = (grausCelsius * 1.8) + 32
print("O valor em Graus Farenheit é: %.2f" %grausFarenheit)