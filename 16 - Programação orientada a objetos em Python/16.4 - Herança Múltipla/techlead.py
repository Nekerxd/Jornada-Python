from random import choice


class Desenvolvedor:
    def __init__(self, linguagens_programacao=None):
        self.linguagens_programacao = linguagens_programacao
        print(f"Novo desenvolvedor com expertise nas Linguagens: \n\t{self.linguagens_programacao}")
    
    
    def desenvolver_codigo(self):
        print(f"Shhhhhh! Dev codando em {choice(self.linguagens_programacao)}!")
    
    
    
class Gerente:
    def __init__(self, softskills=None):
        self.softskills = softskills
        print(f"Novo Gerente com habilidade nas SoftSkills: \n\t{self.softskills}")
    
    
    def gerenciar_equipe(self):
        print(f"Gerente está utilizando {choice(self.softskills)} para gerenciar sua equipe!")
    
    

class TechLead(Desenvolvedor, Gerente):
    def __init__(self, linguagens_programacao=None, softskills=None):
        Desenvolvedor.__init__(self, linguagens_programacao)
        Gerente.__init__(self, softskills)
    
    

tech_lead = TechLead(["C", "C++", "C#"], ["Liderança", "Comunicação Ativa", "Feedbacks Positivos"])
tech_lead.desenvolver_codigo()
tech_lead.gerenciar_equipe()