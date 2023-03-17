# 7 - Faça um Programa que leia três números e mostre o maior e o menor deles.

a=int(input("Digite o primeiro número: "))
b=int(input("Digite o segundo número: "))
c=int(input("Digite o terceiro número: "))
maior=a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
menor = a
if b < c and b < a:
    menor = b
if c < b and c < a:
    menor = c
print(f"O menor número digitado foi {menor}")
print(f"O maior número digitado foi {maior}")