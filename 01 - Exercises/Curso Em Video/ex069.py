#Ler idade e sexo de várias pessoas, a cada pessoa perguntar se quer continuar, 
#Mostrar ao final quantas pessoas tem 18+, quantos homens foram cadastrados e quantas mulheres tem 20-

dezoito = mulheres_vinte = homens = 0

while True:
    idade = int(input("Idade: "))
    while True:
        sexo = str(input("Sexo [M/F]: ")).strip().upper()[0]
        if sexo in "MF":
            break
        else:
            print("Opção inválida, tente novamente!")
    if idade >= 18:
        dezoito += 1
    if idade < 20 and sexo == "F":
        mulheres_vinte += 1
    if sexo == "M":
        homens += 1
    while True:
        resp = str(input("Deseja continuar? [S/N]: ")).strip().upper()[0]
        if resp in "SN":
            break
        else:
            print("Opção inválida, tente novamente!")
    if resp == "N":
        break
print(f"Ao todos {dezoito} pessoas tem mais de 18 anos.")
print(f"Dentre as pessoas listadas, {mulheres_vinte} são mulheres com menos de 20 anos.")
print(f"Foram cadastrados {homens} homens.")