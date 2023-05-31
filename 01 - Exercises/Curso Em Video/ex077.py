#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
#Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

lista = ("Claro", "Ventilador", "Espinho", "Madri", "Vagabundo",
        "Salada", "Superar", "Rabino", "Pacemaker", "Dedo", 
        "Adolescente", "Segar", "Clara", "Audiofone", "Faca",
        "Fagote", "Representar", "Panda", "Assobio", "Pessoas")


for c in lista:
    print(f"\nNa palavra {c.capitalize()} temos: ", end="")
    for letra in c:
        if letra.upper() in "AEIOU":
            print(f"{letra.lower()}", end=" ")
