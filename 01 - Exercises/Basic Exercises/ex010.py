# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn

n = int(input("Digite um número: "))
i = 1
n1 = 0

while (i < 112):
    n1 += n * i
    i = i * 10 + 1
    
print(n1)