cadastro = {
    "id": 1,
    "nome": "Oswaldo Cruz",
    "filhos": ["Cleiton", "Maria"],
    "compras": [
        {
            "id": 2457,
            "produto": "Notebook Acer",
            "preço": 2597.90,
        }
    ]
}

print(cadastro["compras"][0]["id"])

print(f"O usuário {cadastro['nome']} realizou a seguinte compra: {cadastro['compras'][0]['produto']}")

print(cadastro.get("altura", "None"))