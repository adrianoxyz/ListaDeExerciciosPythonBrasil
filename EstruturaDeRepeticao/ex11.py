# 11 - Altere o programa anterior para mostrar no final a soma dos números.

a = int(input("Informe um número: "))
b = int(input("Informe outro número: "))
soma = 0

for i in range (a,b):
    soma += i

print(soma)