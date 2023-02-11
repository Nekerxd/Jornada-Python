import string
import random

pass_size = int(input("Tamanho desejado para a senha: "))
senha = []

for i in range(0, pass_size):
    senha.append(random.choice(string.ascii_letters))
    
print("".join(senha))