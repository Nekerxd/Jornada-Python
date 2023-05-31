#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
sal = float(input("Digite seu salário: R$ "))
print("Com o aumento de 10% vocé passa a receber R${:.2f}".format(sal * 0.1 + sal) if sal > 1250 else "Com o aumento de 15% vocé passa a receber R${:.2f}".format(sal * 0.15 + sal))