#Ler peso e altura, fazer imc e mostrar status
# < 18,5 abaixo do peso, >= 18,5 < 25 peso ideal, 25 a 30 sobrepeso, 30 a 40 obesidade, > 40 obesidade mórbida
peso = float(input("Peso em KG: "))
altura = float(input("Altura em metros: "))
imc = peso / pow(altura,2)
print("{:.2f}".format(imc))
if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc < 25:
    print("Peso ideal")
elif 25 <= imc < 30:
    print("Sobrepeso")
elif 30 <= imc < 40:
    print("Obesidade")
else:
    print("Obesidade Mórbida")