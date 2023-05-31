#Faça um programa que leia um número qualquer e mostre o seu fatorial.
numinit = int(input("Digite um número para saber seu fatorial: "))
num = numinit
res = 1
print("{}! = ".format(num), end="")
while num > 0:
    print("{}".format(num), end="")
    print(" x " if num > 1 else " = ", end="")
    res *= num
    num -= 1
print("{}".format(res))
