"""Crear un programa que defina un número del 1 al 100. El jugador 
debe intentar adivinar el número, y el programa le indicará si esta caliente o frio (caliente 10 unidades o menos del número) """

import random 

numerosecreto = random.randint(1,100)
print("Adivinar el número entre el 1 al 100")

numero_intentos= 6
intentos_restantes = numero_intentos

while intentos_restantes > 0:
    intento = int(input(f"Te quedan {intentos_restantes} intentos. Ingresa tu número: "))

    if intento == numerosecreto:
        print(f"¡Felicidades! Adivinaste el número en {numero_intentos - intentos_restantes + 1} intentos.")
        break

    diferencia= abs(intento - numerosecreto)
    
    if diferencia <= 10:
        print("caliente")
    else:
        print("frio")

    if intento > numerosecreto :
        print("el número secreto es menor")
    elif intento < numerosecreto:
        print("el número secreto es mayor")

    intentos_restantes -= 1

    if intentos_restantes == 0:
        print(f"lo sentimos. se acabaron tus intentos, el numero secreto era {numerosecreto}.")
        

        
