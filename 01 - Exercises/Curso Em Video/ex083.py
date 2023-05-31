#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
#Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

parenteses = list()
expressao = (str(input("Digite a expressão: ")))
for i in expressao:
    if i == "(":
        parenteses.append("(")
    elif i == ")":
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append(")")
            break
if len(parenteses) == 0:
    print("A expressão está errada.")
else:
    print("A expressão está correta!")