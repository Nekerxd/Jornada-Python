#Ler o ano de nascimento de 7 pessoas e mostre quantas pessoas são 21- e quantas são 21+
from datetime import date
menor = 0
maior = 0
for i in range(1,8):
    nasc = int(input("Insira a idade da {}ª pessoa:".format(i)))
    if date.today().year - nasc < 21 :
        menor += 1
    else:
        maior += 1

print("Das pessoas apresentadas, {} são maiores de 21 anos e {} são menores de 21 anos!".format(maior, menor))