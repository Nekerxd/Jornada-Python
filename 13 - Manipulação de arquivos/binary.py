arquivo_png = open("./13 - Manipulação de arquivos/dados/profile.png", "rb")

retorno_png = arquivo_png.read()

arquivo_saida = open("./13 - Manipulação de arquivos/dados/profile_saida.png", "wb")

arquivo_saida.write(retorno_png)

print(retorno_png)

arquivo_saida.close()
arquivo_png.close()