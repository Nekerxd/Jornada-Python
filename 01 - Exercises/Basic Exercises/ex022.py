# Write a Python program to count the number 4 in a given list.

def conta_quatro(numeros):
    count = 0
    for numero in numeros:
        if numero == 4:
            count+=1
    
    return count

print(conta_quatro([8,6,9,4,1,3,4,4]))