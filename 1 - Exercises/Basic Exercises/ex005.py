# Write a Python program which accepts the user's first and last name and print them backwards with a space between them.

nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")

nome_completo = nome.strip().capitalize() + " " + sobrenome.strip().capitalize()
x = ''

for i in range(0, len(nome_completo)+1, 1):
    x += nome_completo[-i]
print(x)
