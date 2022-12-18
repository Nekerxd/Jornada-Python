from unittest import result


def adicao(numeros):
    return int(numeros[0]) + int(numeros[1])


def subtracao(numeros):
    return int(numeros[0]) - int(numeros[1])


def multiplicacao(numeros):
    return int(numeros[0]) * int(numeros[1])


def divisao(numeros):
    return int(numeros[0]) / int(numeros[1])


def potencia(numeros):
    return int(numeros[0]) ** int(numeros[1])


def calculadora(numeros, operacao):
    if operacao == '+':
        resultado_calc = adicao(numeros)
    elif operacao == '-':
        resultado_calc = subtracao(numeros)
    elif operacao == '*':
        resultado_calc = multiplicacao(numeros)
    elif operacao == '/':
        resultado_calc = divisao(numeros)
    elif operacao == '^':
        resultado_calc = potencia(numeros)
        
    print(f"Resultado: {resultado_calc}")

while True:
    numeros_user = input("Digite dois números separados por espaço: ").split(" ")
    if len(numeros_user) == 2:
        break
    print("Quantidade de números inválida!")

while True:
    operacao_user = input("Digite a operação desejada [+] [-] [*] [/] [^]: ").strip()
    if operacao_user in "+-*/^":
        break
    print("A operação escolhida não é válida!")

calculadora(numeros_user, operacao_user)