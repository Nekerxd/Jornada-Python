# # Repetição de código que pode ser evitada

# nome = "Adriano"
# idade = 50
# emprego = "Desenvolvedor Frontend"

# print(f"Olá meu nome é {nome}, tenho {idade} anos e trabalho como {emprego}")

# nome = "Joana"
# idade = 36
# emprego = "Desenvolvedora Backend"

# print(f"Olá meu nome é {nome}, tenho {idade} anos e trabalho como {emprego}")

# nome = "Carlos"
# idade = 22
# emprego = "Estagiário de Desenvolvimento"

# print(f"Olá meu nome é {nome}, tenho {idade} anos e trabalho como {emprego}")

# # Função

# def diz_ola(nome, idade, emprego):
#     print(f"Olá meu nome é {nome}, tenho {idade} anos e trabalho como {emprego}")


# diz_ola("Adriano", 50, "Desenvolvedor Frontend")
# diz_ola("Joana", 36, "Desenvolvedora Backend")
# diz_ola("Carlos", 22, "Estagiário de Desenvolvimento")

# # Função simples de soma

# def soma(num1, num2):
#     return num1 + num2


# resultado = soma(10, 20)

# print(resultado)

# Função com retornos múltiplos

def media_mediana(notas):
    media = sum(notas) / len(notas)
    notas_ordenas = sorted(notas)
    
    if (len(notas) % 2 == 0):
        # Par
        centro_menor = int(len(notas) / 2 - 1)
        centro_maior = int(len(notas) / 2)
        ponto_central_menor = notas[centro_menor]
        ponto_central_maior = notas[centro_maior]
        
        mediana = (ponto_central_maior + ponto_central_menor) / 2
        pass
    else:
        # Ímpar
        indice_mediana = int(len(notas) / 2)
        mediana = notas_ordenas[indice_mediana]

    return media, mediana

resultado_media, resultado_mediana = media_mediana([5, 6, 4, 7])
print(resultado_media)
print(resultado_mediana)

