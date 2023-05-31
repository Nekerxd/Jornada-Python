#Refazer o 35, mostrar se é possível equilátero todos iguais, isósceles dois iguais, escaleno todos diferentes
a = int(input("Digite a primera reta: cm "))
b = int(input("Digite a segunda reta: cm "))
c = int(input("Digite a terceira reta: cm "))

if a + b > c and a + c > b and b + c > a:
    if  a == b == c:
        print("Todos iguais")
        print("Com as medidas {}, {} e {} é possível formar um triângulo equilátero".format(a, b, c))
    elif (a == b and a != c) or (a == c and a != b):
        print("Dois iguais")
        print("Com as medidas {}, {} e {} é possível formar um triângulo isósceles".format(a, b, c))
    elif a != b != c !=a:
        print("Todos diferentes")
        print("Com as medidas {}, {} e {} é possível formar um triângulo escaleno".format(a, b, c))
else:
    print("Com as medidas {}, {} e {} não é possível formar um triângulo".format(a, b, c))