import os

def limpiar_terminal ():
    if os.name== "nt": os.system ("cls")#win
    else: os.system("clear")

limpiar_terminal()

