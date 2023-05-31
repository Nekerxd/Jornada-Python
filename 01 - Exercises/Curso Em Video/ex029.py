#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
#A multa vai custar R$7,00 por cada Km acima do limite.
velo = int(input("Qual é a velocidade atual do carro? "))
if velo > 80:
    print("MULTADO! Você excedeu o limite permitido de 80Km/h \n Você deve pagar uma multa de R${}!".format((velo-80)*7))
else:
    print("A velocidade está OK, boa viagem!")