"""Escribir un programa que cuente cuantas vocales hay en una palabra ingresada por el usuario"""

palabra = input("ingrese una palabra").lower()
vocales = "aeiou"
numeros = "123456789"
caracteres = "+!#$%/()=?[]:;+-"
contador = 0 
tienenumeros = False 


for letra in palabra:

    if (letra in numeros or letra in caracteres):
       esvalido = True 
       break

    if letra in vocales:
        contador += 1

if tienenumeros:# lo mismo que poner (esvalido == True)
    print("Error, la palabra no es valida por que tiene números o caracteres")
else:
    print (f"el número de vocales en la palabra {palabra},es{contador}")
