#Ler vários inteiros até que o valor 999 seja digitado e fazer a soma de todos valores, quantos foram digitados (desconsiderando o flag)
cont = soma = 0

while True:
    n = int(input("Digite um valor: "))
    if n == 999:
        break
    soma += n
    cont += 1
print(f"A soma dos {cont} valores digitados é igual a {soma}")