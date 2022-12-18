# def funcao_com_args(arg1, arg2, *args):
#     print(f"Arg1 : {arg1}")
#     print(f"Arg2 : {arg2}")
#     print(f"*Args : {args}")


# funcao_com_args(1, 2, 3, 4, 5, 6, 7)


def soma(maximo, *numeros):
    resultado = 0
    numeros_somados = []
    
    for numero in numeros:
        if (resultado + numero) > maximo:
            break
        
        resultado += numero
        numeros_somados.append(numero)
    
    return resultado, numeros_somados


resultado_soma, numeros_somados = soma(100, 7, 6, 25, 30, 8, 9, 14, 17, 13)
print(resultado_soma)
print(numeros_somados)