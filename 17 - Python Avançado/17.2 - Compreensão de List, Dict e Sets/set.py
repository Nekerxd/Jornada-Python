class Pessoa:
    def __init__(self, nome, idade, cidade, genero):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
        self.genero = genero
    
    
    def __repr__(self):
        return f"Pessoa: {self.nome}"
    
pessoas = [
    Pessoa("João", 20,"Belém", "M"),
    Pessoa("Catarina", 31,"Brasília", "F"),
    Pessoa("Ana", 38,"Brasília", "F"),
    Pessoa("Joana", 28,"Natal", "F"),
    Pessoa("Henrique", 35,"Palmas", "M"),
    Pessoa("Alberto", 15, "Goiânia", "M")
]

cidades = {pessoa.cidade for pessoa in pessoas}
pessoas_iniciadas_com_j = {pessoa for pessoa in pessoas if pessoa.nome[0].upper() == 'J'}
pessoas_maiores_30 = {pessoa for pessoa in pessoas if pessoa.idade > 30}
pessoas_sexo_masculino = {pessoa for pessoa in pessoas if pessoa.genero.upper() == "M"}

print(f'Cidades: {cidades}')
print(f'Nomes iniciados com J: {pessoas_iniciadas_com_j}')
print(f'Pessoas maiores que 30: {pessoas_maiores_30}')
print(f'Pessoas do sexo Masculino: {pessoas_sexo_masculino}')