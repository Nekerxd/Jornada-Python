# Argumentos Nomeados

# def monta_pc(cpu, memoria, hd, monitor=17):
#     print("O computador montado foi: ")
#     print(f"\tCPU: {cpu}")
#     print(f"\tMemória: {memoria}")
#     print(f"\tHD: {hd}Tb")
#     print(f"\tMonitor: {monitor} polegadas")


# monta_pc("Core i7", hd=2, memoria=16, monitor=25)

# Argumentos Nomeados

def monta_pc(cpu, memoria, hd, *precos, monitor=17, **kwargs):
    print("O computador montado foi: ")
    print(f"\tCPU: {cpu}")
    print(f"\tMemória: {memoria}")
    print(f"\tHD: {hd}Tb")
    
    print(f"\tPreços praticados: ")
    
    for preco in precos:
        print(f"\t\t R$ {preco:.2f}")
    
    
    print(f"\tMonitor: {monitor} polegadas")
    print(f"\tOutros Atributos: ")
    
    for chave, valor in kwargs.items():
        print(f"\t\t {chave}: {valor}")


monta_pc("Core i7", 16, 2, 2500, 3199, 4200, monitor=25, webcam="Multilaser Webcam", teclado="Teclado Multilaser")