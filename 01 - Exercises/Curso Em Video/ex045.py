#criar um programa que jogue jokenpô
from random import randint
from time import sleep
objeto = ("Pedra", "Papel", "Tesoura")
pc = randint(0,2)
print("""Suas opções:
[ 0 ]
[ 1 ]
[ 2 ]""")
jogador = int(input("Qual a sua opção? "))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")
sleep(1)
print("Computador jogou {}".format(objeto[pc]))
print("Jogador jogou {}".format(objeto[jogador]))
if pc == jogador:
    print("Empate")
elif pc == 0 and jogador == 1:
    print("Jogador venceu!")
elif pc == 0 and jogador == 2:
    print("Computador venceu!")
elif pc == 1 and jogador == 0:
    print("Computador venceu!")
elif pc == 1 and jogador == 2:
    print("Jogador venceu!")
elif pc == 2 and jogador == 0:
    print("Jogador venceu!")
elif pc == 2 and jogador == 1:
    print("Computador venceu!")
else:
    print("Opção Inválida!")