#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
opcao = ""
correta = soma = menor = maior = cont = 0
while opcao in "Ss":
    num = int(input("Digite um número: "))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num < menor:
            menor = num
        if num > maior:
            maior = num
    correta = 0
    while correta == 0:
        opcao = str(input("Deseja continuar rodando o programa? [S/N]: ")).strip().upper()
        if opcao not in "SsNn":
            print("Opção Inválida. Tente novamente.")
            correta = 0
        elif opcao in "SsNn":
            correta = 1
media = soma/cont
print("Você digitou {} números e a média foi {:.2f}".format(cont, media))
print("O maior valor foi {} e o menor foi {}".format(maior, menor))
