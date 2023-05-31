#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
valor = float(input('Qual o preço do produto? R$'))
desconto = 0.05
print('O novo valor do produto após 5% de desconto será R${}'.format(valor - (valor * desconto)))