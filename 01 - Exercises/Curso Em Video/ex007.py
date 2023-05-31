#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
print("A média do aluno é igual a {:.1f}".format(media))