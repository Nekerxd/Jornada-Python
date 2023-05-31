#Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
num = int(input("Digite um número para saber seu sucessor e antecessor: "))
print("O sucessor e antecessor de {} é respectivamente {} e {}".format(num, (num+1), (num-1)))