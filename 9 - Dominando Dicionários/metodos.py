familia = {
    "pai" : "José da Silva",
    "mae" : "Ana Almeida",
    "filho" : "Cléber da Silva Almeida",
    "filha" : "Joana da Silva Almeida"
}

print(f"Família: {familia}")

# COPY
# Copia um dicionário

copia = familia.copy()
print(f"Cópia do dicionário família: {copia}")

# ITEMS
# Retorna os pares chave:valor em formato de lista

itens = familia.items()
print(f"Itens: {itens}")

for item in itens:
    print(f"\t Chave = {item[0]} e valor = {item[1]}")

# KEYS
# Retorna todas as chaves em formato de lista

chaves = familia.keys()
print(f"Chaves: {chaves}")

for chave in chaves:
    print(f"\tChave: {chave}")

# VALUES
# Retorna todos os valores em formato de lista

valores = familia.values()
print(f"Valores: {valores}")

for valor in valores:
    print(f"\tValor: {valor}")

# SETDEFAULT
# Insere a chave com o valor passado SE a chave não estiver presente no dicionário
# Retorna o valor da chave SE a chave já estiver presente no dicionário

familia.setdefault("sobrinho","Carlos Silva")

print(familia)

mae = familia.setdefault("mae", "Roberta Miranda")

print(familia)
print(mae)

# FROMKEYS
# Cria um dicionário a partir de uma lista de chaves e um valor

chaves = ["mae", "pai", "filho", "filha"]
valor = 0

jogo = dict.fromkeys(chaves, valor)

print(f"Jogo: {jogo}")