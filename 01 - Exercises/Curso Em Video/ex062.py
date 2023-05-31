#Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
a1 = int(input("Qual o primeiro termo da PA? "))
razao = int(input("Qual a razão da PA? "))
termo = cont = 0
pause = tottermos = 10

while pause != 0:
    while cont < pause+1:
        an = a1 + termo * razao
        print("{}  ➝  ".format(an) if cont < pause else "PAUSA", end="")
        termo += 1
        cont += 1
    pause = int(input("\nQuantos termos você quer mostrar a mais? "))
    tottermos += pause
    cont = 0
print("A progressão foi finalizada. No total foram exibidos {} termos".format(tottermos))
