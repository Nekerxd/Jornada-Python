# calcular valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou o empréstimo é negado
# Perguntar o valor da casa, o salário, pagar em quantos anos.
casa = float(input("Qual o valor da casa a ser financiada? "))
sal = float(input("Qual o valor do seu salário? "))
t = int(input("Em quantos anos deseja pagar? "))
mensal = casa / (t*12)
print("Financiando uma casa de R${:.2f} para pagar em {} anos, a mensalidade será de R${:.2f}".format(casa, t, mensal))
if mensal > (sal*0.3):
    print("\033[0;30;41m Não é possível fazer o empréstimo \033[m")
else:
    print("\033[0;30;42m Financiamento aprovado!\033[m")