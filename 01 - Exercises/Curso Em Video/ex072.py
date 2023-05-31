#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
#Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

num_extenso = ("Zero", "Um", "Dois", "Três", "Quatro",
               "Cinco", "Seis", "Sete", "Oito", "Nove",
               "Dez", "Onze", "Doze", "Treze", "Catorze",
               "Quinze", "Dezesseis", "Dezesete", "Dezoito", "Dezenove", "Vinte")

while True:
    num = int(input("Digite um número para vê-lo por extenso: "))
    if 0 <= num <= 20:
        print(num_extenso[num])
    resp = " "
    while resp not in "SN":
        resp = str(input("Deseja continuar? [S/N]: ")).strip().upper()[0]
    if resp == "N":
        break
