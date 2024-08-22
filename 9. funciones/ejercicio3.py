"""Escriba un programa que invierta una palabra"""

def invertir_cadena(cadena):
    invertida = ""
    for letra in cadena :
        invertida = letra + invertida 
    return invertida 
print(invertir_cadena("Straykids"))