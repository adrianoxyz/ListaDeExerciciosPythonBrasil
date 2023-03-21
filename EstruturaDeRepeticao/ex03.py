# 03 - Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

nome = input("Digite o nome:\n ")
caracterNome = len(nome)
idade = int(input("Digite a idade:\n "))
salario = float(input("Digite o salário:\n "))
sexo = input("Digite o sexo: F ou M:\n")
estadoCivil = input("Digite o estado civil: S-solteiro C-casado V-viúvo(a) D-divorciado(d)\n")
print(caracterNome)

while caracterNome < 3 and idade < 0 or idade > 150 and salario < 0 and sexo != 'f' or sexo != 'm' and estadoCivil != 'S' and estadoCivil != 'C' and estadoCivil != 'V' and estadoCivil != 'D':
    nome = input("Digite o nome:\n ")
    caracterNome = len(nome)
    idade = int(input("Digite a idade:\n "))
    salario = float(input("Digite o salário:\n "))
    sexo = input("Digite a idade: F ou M:\n")
    estadoCivil = ("Digite o estado civil: S-solteiro C-casado V-viúvo(a) D-divorciado(d)\n")

else:
    print("Informações validadas!")

