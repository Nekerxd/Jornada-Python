def trata_texto(texto):
    return texto.replace("'", "").strip()



cadastros = [
    "João,18,joao@e'mail.com",
    "    Joa'na,22,joana@gmail.com   ",
    "Kléber,30,Kleber123@hotmai'l.com"
]

resultado = []


for elemento in cadastros:
    resultado.append(trata_texto(elemento))


print(f'For: {resultado}')

resultado = list(map(trata_texto, cadastros))

print(f'Map: {resultado}')
