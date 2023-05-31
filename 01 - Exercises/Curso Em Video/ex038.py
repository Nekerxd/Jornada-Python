#Ler 2 num inteiro, comparar e mostrar se é maior, menor ou igual
a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))

if a > b:
    print("A é o maior valor!")
elif b > a:
    print("B é o maior valor!")
else:
    print("Não existe valor maior, os dois são iguais!")
