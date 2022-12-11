idade = 25
texto = "Parabéns Luiz pelos seus " + str(idade) + " anos de idade"

print(texto)

pontuacao_str = "31"
pontuacao_int = int(pontuacao_str)

print(pontuacao_int)
print(f"Tipo: {type(pontuacao_int)}")


pontuacao_str = "5.5"
pontuacao_float = float(pontuacao_str)

print(pontuacao_float)
print(f"Tipo: {type(pontuacao_float)}")

# print(int("5.5")) não é possível

print(float("1"))