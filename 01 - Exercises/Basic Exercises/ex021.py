# Write a Python program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user.

def impar_par():
    num = int(input("Insira um número inteiro: "))
    
    if num % 2 == 0:
        return print("O número escolhido é par!")
    return print("O número escolhido é ímpar!")


impar_par()