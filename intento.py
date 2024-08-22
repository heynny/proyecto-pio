import random

numerosecreto = random.randint(1, 100)
print("Adivina el número entre 1 al 100")

numero_intentos = 6
intentos_restantes = numero_intentos

while intentos_restantes > 0:
    intento = int(input(f"Te quedan {intentos_restantes} intentos. Ingresa tu número: "))

    if intento == numerosecreto:
        print(f"¡Felicidades! Adivinaste el número en {numero_intentos - intentos_restantes + 1} intentos.")
        break

    diferencia = abs(intento - numerosecreto)

    if diferencia <= 10:
        print("Caliente")
    else:
        print("Frío")

    if intento > numerosecreto:
        print("El número secreto es menor.")
    elif intento < numerosecreto:
        print("El número secreto es mayor.")

    intentos_restantes -= 1

    if intentos_restantes == 0:
        print(f"Lo siento, se acabaron los intentos. El número secreto era {numerosecreto}.")