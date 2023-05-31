#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
from math import trunc, floor
num1 = float(input('Digite um número: '))
print('O número {} tem a parte inteira {}.'.format(num1, trunc(num1)))
print('O número {} tem a parte inteira {}.'.format(num1, floor(num1)))