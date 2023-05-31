#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
cidade = str(input('Qual o nome da sua cidade? ')).strip()
print('A sua cidade começa com Santo?',cidade[:5].title() == 'Santo')