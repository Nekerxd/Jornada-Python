texto = "Jornada Python - Manipulação de Arquivos"
texto2 = "\nVenha DOMINAR Python!"

# arquivo = open("./13 - Manipulação de arquivos/dados/dados.txt", "w")
# arquivo = open("./13 - Manipulação de arquivos/dados/dados.txt", "r")
arquivo = open("./13 - Manipulação de arquivos/dados/dados.txt", "a+")

arquivo.write(texto2)

print(arquivo.read())

arquivo.close()