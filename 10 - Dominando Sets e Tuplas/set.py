#Criando Sets

carteira = {'PETR4', 'CASH3', 'MGLU3', 'BBAS3', 'WEGE3'}
print(f"Carteira inicial: {carteira}")

#Adicionando elementos com ADD
carteira.add('PETR4')
print(f"Carteira após add(): {carteira}")

#Atualizando elementos com UPDATE
carteira.update({'PETR4', 'ABEV3', 'RAIZ4'})
print(f"Carteira após update(): {carteira}")

#Removendo elementos com DISCARD (não lança exceção caso elemento não seja encontrado)
carteira.discard('PETR4')
print(f"Carteira após discard(): {carteira}")

#Removendo elementos com REMOVE (lança exceção caso elemento não seja encontrado)
carteira.remove('ABEV3')
print(f"Carteira após remove(): {carteira}")

#Removendo elementos com POP (retira um aleatório)
item = carteira.pop()
print(f"Item removido: {item}")
print(f"Carteira após pop(): {carteira}")

#Limpando elementos com CLEAR
carteira.clear()
print(f"Carteira após clear(): {carteira}")