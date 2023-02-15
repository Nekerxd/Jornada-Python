from random import randint
from time import sleep


VALOR_PEDAGIO_CARRO = 3.5
VALOR_PEDAGIO_MOTO = 2.75

VALOR_KM_RODADO_CARRO = 1.5
VALOR_KM_RODADO_MOTO = 1.0

class Automovel:
    numero_total_locacoes = 0
    
    def __init__(self, montadora, modelo, alugado):
        self.montadora = montadora
        self.modelo = modelo
        self.alugado = alugado
        self.valor_fatura = 0
        self.nome_cliente = ""
        print(f"Automóvel {self.montadora} {self.modelo} adquirido pela locadora!")
    
    
    def alugar(self, nome_cliente):
        Automovel.numero_total_locacoes += 1
        self.alugado = True
        self.nome_cliente = nome_cliente
        print(f"O Automóvel {self.montadora} {self.modelo} foi alugado por {self.nome_cliente}!")
    
    
    def devovler_automovel(self):
        self.alugado = False
        print(f"O Automóvel {self.montadora} {self.modelo} foi devolvido por {self.nome_cliente}!")
        self.nome_cliente = ""
    
    
    def gerar_valor_fatura(self, numero_pedagios, km_rodados):
        raise NotImplementedError

    
    @classmethod
    def mostrar_numero_total_locacoes(cls):
        print(f"O número total de Locações de Automóveis é de {cls.numero_total_locacoes} locações")


# ---------------------------------------------------------------------------------------------------------------------

class Carro(Automovel):
    numero_total_locacoes_carro = 0
    valor_total_locacoes = 0.0
    
    def __init__(self, montadora, modelo, alugado):
        super(Carro, self).__init__(montadora, modelo, alugado)
        print("O automóvel adquirido foi um Carro!")
    
    
    def alugar(self, nome_cliente):
        super(Carro, self).alugar(nome_cliente)
        Carro.numero_total_locacoes_carro +=1
    
    def gerar_valor_fatura(self, numero_pedagios, km_rodados):
        self.valor_fatura = numero_pedagios * VALOR_PEDAGIO_CARRO + km_rodados * VALOR_KM_RODADO_CARRO
        print(f"Fatura do Carro {self.montadora} {self.modelo} gerada com sucesso no valor de R${self.valor_fatura:.2f}")
        Carro.valor_total_locacoes += self.valor_fatura
        
    
    @classmethod
    def calcular_media_locacao(cls):
        if cls.numero_total_locacoes_carro != 0:
            media_locacao = cls.valor_total_locacoes / cls.numero_total_locacoes_carro
            print(f"O valor médio de Locação de Carros é de R$ {media_locacao}/locação")
        else:
            print("Número total de Locações de Carros igual a zero.")



# ---------------------------------------------------------------------------------------------------------------------

class Moto(Automovel):
    numero_total_locacoes_moto = 0
    valor_total_locacoes = 0.0
    
    def __init__(self, montadora, modelo, alugado):
        super(Moto, self).__init__(montadora, modelo, alugado)
        print("O automóvel adquirido foi um Moto!")
    
    
    def alugar(self, nome_cliente):
        super(Moto, self).alugar(nome_cliente)
        Moto.numero_total_locacoes_moto +=1
    
        
    def gerar_valor_fatura(self, numero_pedagios, km_rodados):
        self.valor_fatura = numero_pedagios * VALOR_PEDAGIO_MOTO + km_rodados * VALOR_KM_RODADO_MOTO
        print(f"Fatura da Moto {self.montadora} {self.modelo} gerada com sucesso no valor de R${self.valor_fatura:.2f}")
        Moto.valor_total_locacoes += self.valor_fatura
    
    
    @classmethod
    def calcular_media_locacao(cls):
        if cls.numero_total_locacoes_moto != 0:
            media_locacao = cls.valor_total_locacoes / cls.numero_total_locacoes_moto
            print(f"O valor médio de Locação de Motos é de R$ {media_locacao}/locação")
        else:
            print("Número total de Locações de Motos igual a zero.")


# Polimorfismo
def mostrar_fatura(automovel):
    print(f'O valor da Fatura do Automóvel {automovel.montadora} {automovel.modelo} alugado por {automovel.nome_cliente} ficou no valor de R$ {automovel.valor_fatura:.2f}')
    


# ---------------------------------------------------------------------------------------------------------------------

cb_500 = Moto("Honda", "CB500", False)
cb_500.alugar("Ana")
cb_500.devovler_automovel()
cb_500.gerar_valor_fatura(5, 650)
cb_500.alugar("Clara")
cb_500.devovler_automovel()
cb_500.gerar_valor_fatura(4, 1245)
cb_500.calcular_media_locacao()

# ---------------------------------------------------------------------------------------------------------------------
vw_polo = Carro("Volkswagen", "Polo", False)
vw_polo.alugar("João")
vw_polo.devovler_automovel()
vw_polo.gerar_valor_fatura(8, 1300)
vw_polo.alugar("Mario")
vw_polo.devovler_automovel()
vw_polo.gerar_valor_fatura(2, 730)
vw_polo.calcular_media_locacao()
