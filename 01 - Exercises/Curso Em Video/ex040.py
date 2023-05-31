# Ler duas notas e calcular média, < 5 reprovado, entre 5 e 6,9 recuperação, > 7 aprovado
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
med = (n1 + n2)/2
print("Sua média é {} e você foi".format(med))
if med < 5:
    print("Reprovado")
elif 5 <= med < 7:
    print("Recuperação")
elif med >= 7:
    print("Aprovado")