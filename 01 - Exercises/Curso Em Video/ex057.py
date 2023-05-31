# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = "."
while sexo not in "MF":
    sexo = str(input("Qual o seu sexo? [M / F]: ")).strip().upper()[0]
    if sexo not in "MF":
        print("Por favor, digite uma opção válida!")
    sexo = sexo
print("Então você é do sexo {}!".format(sexo))