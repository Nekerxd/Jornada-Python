from random import randint

veiculos = ["Carro", "Moto", "Bicicleta", "Barco"]

# for veiculo in veiculos:
#     print(f"O tipo de veículo é: {veiculo}")
    
# for veiculo in veiculos:
#     kilometragem = randint(0, 100)
#     print(f"O veículo {veiculo} possui {kilometragem}Km rodados.")

kilometragem = [randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100)]

for veiculo, km in zip(veiculos, kilometragem):
    print(f"O veículo {veiculo} já percorreu {km}Km")