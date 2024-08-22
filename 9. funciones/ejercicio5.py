"""programa de Calculadora"""

def suma (x,y):
    return x + y


def resta(x,y):
    return x - y

def multiplicacion( x,y):
    return x* y

def dividir (x,y):
    if y != 0 :
        return x/ y
    else:
        return "Error: Division por cero"

def opciones ():
    print("opciones:")
    print("1. suma")
    print("2. Restar")
    print("3. multiplicar")
    print("4. Dividir")
    print("5. salir")  

def calculadora ():
    

    while True: 
        operacion = int(input("Digite la opcion que desea:"))

        if operacion == 1: 
            
        elif operacion == 2:
            pass
        elif operacion == 3:
            pass
        elif operacion == 4:
            pass
        elif operacion == 5:
            print("Muchas gracias, saliendo...")
            break

        else: 
            
            print("#######################...")
            opciones ()




            print("opcion no valida...")
            print("#######################...")


calculadora()

