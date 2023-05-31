#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
variavel = input("Digite algo: ")

print("Só tem espaços? ", variavel.isspace())
print("É um número? ", variavel.isnumeric())
print("É alfabético? ", variavel.isalpha())
print("É alfanumérico? ", variavel.isalnum())
print("Está em maiúsculas? ", variavel.isupper())
print("Está em minúsculas? ", variavel.islower())
print("Está capitalizada? ", variavel.istitle())