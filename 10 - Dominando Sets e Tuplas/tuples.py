# Criação de Tuplas

# lista = [5, 6, 7]
tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# tupla_2 = tuple(lista)

# print(type(tupla))
print(f"Tupla Inicial: {tupla}")
# print(tupla_2)

# Indexação
print(f"O quinto elemento da Tupla é: {tupla[4]}")

# Indexação Negativa
print(f"O último elemento da Tupla é: {tupla[-1]}")

# Slicing
tupla_slicing = tupla[1::2]
print(tupla_slicing)

# Tuplas não suportam atribuição de valores
# tupla[0] = 1

# Deleção com del
# Tuplas não suportam deleção de itens, apenas a tupla inteira
# del tupla[0]

# Métodos
print(f"A quantidade de elementos iguais à 1 é: {tupla.count(1)}")
print(f"O elemento 7 está na posição: {tupla.index(7)}")

# Iteração
for elemento in tupla:
    print(f"Elementos = {elemento}")
