#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A"
#E em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input('Digite uma frase: ')).strip().lower()
print('A letra A aparece {} vezes'.format(frase.count('a')))
print('A primeira letra A está na posição {}'.format(frase.find('a')+1))
print('A última letra A está na posição {}'.format(frase.rfind('a')+1))