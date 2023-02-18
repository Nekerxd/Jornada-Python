class NumerosPares:
    def __init__(self, maximo):
        self.maximo = maximo
        self.atual = 0
    
    def __iter__(self):
        return self
    
    
    def __next__(self):
        if self.atual > self.maximo:
            raise StopIteration
        
        retorno = self.atual
        self.atual += 2
        
        return retorno


iterador_numeros_pares = NumerosPares(150)

for numero in iterador_numeros_pares:
    print(numero, end=" ")