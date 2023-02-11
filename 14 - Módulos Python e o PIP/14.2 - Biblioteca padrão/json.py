import json

cadastros = [
    {
        "Nome" : "João",
        "Idade" : 31,
        "Profissões" : ["Estagiário", "Dev Python", "Engenheiro de Software"]
    }, {
        "Nome" : "Clara",
        "Idade" : 35,
        "Profissões" : ["Estagiária de Design", "Desenvolvedora Frontend"]
    }
]

print(json.dumps(cadastros, ensure_ascii=False, indent=True))