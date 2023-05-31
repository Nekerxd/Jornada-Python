#ler nome, idade e sexo de 4 pessoas, no final mostrar a média de idade do grupo, nome do homem mais velho, e quantas mulheres tem menos de 20 anos.

velho = ""
idade_maior = 0
media_idade = 0
mulheres_menor = 0

for i in range(1,5):
    print("------ {}ª Pessoa ------".format(i))
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sex = str(input("Sexo [M / F]: ")).strip()
    if sex in "Ff" and idade < 20:
        mulheres_menor += 1
    if sex in "Mm" and idade > idade_maior:
        idade_maior = idade
        velho = nome
    media_idade += idade

media_idade = media_idade / 4
print("O homem mais velho se chama {} e tem {} anos".format(velho, idade_maior))
print("Existem {} mulheres com menos de 20 anos.".format(mulheres_menor))
print("A média de idade do grupo é {:.2f}".format(media_idade))
