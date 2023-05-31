#Gerar 5 número aleatórios e colocar em uma tupla. Mostrar listagem de números gerados e mostrar o menor e o maior valor que estão na tupla.
from random import randint


num_ale = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print("Os valores sorteados foram: ", end="")
for n in num_ale:
    print(f"{n} ", end="")
print(f"\nO maior valor sorteado foi {max(num_ale)}")
print(f"O menor valor sorteado foi {min(num_ale)}")