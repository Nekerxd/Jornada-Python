#refazer o 009 de tabuada, agora com laço for
n1 = int(input('Digite um número para ver a sua tabuada: '))
for c in range(0,11):
    print('{} x  {:2} = {}'.format(n1, c, n1*c))
