"""Escribir un programa que siga piendo al usuario que ingrese 
una contraseña, hasta que coincida con una contraseña predefinida"""
#no se coloca la ñ porque es una mala practica


contrasena = "Yoamoelkpop"
intentocontrasena = input("Ingrese la contraseña")
intentos = 4

while intentocontrasena != contrasena : 
    intentos -= 1
    if intentos == 0: 

        break


    print("contraseña incorrecta, Intente nuevamente")
    intentocontrasena = input("ingrese contraseña")


print("Bienvenidahyunjinista")