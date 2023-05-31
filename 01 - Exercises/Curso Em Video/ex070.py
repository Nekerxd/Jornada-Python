#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. 
#No final, mostre qual é o total gasto na compra, quantos produtos custam mais de R$1000,qual é o nome do produto mais barato.

total = caros = barato = cont = 0
p_barato = ""

while True:
    nome = str(input("Nome do produto: "))
    preco = float(input("Preço: "))
    cont += 1
    total += preco
    if cont == 1 or preco < barato:
        barato = preco
        p_barato = nome
    if preco >= 1000:
        caros += 1
    resp = " "
    while resp not in "SN":
        resp = str(input("Deseja continuar? [S/N]: ")).strip().upper()[0]
    if resp == "N":
        break
    print(p_barato)
print(f"O total gasto na compra foi de R${total:.2f}")
print(f"Dos produtos listados {caros:0} custam mais que R$1000,00")
print(f"O produto mais barato é {p_barato}")