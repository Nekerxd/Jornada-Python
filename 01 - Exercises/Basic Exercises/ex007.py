# Write a Python program to accept a filename from the user and print the extension of that.

arquivo = input("Digite o nome do arquivo: ")

extensao = arquivo.split(".")

print(f"A extensão do arquivo é {extensao[-1]}")