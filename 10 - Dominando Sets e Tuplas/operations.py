homens = {'João', 'Joaquim', 'Alberto', 'Antônio', 'Leonardo', 'Victor', 'Kléber', 'Marcelo', 'Alfredo'}
alta_renda = {'Ana', 'Joaquim', 'Joana', 'Antônio', 'Kléber', 'Marcelo', 'Alfredo', 'Carla', 'Adriana'}

print(f"Conjunto de Homens: {homens}")
print(f"Conjunto de Alta Redna: {alta_renda}\n {'-' * 150}\n")


# Interseção: Itens que estão em ambos os conjuntos
homens_alta_renda = homens.intersection(alta_renda)

print(f"Usuários Homens com Alta Renda: {homens_alta_renda}")


# União: Itens de ambos os conjuntos
homens_e_alta_renda = homens.union(alta_renda)

print(f"Homens e Usuários com Alta Renda: {homens_e_alta_renda}")

# Diferença: Itens que estão apenas em um dos conjuntos
homens_nao_alta_renda = homens.difference(alta_renda)
alta_renda_nao_homens = alta_renda.difference(homens)

print(f"Usuários Homens não Alta Renda: {homens_nao_alta_renda}")
print(f"Usuários Alta Renda não Homens: {alta_renda_nao_homens}")

# Diferença Simétrica: Itens que estão em um conjunto ou em outro mas não em ambos (retira a interseção)
# é possivel utilizar _update para alterar o set origem
# homens.symmetric_difference_update(alta_renda)

homens_nao_alta_renda_e_mulheres = homens.symmetric_difference(alta_renda)

print(f"Usuários Homens não Alta Renda e Usuárias Mulheres Alta Renda: {homens_nao_alta_renda_e_mulheres}")

# Métodos de Conjuntos

# Não possuem interseção entre eles
print(f"Os conjuntos de Homens e Alta Renda são disjuntos? {homens.isdisjoint(alta_renda)}")

# Um conjunto é englobado por outro
print(f"O conjunto de Homens é um subconjunto de Alta Renda? {homens.issubset(alta_renda)}")

# Um conjunto engloba outro
print(f"O conjunto de Homens é um superconjunto Alta Renda? {homens.issuperset(alta_renda)}")


# Operadores

# Interseção:
print(homens & alta_renda)

# União:
print(homens | alta_renda)

# Diferença:
print(homens - alta_renda)

# Diferença Simétrica:
print(homens ^ alta_renda)