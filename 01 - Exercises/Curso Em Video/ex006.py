#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
num = int(input("Digite um número: "))
print("O dobro de {} é {}, seu triplo é {} e a sua raiz quadrada é {:.2f}".format(num, (num*2), (num*3), pow(num, (1/2))))