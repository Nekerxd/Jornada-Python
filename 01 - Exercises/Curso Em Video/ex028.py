#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
n = randint(0, 5)
num = int(input('Adivinhe o número que o computador pensou de 0 a 5: '))
print('Você venceu! Eu pensei no número {}'.format(n) if n == num else 'Você perdeu! Eu pensei no número {}'.format(n))
