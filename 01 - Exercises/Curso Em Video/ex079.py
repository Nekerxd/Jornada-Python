#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
#Caso o número já exista lá dentro, ele não será adicionado.
#No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = list()
while True:
    num = int(input("Digite um valor: "))
    if num not in lista:
        lista.append(num)
        print("Número cadastrado com sucesso.")
    else:
        print("Número duplicado, não é possível cadastrá-lo.")
    resp = " "
    while resp not in "SN":
        resp = str(input("Deseja continuar? [S/N]: ")).strip().upper()
    if resp == "N":
        break
print("Os números cadastrados em ordem crescente são: ")
for n in sorted(lista):
    print(f"{n}, " if n != len(lista) else f"{n}.", end=" ")
