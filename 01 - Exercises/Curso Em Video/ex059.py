#Crie um programa que leia dois valores e mostre um menu na tela:[1] somar,[2] multiplicar,[3] maior,[4] novos números,[5] sair do programa.
#Seu programa deverá realizar a operação solicitada em cada caso.

num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))

opcao = 0
while opcao != 5:
    print("Escolha uma das opções do menu: ")
    opcao = int(input("""\n[ 1 ] somar \n[ 2 ] multiplicar \n[ 3 ] maior \n[ 4 ] novos números \n[ 5 ] sair do programa \n"""))
    if opcao == 1:
        soma = num1 + num2
        print("A soma dos números {} e {} é igual a {}".format(num1, num2, soma))
    elif opcao == 2:
        multi = num1 * num2
        print("O produto dos números {} e {} é igual a {}".format(num1, num2, multi))    
    elif opcao == 3:
        if num1 > num2:
            maior = num1
            print("O maior entre {} e {} é o número {}".format(num1, num2, maior))
        elif num1 < num2:
            maior = num2
            print("O maior entre {} e {} é o número {}".format(num1, num2, maior))
        else:
            print("Os dois números são iguais.")
    elif opcao == 4:
        print("Informe os novos números: ")
        num1 = int(input("Digite o primeiro valor: "))
        num2 = int(input("Digite o segundo valor: "))
    elif opcao == 5:
        print("Finalizando...")
    else:
        print("Opção inválida. Tente novamente")
    print("=-"*20)
