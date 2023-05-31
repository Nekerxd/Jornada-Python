#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
num = int(input("Digite um número:"))
print("{} é par!".format(num) if num % 2 == 0 else "{} é ímpar!".format(num))
