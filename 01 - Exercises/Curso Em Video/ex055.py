#Ler o peso de 5 pessoas e mostre qual foi o maior e o menor peso lido

peso_maior = 0
peso_menor = 0
leve = ""
pesado = ""

for i in range (1,6):
    print("------ {}ª Pessoa ------".format(i))
    nome = str(input("Nome: "))
    peso = float(input("Peso: "))
    if peso > peso_maior:
        peso_maior = peso
        pesado = nome
    if i == 1:
        peso_menor = peso
    if peso < peso_menor:
        peso_menor = peso
        leve = nome

print("A pessoa com o menor peso é {} com {:.1f}Kg".format(leve, peso_menor))
print("A pessoa com o maior peso é {} com {:.1f}Kg".format(pesado, peso_maior))
