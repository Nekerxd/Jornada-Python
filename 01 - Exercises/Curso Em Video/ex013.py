#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
sal = float(input('Qual o seu salário? R$'))
aumento = 0.15
print('O novo valor do seu salário após 15% de aumento será R${:.2f}'.format(sal + (sal * aumento)))