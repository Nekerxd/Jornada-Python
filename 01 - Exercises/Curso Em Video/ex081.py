#Crie um programa que vai ler vários números e colocar em uma lista.
#Ao final, mostre quantos números foram digitados, a lista de valores ordenada de forma decrescente e se o valor 5 foi digitado e está ou não na lista.

lista = list()
while True:
    lista.append(int(input("Digite um valor: ")))
    resp = " "
    while resp not in "SN":
        resp = str(input("Deseja continuar? [S/N]: ")).strip().upper()[0]
    if resp == "N":
        break
lista.sort(reverse=True)
print(f"Os valores digitados de maneira decrescente:\n{lista}")
print(f"Foram digitados {len(lista)} números.")
if 5 in lista:
    print("O número 5 se encontra presente na lista!")
else:
    print("O número 5 não está presente na lista!")
