#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
metro = float(input("Uma distância em metros: "))
cm = metro * 100
mm = metro * 1000
print("A medida de {}m corresponde a {:.0f}cm e {:.0f}mm".format(metro, cm, mm))