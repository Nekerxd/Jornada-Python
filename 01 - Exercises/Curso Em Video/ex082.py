#Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
#Ao final, mostre o conteúdo das três listas geradas.

valores = list()
pares = list()
impares = list()
while True:
    valores.append(int(input("Digite um valor: ")))
    resp = " "
    while resp not in "SN":
        resp = str(input("Deseja continuar? [S/N]: ")).strip().upper()[0]
    if resp == "N":
        break
for ind, num in enumerate(valores):
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(f"A lista completa é {valores}")
print(f"A lista de pares é {pares}")
print(f"A lista de ímpares é {impares}")