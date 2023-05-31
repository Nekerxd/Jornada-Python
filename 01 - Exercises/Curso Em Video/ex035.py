#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
a = int(input("Digite a primera reta: cm "))
b = int(input("Digite a segunda reta: cm "))
c = int(input("Digite a terceira reta: cm "))

if a + b > c and a + c > b and b + c > a:
    print("Com as medidas {}, {} e {} é possível formar um triângulo")
else:
    print("Com as medidas {}, {} e {} não é possível formar um triângulo")