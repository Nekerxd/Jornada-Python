#Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while. PA (AN = A1 + Termos * Razão). 
a1 = int(input("Qual o primeiro termo da PA? "))
razao = int(input("Qual a razão da PA? "))
cont = 0
while cont < 10:
    an = a1 + cont * razao
    print("{}  ➝  ".format(an), end="")
    cont += 1
print("FIM")
