# Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.

def distancia(num):
    if num <= 17:
        return 17 - num
    else:
        return (num - 17)*2
    
num = int(input("Insira um número: "))

        