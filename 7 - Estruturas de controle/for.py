# For: Sintaxe básica

sequencia = [1, 2, 3]

# for elemento in sequencia:
#     print(f"{elemento}")
    
# Range
# Em C -> for(i = 0; i < 10; i += 2)

# for i in range(0, 10, 2):
#     print(f"{i}")
    
set_ = {1, 2, 3}
tupla = (1, 2, 3)
lista = [1, 2, 3]
dicionario = {"a": 1, "b": 2}

for elemento in set_:
    print(f"[SET] Elemento do set: {elemento}")
for elemento in tupla:
    print(f"[TUPLA] Elemento da tupla: {elemento}")
for elemento in lista:
    print(f"[LISTA] Elemento da lista: {elemento}")
for elemento in dicionario.items():
    print(f"[DICT] Elemento do dicionario: {elemento}")