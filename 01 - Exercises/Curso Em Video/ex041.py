#Ler ano de nascimento e mostrar categoria
# <= 9 mirim, > 9 <= 14 infantil, > 14 <= 19 junior, == 20 sênior, > 20 master
from datetime import date
nasc = int(input("Digite o seu ano de nascimento: "))
idade = date.today().year - nasc
if idade <= 9:
    print("Mirim")
elif idade > 9 and idade <= 14:
    print("Infantil")
elif idade > 14 and idade <=19:
    print("Júnior")
elif 19 <= idade < 25:
    print("Sênior")
else:
    print("Master")