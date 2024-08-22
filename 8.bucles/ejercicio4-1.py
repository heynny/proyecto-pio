"""Crear un programa que defina un número del 1 al 100. El jugador 
debe intentar adivinar el númeri, y el programa le indicará si esta caliente o frio (caliente 10 unidades o menos del número) """

import random 

numerosecreto = random.randint(1,100)
print("Adivinar el número entre el 1 al 100")

print(numerosecreto)

intento= int(input("Ingrese su intento"))


while intento != numerosecreto:
    if intento > numerosecreto:
        diferencia = intento - numerosecreto
    
    else:
        diferencia = numerosecreto -  intento 


    if diferencia <= 10:
        print("calente")
    
    else:
        print("frio")

    if intento < numerosecreto:
        print("el numero secreto es mayor")

    else:
        print("el numero secreto es menor")

    intento = int(input("Ingrese su intento"))

print("Lo lograste >_<")
