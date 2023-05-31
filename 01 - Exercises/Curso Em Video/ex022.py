#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas e minúsculas, quantas letras ao todo (sem considerar espaços) e quantas letras tem o primeiro nome.
nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('O seu nome sem espaços contém {}'.format(len(nome) - nome.count(' ')))
nomes = nome.split()
print('Seu primeiro é {} e tem {} letras'.format(nomes[0], len(nomes[0])))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))