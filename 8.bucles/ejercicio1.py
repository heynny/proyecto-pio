"""programa que pida un número y lo muestre, 
el programa parara cuando se ingrese un número negativo"""

num= int(input("ingrese un número(ingrese un número para salir)"))

while num >= 0: 
    print(f"El número es: {num}")
    num= int(input("Ingrese otro numero"))
else:
    print("programa terminado...")
