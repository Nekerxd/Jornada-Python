

class Empregado:
    numero_empregados = 0
    
    def __init__(self, nome_completo: str, email: str, matricula_funcional: str, salario: int):
        self.nome_completo = nome_completo
        self.email = email
        self.matricula_funcional = matricula_funcional
        self.salario = salario
        
    
    def iniciar_jornada(self):
        print(f'O empregado {self.nome_completo} iniciou sua jornada de trabalho!')
    
    
    def finalizar_jornada(self):
        print(f'Jornada de trabalho finalizada para o empregado {self.nome_completo}.')
       
        
    def receber_aumento(self):
        raise NotImplementedError
    
    
class Desenvolvedor(Empregado):
    porcentagem_aumento = 1.07
    
    def __init__(self, nome_completo: str, email: str, matricula_funcional: str, salario: int, linguagens_programacao: list):
        
        super(Desenvolvedor, self).__init__(nome_completo, email, matricula_funcional, salario)

        Empregado.numero_empregados += 1
    
        self.linguagens_programacao = linguagens_programacao
        self.litros_cafe = 0.0
        self.burnout = False
        
    
    def adicionar_linguagem(self, linguagem: str):
        self.linguagens_programacao.append(linguagem)
        print(f'O desenvolvedor {self.nome_completo} aprendeu a linguagem {linguagem}!')
    
    
    def beber_cafe(self, quantidade: float):
        self.litros_cafe += quantidade
        
        if self.litros_cafe > 2:
            self.burnout = True
            print(f'Após beber mais de 2L de café, o desenvolvedor {self.nome_completo} sofreu um burnout!!')
            self.finalizar_jornada
        else:
            print(f'O desenvolvedor {self.nome_completo} já bebeu {self.litros_cafe}L de café!!')
    
    
    def receber_aumento(self):
        self.salario = self.salario * Desenvolvedor.porcentagem_aumento
        print(f'O Desenvolvedor {self.nome_completo} recebeu um aumento! Parabéns!')


    
class GerenteProjeto(Empregado):
    porcentagem_aumento = 1.1
    
    def __init__(self, nome_completo: str, email: str, matricula_funcional: str, salario: int, time: list, projetos_envolvidos: list):
        
        super(GerenteProjeto, self).__init__(nome_completo, email, matricula_funcional, salario)
        
        Empregado.numero_empregados += 1
    
        self.time = time
        self.projetos_envolvidos = projetos_envolvidos
    
    def adicionar_desenvolvedor(self, desenvolvedor: Desenvolvedor):
        self.time.append(desenvolvedor)
        print(f'O desenvolvedor {desenvolvedor.nome_completo} foi adicionado ao time pelo Gerente {self.nome_completo}')
    
    
    def remover_desenvolvedor(self, desenvolvedor: Desenvolvedor):
        self.time.remove(desenvolvedor)
        print(f'O desenvolvedor {desenvolvedor.nome_completo} foi removido do time pelo Gerente {self.nome_completo}')
    
    
    def participar_projeto(self, projeto):
        self.projetos_envolvidos.append(projeto)
        print(f'O Gerente {self.nome_completo} agora está participando do projeto {projeto}')
    
    
    def sair_projeto(self, projeto):
        self.projetos_envolvidos.remove(projeto)
        print(f'O Gerente {self.nome_completo} não mais participa do projeto {projeto}')
    
    
    def receber_aumento(self):
        self.salario = self.salario * GerenteProjeto.porcentagem_aumento
        print(f'O Gerente {self.nome_completo} recebeu um aumento! Parabéns!')

#  def __init__(self, nome_completo: str, email: str, matricula_funcional: str, salario: int, linguagens_programacao: list, litros_cafe: float, burnout: bool):
joao_dev = Desenvolvedor(
    nome_completo='João Carlos da Silva',
    email='joao.carlos@empresa.br',
    matricula_funcional='F4787962',
    salario=4500,
    linguagens_programacao=['C', 'Python']
)

adam_gerente = GerenteProjeto(
    nome_completo='Gabriel Meirelles',
    email='gabriel_meirelles@gmail.com',
    matricula_funcional='G684G63D',
    salario=7360,
    time=[joao_dev],
    projetos_envolvidos=['Polícia Federal', 'Ministério da Economia']
)

# João e Adam iniciam sua Jornada de Trabalho
joao_dev.iniciar_jornada()
adam_gerente.iniciar_jornada()

# João toma aquele cafézinho pra iniciar mais um dia de trabalho
joao_dev.beber_cafe(0.5)

# Adam começa a participar de mais um projeto...
adam_gerente.participar_projeto('Ministério do Turismo')

# E por isso, recebe um aumento...
adam_gerente.receber_aumento()

# E João também, que desempenhou um ótimo trabalho...
joao_dev.receber_aumento()

# Mas Adam fica sobrecarregado e pede pra sair do projeto da Polícia Federal
adam_gerente.sair_projeto('Polícia Federal')

# João deu um UPDATE SEM WHERE na sexta feira e Adam o removeu do time
adam_gerente.remover_desenvolvedor(joao_dev)

# João ficou pistola e enche a cara de café
joao_dev.beber_cafe(1.6)

# O que resulta em um burnout 🔥🔥🔥
print("\n\n\n\n\n")

print(Empregado.numero_empregados)