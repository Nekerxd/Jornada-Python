#Faça um programa que jogue par ou impar com o computador e será interrompido quando o jogador perder, mostrando quantas vezes seguidas você venceu
from random import randint

cont = 0
while True:
    cpu = randint(9,10)
    jogador = int(input("Escolha um número: "))
    imp_par = str(input("Ímpar ou Par? [I/P]: ")).strip().upper()[0]
    tot = jogador + cpu
    print(f"Você jogou {jogador} e o computador {cpu}, o total deu {tot}.", end=" ")
    if tot %2 == 0:
        result = "P"
    else:
        result = "I"
    print("Deu Par" if result == "P" else "Deu Ímpar")
    if result == "P" and imp_par == "P":
        print("Jogador venceu!")
        cont += 1
    elif result == "I" and imp_par == "I":
        print("Jogador venceu!")
        cont += 1
    else:
        print("O computador venceu")
        break
print(f"Parabéns você teve um streak de {cont} vitórias!!" if cont >= 1 else "Infelizmente você não teve nenhuma vítória! Boa sorte na próxima vez.")