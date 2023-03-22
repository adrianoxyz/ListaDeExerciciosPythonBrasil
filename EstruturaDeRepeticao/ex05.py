# 5 - Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

a = float(input("Entre com a taxa populacional:\n "))
b = float(input("Entre com a outra taxa populacional:\n "))
taxaDeCrescimentoA = float(input("Entre com a taxa de crescimento da cidade A:\n"))
taxaDeCrescimentoB = float(input("Entre com a taxa de crescimento da cidade B:\n"))
ano = 0

while a <= b:
    a += a * taxaDeCrescimentoA
    b += b * taxaDeCrescimentoB
    ano += 1

print(f"A cidade A ultrapassará a cidade B em {ano} anos")
