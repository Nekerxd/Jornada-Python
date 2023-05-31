# Desenvolva um programa que pergunte a distância de uma viagem em Km. 
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
km = float(input("Qual será a distância da viagem: "))
price = km * 0.5 if km <= 200 else km * 0.45
print("Você está prestes a começar uma viagem de {}Km.\n E o preço da passagem será R${:.2f}.".format(km, price))