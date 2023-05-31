#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import radians, sin, tan, cos
rad = float(input('Digite um ângulo: '))
ang = radians(rad)
print('Para o ângulo {} temos: \nSeno: {:.2f} \nCosseno: {:.2f} \nTangente: {:.2f}'.format(ang, sin(ang), cos(ang), tan(ang)))