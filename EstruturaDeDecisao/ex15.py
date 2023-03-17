# 15 - Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;

a = float(input("Digite o lado a do triângulo: \n"))
b = float(input("Digite o lado b do triângulo: \n"))
c = float(input("Digite o lado c do triângulo: \n"))

if a != b or a != c or b !=c:
    print("Triângulo Escaleno")

elif a == b and a == c and b == c:
    print("Triângulo Equilátero")

elif a == b or a == c or b == c:
    print("Triângulo Isósceles")

else:
    print("Triângulo Inexistente")

