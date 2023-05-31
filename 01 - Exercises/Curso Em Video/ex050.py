#Desenvolva um programa que leia seis números inteiros e mostre a soma dos que forem pares
s = 0
for c in range(0,6):
    n = int(input("Digite um número: "))
    if n % 2 == 0:
        s += n
print("A soma dos números pares foi: {}".format(s))