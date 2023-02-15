from random import randint
from time import sleep


VALOR_PEDAGIO_CARRO = 3.5
VALOR_PEDAGIO_MOTO = 2.75
VALOR_KM_RODADO_CARRO = 1.5
VALOR_KM_RODADO_MOTO = 1.0

class Automovel:
    def __init__(self, montadora, modelo, alugado):
        self.montadora = montadora
        self.modelo = modelo
        self.alugado = alugado
        self.valor_fatura = 0
        self.nome_cliente = ""
        print(f"Automóvel {self.montadora} {self.modelo} adquirido pela locadora!")
    
    
    def alugar(self, nome_cliente):
        self.alugado = True
        self.nome_cliente = nome_cliente
        print(f"O Automóvel {self.montadora} {self.modelo} foi alugado por {self.nome_cliente}!")
    
    
    def devovler_automovel(self):
        self.alugado = False
        print(f"O Automóvel {self.montadora} {self.modelo} foi devolvido por {self.nome_cliente}!")
        self.nome_cliente = ""
    
    
    def gerar_valor_fatura(self, numero_pedagios, km_rodados):
        raise NotImplementedError



class Carro(Automovel):
    def __init__(self, montadora, modelo, alugado):
        super(Carro, self).__init__(montadora, modelo, alugado)
        print("O automóvel adquirido foi um Carro!")
        
    
    def gerar_valor_fatura(self, numero_pedagios, km_rodados):
        self.valor_fatura = numero_pedagios * VALOR_PEDAGIO_CARRO + km_rodados * VALOR_KM_RODADO_CARRO
        print(f"Fatura do Carro {self.montadora} {self.modelo} gerada com sucesso no valor de R${self.valor_fatura:.2f}")

class Moto(Automovel):
    def __init__(self, montadora, modelo, alugado):
        super(Moto, self).__init__(montadora, modelo, alugado)
        print("O automóvel adquirido foi um Moto!")
        
    def gerar_valor_fatura(self, numero_pedagios, km_rodados):
        self.valor_fatura = numero_pedagios * VALOR_PEDAGIO_MOTO + km_rodados * VALOR_KM_RODADO_MOTO
        print(f"Fatura da Moto {self.montadora} {self.modelo} gerada com sucesso no valor de R${self.valor_fatura:.2f}")


# Polimorfismo
def mostrar_fatura(automovel):
    print(f'O valor da Fatura do Automóvel {automovel.montadora} {automovel.modelo} alugado por {automovel.nome_cliente} ficou no valor de R$ {automovel.valor_fatura:.2f}')
    


# ---------------------------------------------------------------------------------------------------------------------

fiesta = Carro("Ford", "Fiesta", False)
fiesta.alugar("João")

# Simulação do tempo de aluguel do Automóvel
sleep(randint(2, 5))

# fiesta.devovler_automovel()

fiesta.gerar_valor_fatura(numero_pedagios=2, km_rodados=369)

mostrar_fatura(fiesta)

honda_cb = Moto("Honda", "CB600", False)
honda_cb.alugar("Ana")

# Simulação do tempo de aluguel do Automóvel
sleep(randint(2, 5))

honda_cb.gerar_valor_fatura(numero_pedagios=3, km_rodados=500)
mostrar_fatura(honda_cb)