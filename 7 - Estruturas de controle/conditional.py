idade = input("Digite a sua idade: ")
sexo = input("Digite seu sexo (\"M\" para Masculino e \"F\" para Feminino): ")

if sexo[0].strip().upper() == "M":
    if int(idade) >= 65:
        print("Aposentadoria aprovada!")
    else:
        print(f"Desculpe você ainda não possui a idade necessária. Aguarde mais {65 - int(idade)} anos.")
        
elif sexo[0].strip().upper() == "F":
    if int(idade) >= 60:
        print("Aposentadoria aprovada!")
    else:
        print(f"Desculpe você ainda não possui a idade necessária. Aguarde mais {60 - int(idade)} anos.")
    
else:
    print("Opção Inválida! Tente novamente.")