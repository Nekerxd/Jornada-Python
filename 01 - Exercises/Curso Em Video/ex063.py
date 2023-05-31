#Sequência Fibonacci F(n + 2) = F(n + 1) + F(n)

termos = int(input("Digite quantos termos deseja da Sequência Fibonacci: "))
n1 = 0
n2 = 1
cont = 3

print("{} ➝  {}".format(n1, n2), end="")
while cont <= termos:
    n3 = n1 + n2
    print(" ➝  {}".format(n3), end="")
    n1 = n2
    n2 = n3
    cont += 1
print(" ➝  FIM")
