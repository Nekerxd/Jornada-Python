# print("    Strip    ".strip())
# print("maiúsculo".upper())
# print("minúsculo".lower())
# print("Te,xto c,o,m vár,i,as ví,rg,u,la,s".replace(",",""))
# print("O rato roeu a roupa do rei de roma".count("r"))
# print("Texto Centralizado".center(50, "="))
# print("Tecnológico".index("ó"))
# print("Alfanumérico".isnumeric())
# print("Teste de quebra de string com split".split(" "))
# print("Nome;Cidade;Idade;País".split(";"))
# print("este é um título".title())
# print("este é um título".capitalize())
# print("585".zfill(5))

#Encadeamento de funções
print("     Te;xt;o     ".strip().replace(";","").center(25, "=").upper())

#Tamanho de Strings
string_extensa = "Essa é uma string extensa. Como Faremos para saber seu tamanho?"

print(len(string_extensa))