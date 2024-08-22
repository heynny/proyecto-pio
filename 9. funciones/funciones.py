"""las funciones son pequeños bloques"""
#funcion simple
def saludar():
    print("hola soy un funciones")
saludar()

#funcion con parametros
def saludar2(nombre):
    print(f"Hola {nombre}, Bienvenido a pio")


saludar2("heynny")
saludar2("Laura")

#funcion con valores  de retorno
def suma(numero1:int, numero2:int):
    return numero1 + numero2

resultado = suma(5,3)
print(resultado)



