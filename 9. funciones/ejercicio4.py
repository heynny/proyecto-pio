"""Vamos a crear programa que simule el juego de Ahorcados"""


import random

"lista de palabras para el juego"
palabras = ["kpop","straykids","Exo","Boynextdoor","Enhypen"]

def elegir_palabra(palabras:list):
    #elegimos la palabra
    return random.choice(palabras)

def jugar_adivinar_palabra(palabra):
    intentos = 4

    print("!Bienvenidos al juego de adivinar la palabra¡")
    print(f"Tienes {intentos} intentos para adivinar la palabra.")

    while intentos > 0:
        intento= input("Adivina la palabra:").lower()

        if intento == palabra:
            print(f"Felicidades, Adivinaste la palabra")
            break
        else:
            intentos -=1
            if intentos > 0:
                print(f"Incorrectos, te quedan intentos { intentos}")
            else:
                print(f"Te has quedado sin intentos. la palabra era {palabra}")


palabra = elegir_palabra(palabras)
jugar_adivinar_palabra(palabra)