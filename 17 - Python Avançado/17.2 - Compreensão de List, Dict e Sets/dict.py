clientes = {
    'Maria': '041.587.56-85',
    'Carlos': '136.857.963-88',
    'Joana': '140.857.965-16',
    'Marcos': '745.878.969-12'
}

# resultado = {}

# for chave, valor in clientes.items():
#     resultado[chave] = valor.replace('.', '').replace('-', '')
    
# print(resultado)

resultado = {chave.upper():valor.replace('.', '').replace('-', '') for chave, valor in clientes.items()}

print(resultado)

# Salários maiores que 5000

cadastro = {
    'Maria': 4500,
    'Carlos': 7800,
    'Joana': 3750,
    'Marcos': 15000
}

salario_maior_5000 = {chave:valor for chave, valor in cadastro.items() if valor > 5000}