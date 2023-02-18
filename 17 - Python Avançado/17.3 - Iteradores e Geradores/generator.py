def numeros_pares(maximo):
    atual = 0
    
    while atual < maximo:
        yield atual
        
        atual += 2
    

print(list(numeros_pares(150)))