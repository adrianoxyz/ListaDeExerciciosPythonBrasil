# 2 - Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

nome=input("Digite o nome:\n")
senha=input("Digite uma senha:\n ")

while nome == senha:
    print("O nome e senha devem ser diferentes!")
    nome=input("Digite o nome:\n")
    senha=input("Digite a senha:\n")

else:
    print("Login registrado!")