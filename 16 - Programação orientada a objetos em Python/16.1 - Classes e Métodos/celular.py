import random

# Classe Celular:
#     Atributos:
#         Fabricante: String
#         Modelo: String
#         Tela: Decimal
#         Armazenamento: Inteiro
#         Memória: Inteiro
#         Câmera: Inteiro
#         Bateria: Inteiro
#         Tela Ligada: Booleano
#     Métodos:
#         ligar_tela()
#         salvar_em_disco()
#         carregar_aplicativo()
#         tirar_foto()
#         verificar_carga_bateria()

class Celular:
    def __init__(self, fabricante, modelo, tela, armazenamento, memoria, camera, bateria, tela_ligada):
        self.fabricante = fabricante
        self.modelo = modelo
        self.tela = tela
        self.armazenamento = armazenamento
        self.memoria = memoria
        self.camera = camera
        self.bateria = bateria
        self.tela_ligada = tela_ligada
    
    def ligar_tela(self):
        self.tela_ligada = True

    
    def verificar_carga_bateria(self):
        self.carga = random.randint(0,100)
        print(f"O celular está com de {self.carga} Bateria e {(self.carga/100)*self.bateria}mA restantes")
        


celular_android = Celular("Samsung", "S10", 6.25, 128, 4, 21, 3400, False)
celular_iphone = Celular(fabricante="Apple", modelo="Iphone 13 PRO", tela=5.75, armazenamento=128, memoria=3, camera=16, bateria=2650, tela_ligada=False)

celular_iphone.ligar_tela()

celular_android.verificar_carga_bateria()

pass
