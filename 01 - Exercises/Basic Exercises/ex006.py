# Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.

nums = input("Digite uma sequência de números separados por vírgulas: ")

lista = list(nums.split(","))
tupla = tuple(nums.split(","))

print(f"Lista: {lista}")
print(f"Tupla: {tupla}")