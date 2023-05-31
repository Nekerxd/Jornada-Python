# Ler um número qualquer inteiro e escolher qual a base de conversão
from tkinter import N


num = int(input("Escolha um número para conversão: "))
base = int(input("Escolhe a base de conversão:\n[1] Octal\n[2] Hexadecimal\n[3] Binário\n"))
if base == 1:
    print(oct(num) [2:])
elif base == 2:
    print(hex(num) [2:])
elif base == 3:
    print(bin(num) [2:])
else:
    print("Opção inválida")