def div_dois_num(dividendo, divisor):
    return dividendo/divisor

try:
    # Código a ser testado
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))

    result = div_dois_num(n1, n2)

except TypeError as ErroTipagem:
    print(f"Um erro ocorreu: {ErroTipagem}")
    
except (ZeroDivisionError, TypeError):
    print("Divisão por 0 ou erro de Tipagem!")
    
except:
    # Execute esse código caso um erro ocorra
    print("Um erro ocorreu!!")
    
else:
    # Execute esse código caso nenhum erro ocorra
    print(result)
    
finally:
    # Sempre execute esse código
    print("Finalizando programa. Muito obrigado!")
