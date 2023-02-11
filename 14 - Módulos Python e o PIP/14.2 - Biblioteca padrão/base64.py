from email.mime import base
from operator import imod


import base64

with open("./14 - Módulos Python e o PIP/14.2 - Biblioteca padrão/logo.png", "rb") as file:
    arquivo_b64 = base64.b64encode(file.read())
    
    print(arquivo_b64)
