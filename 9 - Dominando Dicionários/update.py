computador = {
    "cpu": "Core i7 12700k",
    "ram": "DDR4 16Gb",
    "ssd": "Samsung Evo 840 256Gb",
    "gpu": "RTX 2080 Ti"
}

print(f"Computador v1: {computador}")

computador["ram"] = "DDR4 32Gb"

print(f"Computador v2: {computador}")

computador["fonte"] = "Fonte 650W Corsair"

print(f"Computador v3: {computador}")

computador.update({"fonte" : "Fonte 850W Corsair", "ssd" : "Samsung Evo 840 1Tb" })

print(f"Computador v4: {computador}")