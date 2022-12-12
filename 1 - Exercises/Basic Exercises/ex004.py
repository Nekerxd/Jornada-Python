# Write a Python program which accepts the radius of a circle from the user and compute the area

import math

raio = float(input("Digite o raio do círculo: "))

area = math.pi * (raio ** 2)

print(f"A área do círculo é aproximadamente {area}")