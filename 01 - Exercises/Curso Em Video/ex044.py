#Calcular valor pago e o método
# a vista dinheiro/cheque -10%, a vista cartão -5%, em até 2x cartão preço normal, 3x ou mais 20% de juros
valor = float(input("Preço das compras: "))
pgmt = int(input("""Formas de pagamento
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
Qual é a opção? """))
if pgmt == 1:
    print("A sua compra de R${:.2f} à vista no dinheiro/cheque saíra por R${:.2f}".format(valor, valor-(valor*0.1)))
elif pgmt == 2:
    print("A sua compra de R${:.2f} à vista no cartão saíra por R${:.2f}".format(valor, valor-(valor*0.05)))
elif pgmt == 3:
    print("A sua compra em 2x no cartão saíra por R${:.2f} por mês".format(valor/2))
    print("A sua compra de R${:.2f} parcelada em 2x no cartão saíra no total por R${:.2f}".format(valor, valor))
elif pgmt == 4:
    parcela = int(input("Em quantas parcelar quer pagar? "))
    total = valor + (valor*0.2)
    print("Sua compra em {}x no cartão saíra por R${:.2f} por mês".format(parcela, total/parcela))
    print("A sua compra de R${:.2f} parcelada em {}x no cartão saíra por R${:.2f}".format(valor, parcela, total))
else:
    print("Opção inválida")