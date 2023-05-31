# Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front. Return the string unchanged if the given string already begins with "Is".

def trata_string(frase):
    if len(frase) >= 2 and frase[:2] == "Is":
        return frase
    return "Is"+frase

print(trata_string("IsEmpty"))
print(trata_string("Teste"))