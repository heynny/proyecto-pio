"""Escribe una funcion llamada es_par que reciba número 
devuelva el mayor de los dos"""

def es_par(numero):
    return numero % 2 == 0

num= int(input("Ingrese un numero"))
validacion=es_par(num)
print (validacion) 

