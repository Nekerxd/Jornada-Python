#Crie um programa que simule um caixa eletrônico, perguntar o valor a ser sacado (inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues
#Considerar cédulas de R$50, R$20, R$10 e R$1

print("="*40)
print("{:^40}".format("Caixa Eletrônico"))
print("="*40)
saque = int(input("Quanto deseja sacar? "))
cont = saque
nota = 50
totnotas = 0
while True:
    if cont >= nota:
        cont -= nota
        totnotas += 1
    else:
        if totnotas > 0:
            print(f"Total de {totnotas} cédulas de R${nota}")
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        totnotas = 0
        if cont == 0:
            break
print("="*40)
print("Volte sempre!")