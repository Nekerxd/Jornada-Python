"""
Comma-separated values

1) Ler arquivo de entrada CSV
2) Processamento (Retirada do campo ID e junção do campo Nome e Sobrenome)
3) Gravação do arquivo de CSV de saída

"""
resultados = []

with open("./13 - Manipulação de arquivos/dados/cadastro.csv", "r") as arquivo_entrada:
    linhas = arquivo_entrada.readlines()[1:]
    
    for linha in linhas:
        dados = linha.split(",")
        email = dados[3].replace("\n", "")
        resultados.append(f"{dados[1]} {dados[2]},{email}\n")

with open("./13 - Manipulação de arquivos/dados/cadastro_saida.csv", "w") as arquivo_saida:
    for resultado in resultados:
        arquivo_saida.write(resultado)