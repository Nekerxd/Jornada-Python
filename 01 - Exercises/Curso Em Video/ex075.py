#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#Quantas vezes apareceu o valor 9, em que posição foi digitado o primeiro valor 3, quais foram os números pares.

num = (int(input("Digite um número: ")), int(input("Digite outro número: ")),
     int(input("Digite mais um número: ")), int(input("Digite o último número: ")))

if num.count(9) == 0:
    print(f"O número 9 não apareceu nenhuma vez.")
else:
    print(f"O número 9 apareceu {num.count(9)} vezes.")
if 3 in num:
    print(f"O número 3 aparece pela primeira vez na {num.index(3)+1}ª posição.")
else:
    print(f"O número 3 não apareceu nenhuma vez.")
print("Os números pares foram:", end=" ")

for c in num:
    if c % 2 == 0:
        print(f"{c} ", end="")
