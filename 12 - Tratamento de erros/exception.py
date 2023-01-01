from multiprocessing.sharedctypes import Value
from traceback import print_tb


cadastro_csv = [
    "João,28,Analista de Sistemas",
    "Maria,31,Desenvolvedora Frontend",
    "Jonas,37,Gerente de Projetos",
    "Alberto,47"
]

def processa_dados(cadastros):
    for cadastro in cadastros:
        dados = cadastro.split(",")
        
        if len(dados) != 3:
            raise ValueError("Formato incorreto dos dados!")
        
        nome = dados[0]
        
        try:
            idade = int(dados[1])
        except ValueError:
            raise ValueError("Erro no formato do dado \"Idade\"")
        cargo = dados[2]

        print(f"{nome} tem {idade} anos e atua no cargo de {cargo}.")

try:
    processa_dados(cadastro_csv)
    
except ValueError as exececao:
    print(f"O programa encontrou um erro. Erro: {exececao}")