#Ler um número inteiro e dizer se ele é ou não um número primo.
from calendar import c


num = int(input("Insira um número: "))
k = 0
for i in range (1, num + 1):
    if (num % i == 0):
        print('\033[33m', end='')
        k+=1
    else:
        print('\033[31m', end='')
    print('{} '.format(i), end='')
print('\n\033[mO número {} foi divisível {} vezes'.format(num, k))
if k == 2:
    print('E por isso ele é primo!')
else:
    print('E por isso ele não é primo!')