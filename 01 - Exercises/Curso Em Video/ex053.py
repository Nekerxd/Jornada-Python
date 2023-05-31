# Ler uma frase qualquer e diga se ela é um palíndromo desconsiderando os espaços. Ex: Apos a sopa
frase = str(input("Insira uma frase: ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
len(frase)
for letra in range (len(junto)-1, -1, -1):
    inverso += junto[letra]
print("O inverso de {} é {}".format(junto, inverso))

if junto == inverso :
    print("Temos um palíndromo!")
else:
    print("Não é um palíndromo!")
