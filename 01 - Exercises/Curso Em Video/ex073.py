#Primeiros 20 do Brasileirão em numa tupla. Mostrar os 5 primeiros, Os 4 últimos, os times em ordem alfabética, a posição da Bragantino.

brasileiro = ("Palmeiras", "Atlético-MG", "Corinthians", "Coritiba", "São Paulo", "Athletico-PR", "Botafogo", "Flamengo", "Santos", "América-MG", 
              "Fluminense", "Avaí", "Bragantino", "Internacional", "Goiás", "Cuiabá", "Juventude", "Ceará", "Atlético-GO", "Fortaleza")

print("-="*15)
print(f"Os 5 primeiros times são: {brasileiro[:5]}")
print("-="*15)
print(f"Os quatro últimos times são: {brasileiro[-4:]}")
print("-="*15)
print(f"Os times em ordem alfábetica: {sorted(brasileiro)}")
print("-="*15)
print(f"Bragantino está na {brasileiro.index('Bragantino')+1}º posição")
print("-="*15)