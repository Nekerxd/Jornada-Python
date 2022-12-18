def aplica_baskhara(a: float, b: float, c: float) -> float:
    delta = b ** 2 - 4 * a * c
    x_1 = (-b + (delta ** 1/2)) / (2 * a)
    x_2 = (-b - (delta ** 1/2)) / (2 * a)


    return x_1, x_2


print(aplica_baskhara(5.0, 15.0, -25.0))

def aplica_desconto(produtos: dict, desconto: float) -> dict[str: str]:
    resultado = {}
    
    for nome_produto, valor_produto in produtos.items():
        resultado[nome_produto] = f"{valor_produto * (1 - desconto):.2f}"
        
    
    return resultado


valores_produtos = {
    'microondas': 497.99,
    'computador': 3499.97,
    'forno': 399.97,
}

print(aplica_desconto(valores_produtos, 0.15))

x: list = "1, 2, 3".split(",")