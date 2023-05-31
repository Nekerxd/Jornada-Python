#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
real = float(input('Quanto você tem na sua carteira? R$'))
dolar = real / 3.27
print('Com R${:.2f} pode comprar U${:.2f}'.format(real, dolar))