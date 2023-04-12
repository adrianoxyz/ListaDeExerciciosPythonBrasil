# 28 - Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

qtdCds = int(input("Digite a quantidade de Cd's: "))
qtdCds += 1
contador = 0

for i in range(1, qtdCds):
    valorCds = float(input("Digite o valor de cada Cd: "))
    contador += valorCds

qtdCds -= 1
media = contador / qtdCds
print(f"O valor gasto em média em cada CD foi: {media}")