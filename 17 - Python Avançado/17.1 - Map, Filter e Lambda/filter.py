cadastros = [
    "João,18,joao@e'mail.com",
    "    Joa'na,22,joana@gmail.com   ",
    "Kléber,30,Kleber123@hotmai'l.com"
]

resultado = list(map(lambda texto: texto.replace("'", "").strip(), cadastros))

print(f'Map e Lambda: {resultado}')

resultado_filter = list(filter(lambda cadastro: '@gmail' in cadastro, resultado))

print(f'Email filtrado: {resultado_filter}')
