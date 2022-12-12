from itertools import count
from pickle import TRUE


sacola = ["Arroz", "Feijão", "Carne", "Farinha"]

print(f"A lista inicial é: {sacola}")

# Método: APPEND(objeto)
# Adiciona um item ao fim da lista

sacola.append("Macarrão")
print(f"Lista após a chamada do método APPEND(): {sacola}")

# Método: EXTEND(estrutura)
# Adiciona todos os itens de outra estrutura ao fim da lista

sacola.extend(["Maionese", "Ketchup"])
print(f"Lista após a chamada do método EXTEND(): {sacola}")

# Método: INSERT(indice, objeto)
# Insere um item na posição desejada da lista

sacola.insert(0, "Milho")
print(f"Lista após a chamada do método INSERT(): {sacola}")

# Método: REMOVE(objeto)
# Remove o primeiro elemento igual ao valor passado

sacola.remove("Macarrão")
print(f"Lista após a chamada do método REMOVE(): {sacola}")

# Método: POP(indice)
# Remove o item na posição desejada da lista e o retorna
# Caso o índice não seja especificado, retorna o último elemento

elemento = sacola.pop()
print(f"Lista após a chamada do método POP(): {sacola}")
print(elemento)

# Método: CLEAR()
# Remove todos os elementos da lista

# sacola.clear()
# print(f"Lista após a chamada do método CLEAR(): {sacola}")

# Método: INDEX(valor[, comeco, fim])
# Retorna o índice do primeiro elemento do valor especificado
# Podemos ainda passar outros parâmetros que dizem onde pesquisar na lista (começo e fim)

print(sacola.index("Milho", 0, 3))
print(f"Lista após a chamada do método INDEX(): {sacola}")

# Método: COUNT(valor)
# Conta o número de ocorrências do valor especificado na lista

print(sacola.count("Arroz"))
print(f"Lista após a chamada do método COUNT(): {sacola}")

# Método: SORT([chave, reverso])
# Ordena os itens da lista. Parâmetros adicionais podem ser utilizados para customizar a ordenação.

sacola.sort()
print(f"Lista após a chamada do método SORT(): {sacola}")
sacola.sort(reverse=True)
print(f"Lista após a chamada do método SORT(): {sacola}")

# Método: REVERSE()
# Reverte os elementos da lista

sacola.reverse()
print(f"Lista após a chamada do método REVERSE(): {sacola}")

# Método: COPY()
# Retorna uma lista com a cópia dos elementos da lista de origem

copia = sacola.copy()
print(copia)
print(f"Lista após a chamada do método COPY(): {sacola}")



