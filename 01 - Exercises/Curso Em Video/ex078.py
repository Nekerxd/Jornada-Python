#Leia 5 valores númericos e guarde-os em uma lista. No final mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

valores = list()
maior = menor = 0

for i in range(0,5):
    valores.append(int(input(f"Digite um valor para a posição {i}: ")))
    if i == 0:
        maior = menor = valores[i]
    else:
        if valores[i] > maior:
            maior = valores[i]
        if valores[i] < menor:
            menor = valores[i]
print("=-"*30)
print(f"Você digitou os valores {valores}")
print(f"O maior valor digitado foi {maior} nas posições: ", end="")
for c, v in enumerate(valores):
    if v == maior:
        print(f"{c},", end= " ")
print(f"\nO menor valor digitado foi {menor} nas posições: ", end="")
for c, v in enumerate(valores):
    if v == menor:
        print(f"{c},", end= " ")
