#Faça um programa que mostre a tabuada de vários números, um de cada vez para cada valor que for digitado, até que seja digitado um valor negativo.
while True:
    cont = 1
    n = int(input("Insira um número para ver a sua tabuada: "))
    if n < 0:
        break
    print(f"Tabuada de {n}")
    for cont in range(1,11):
        print(f"{n} x {cont} = {n*cont}")
print("Fim")