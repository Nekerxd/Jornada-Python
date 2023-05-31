#Ler o primeiro termo e a razão de uma PA, no final mostrar os 10 primeiros termos dessa progressão
a1 = int(input("Qual o primeiro termo da PA? "))
r = int(input("Qual a razão da PA? "))
an = a1+9*r
for c in range(a1,an+1,r):
    print(c, end=' ')