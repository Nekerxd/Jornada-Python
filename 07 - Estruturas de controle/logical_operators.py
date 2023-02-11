# ============== Operadores Lógicos ==============

x = True
y = True

print("*** IS ***")

print(x is y)
print(True is False)

print("*** AND ***")

print(False and False)
print(False and True)
print(True and False)
print(True and True)

print("*** OR ***")

print(False or False)
print(False or True)
print(True or False)
print(True or True)

print("*** NOT ***")

print(not True)
print(not False)

# ============== Operadores de Comparação ==============

x = 10
y = 20

# ==
print(f"{x} == {y}: {x == y}")
# !-
print(f"{x} != {y}: {x != y}")
# >
print(f"{x} > {y}: {x > y}")
# >=
print(f"{x} >= {y}: {x >= y}")
# <
print(f"{x} < {y}: {x < y}")
# <=
print(f"{x} <= {y}: {x <= y}")

# ============== Operadores de Atribuição ==============

x = 100

print(f"valor inicial de x = {x}")

# +=
x += 10
x = x + 10
print(f"x += 10 = {x}\t(Equivalente: x = x + 10)")

# -=
x -= 5
print(f"x -= 5 = {x}\t(Equivalente: x = x - 5)")
# /=
x /= 5
print(f"x /= 5 = {x}\t(Equivalente: x = x / 5)")

# *=
x *= 5
print(f"x *= 5 = {x}\t(Equivalente: x = x * 5)")

# //=
x //= 20
print(f"x //= 20 = {x}\t(Equivalente: x = x // 20)")

# %=
x %= 3
print(f"x %= 3 = {x}\t(Equivalente: x = x % 3)")
