"""Determinar si un numero si un numero es positivo negativo o cero"""
numero = int(input("ingrese un número : "))
if numero == 0:
    print(f"el numero {numero} es cero")
elif numero >0:
    print(f"el numero {numero}es positivo")
else: 
    print(f"el numero {numero} es negativo")