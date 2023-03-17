# 9 - Faça um Programa que leia três números e mostre-os em ordem decrescente.

primeiro=int(input("Digite o primeiro numero a ser comparado: "))
segundo=int(input("Digite o primeiro segundo a ser comparado: "))
terceiro=int(input("Digite o primeiro terceiro a ser comparado: "))

print(primeiro, '-', segundo, '-', terceiro)

if terceiro > segundo:
    aux = terceiro
    terceiro = segundo
    segundo = aux

if segundo > primeiro:
    aux = segundo
    segundo = primeiro
    primeiro = aux

if terceiro > segundo:
    aux = terceiro
    terceiro = segundo
    segundo = aux

print(primeiro, '-', segundo, '-', terceiro)