from random import randint


CAP = 1000

balde = 0

while(balde <= CAP):
    volume_copo = randint(95, 100)
    print(f"O copo foi enchido com {volume_copo}ML\n")
    balde += volume_copo
    print(f"O volume atual do balde é de {balde}ML\n")
print(f"O balde ultrapassou a capacidade máxima de {CAP}ML e está com {balde}ML")