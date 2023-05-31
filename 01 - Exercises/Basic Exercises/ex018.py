# Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.

def calcular(n1, n2, n3):
    
    soma = n1 + n2 + n3
    
    if n1 == n2 == n3:
        soma *= 3
        
    return soma


print(calcular(7, 9, 3))
print(calcular(7, 7, 3))
print(calcular(7, 7, 7))
