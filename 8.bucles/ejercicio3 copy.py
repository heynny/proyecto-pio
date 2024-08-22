"""Escribir un programa que siga piendo al usuario que ingrese 
una contraseña, hasta que coincida con una contraseña predefinida"""
#no se coloca la ñ porque es una mala practica

#contraseña predefinida
contrasena = "Yoamoelkpop"
#Número maximo de intentos permitidos
intentos_max = 4
#contador de intentos
intentos= 0
#bucle para pedir la contraseña
while intentos < intentos_max:

    intentocontrasena = input("Ingrese contraseña")

    if intentocontrasena == contrasena :
        print("contraseña correcta")
        break # salir bucle
    else:
        intentos += 1
        intentos_restantes = intentos_max - intentos 

        if intentos_restantes  >0:
            print(f"contraseña incorrecta, te queda{intentos_restantes}intentos")
        else:
            print("has superado el numero maximo de intentos")
            break





print("Bienvenidahyunjinista")