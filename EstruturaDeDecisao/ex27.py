# 27 - Uma fruteira está vendendo frutas com a seguinte tabela de preços:
# Se o cliente comprar mais de 8 Kg em frutas receberá um desconto de 10% sobre este total. 

kgMorango = float(input("Quantos kg deseja levar de morango?\n"))
kgMaca = float(input("Quantos kg deseja levar de maçâ?\n"))

totalKg = kgMorango + kgMaca

if totalKg > 8:
    descontoPercentual = totalKg * 0.1
    totalComDesconto = totalKg - descontoPercentual
    print("Você pagará somente %.2f" %totalComDesconto,"KG")

else:
    print("Você pagará o valor total comprado: %.2f" %totalKg)