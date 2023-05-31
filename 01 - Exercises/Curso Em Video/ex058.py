#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. 
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

n = randint(0, 10)
tentativas = 0
acertou = False
while not acertou:
    num = int(input('Adivinhe o número que o computador pensou de 0 a 10: '))
    tentativas += 1
    if num == n:
        print("Parabéns você acertou, o número era {}. Você levou {} tentativas para acertar.".format(n, tentativas))
        acertou = True
    elif num > n:
        print("Número muito alto, tente outro.")
    else:
        print("Número muito baixo, tente outro.")
