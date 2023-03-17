# 3 - Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = input("Digite o sexo: M - Masculino\n F - Feminino\n")

if sexo == 'M':
    print("Sexo Masculino!")

elif sexo == 'F':
    print("Sexo Feminino!")

else:
    print("Sexo Inválido!")
