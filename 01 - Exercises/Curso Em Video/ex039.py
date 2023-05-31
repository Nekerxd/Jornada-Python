#Ler o ano de nascimento, se vai se alistar, se é a hora de se alistar, se já passou do tempo de alistar, deve mostrar quanto tempo falta ou que passou do prazo
from datetime import date
data = date.today().year
nasc = int(input("Digite o seu ano de nascimento: "))
idade = data - nasc

if idade <= 17:
    print("Ainda falta {} anos para você se alistar".format(18 - idade))
elif idade == 18:
    print("Você deve se alistar nesse ano!")
else:
    print("Você já passou do ano de alistamento a {} anos".format(idade - 18))