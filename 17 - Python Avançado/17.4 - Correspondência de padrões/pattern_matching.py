# ------------------------------------------------------------
# Padrões Literais
# ------------------------------------------------------------

sexo = "M"

match sexo:
    case "F":
        print("Sexo Feminino.")
    case "M":
        print("Sexo Masculino.")

idade = 15

match idade:
    case x if x > 18:
        print("Maior de idade.")
    case x if x < 18:
        print("Menor de idade.")

# ------------------------------------------------------------
# Padrões Coringa
# ------------------------------------------------------------

sexo = "X"

match sexo:
    case "M":
        print("Sexo Masculino.")
    case "F":
        print("Sexo Feminino.")
    case _:
        print("Sexo inválido, tente novamente!")

# ------------------------------------------------------------
# Padrões de Sequências
# ------------------------------------------------------------

# notas = []
# notas = [5]
# notas = [5, 8]
# notas = [5, 8, 6]
notas = [0, 8, 6]

match notas:
    case []:
        print("Aluno não realizou nenhuma das provas")
    case [p1]:
        print(f"Aluno faltou duas provas. Sua média final foi {p1/3:.2f}")
    case [p1, p2]:
        print(f"Aluno faltou uma prova. Sua média final foi {(p1 + p2)/3:.2f}")
    case [0, *resto]:
        print(f"Aluno zerou a primeira prova. Suas outras notas foram: {resto}")
    case [p1, p2, p3]:
        print(f"Média final foi {(p1 + p2 + p3)/3:.2f}")
    
# ------------------------------------------------------------
# Padrões de Mapas
# ------------------------------------------------------------

produtos = [
    {"nome": "Teclado Gamer", "valor": 797.99, "categoria": "computador"},
    {"nome": "Gabinete Corsair", "valor": 499.99, "categoria": "computador"},
    {"nome": "Geladeira Brastemp", "valor": 3797.99, "categoria": "eletrodomestico"}
]

for produto in produtos:
    match produto:
        case {"nome": nome, "valor": valor, "categoria": "computador"}:
            print(f"O Produto {nome} está com um MEGA DESCONTO de 20%: DE R$ {valor} POR R$ {valor*0.8:.2f}")
            
        case {"nome": nome, "valor": valor, "categoria": "eletrodomestico"}:
            print(f"O Produto {nome} está com um MEGA DESCONTO de 35%: DE R$ {valor} POR R$ {valor *0.65:.2f}")
            
# ------------------------------------------------------------
# Padrões de Classes
# ------------------------------------------------------------

class Carro:
    def __init__(self, montadora, modelo):
        self.montadora = montadora
        self.modelo = modelo
        
    
carro = Carro("Tesla", "Model S")

match carro:
    case Carro(montadora="Ford", modelo="Fiesta"):
        print("Ford Fiesta")
    case Carro(montadora="Fiat", modelo="Pulse"):
        print("Fiat Pulse")
    case Carro(montadora="Tesla", modelo="Model S"):
        print("Tesla Model S")
        
# ------------------------------------------------------------
# Padrões de Captura
# ------------------------------------------------------------

notas = [5, 8, 6]

match notas:
    case []:
        print("Aluno não realizou nenhuma das provas")
    case [p1]:
        print(f"Aluno faltou duas provas. Sua média final foi {p1/3:.2f}")
    case [p1, p2]:
        print(f"Aluno faltou uma prova. Sua média final foi {(p1 + p2)/3:.2f}")
    case [0, *resto]:
        print(f"Aluno zerou a primeira prova. Suas outras notas foram: {resto}")
    case [p1, p2, p3]:
        print(f"Média final foi {(p1 + p2 + p3)/3:.2f}")

# ------------------------------------------------------------
# Padrões OR
# ------------------------------------------------------------

notas = [0.0, 8, 6]

match notas:
    case []:
        print("Aluno não realizou nenhuma das provas")
    case [0 | 0.0, *resto]:
        print(f"Aluno zerou a primeira prova. Suas outras notas foram: {resto}")

        
# ------------------------------------------------------------
# Padrões AS
# ------------------------------------------------------------

notas = [0.0, 8, 6]

match notas:
    case []:
        print("Aluno não realizou nenhuma das provas")
    case [0 | 0.0, *resto] as lista:
        print(f"Primeira nota: {lista[0]}")
        print(f"Aluno zerou a primeira prova. Suas outras notas foram: {resto}")