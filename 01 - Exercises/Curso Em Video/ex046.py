#contagem regressiva de 10 a 0 com pause de 1 seg entre eles msg explodindo
from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print("KABUUM!!!")