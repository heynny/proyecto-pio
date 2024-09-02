import os

productos = [
    {"nombre":"laptop", "precio": 300000.00, "stock": 10},
    {"nombre":"mouse", "precio": 150000.00, "stock": 20},
    {"nombre":"teclado", "precio": 100000.00, "stock": 15},
    {"nombre":"monitor", "precio": 60000.00, "stock": 5},
]


#carrito
carrito= []

cupones = [
    {"cupon":"COMPRAMAX100","descuento":15, "min": 10000, "limite": 3}
]

administradores = [
    {"usuario": "hyunjin", "contrasena": "skz817"},
    {"usuario": "Sunghoon", "contrasena": "ehp720"}
]


def limpiar_terminal ():
    if os.name== "nt": os.system ("cls")#win
    else: os.system("clear")


def opcion_no_valida():
    input("Opcion no valida....... Enter para continuar")
    limpiar_terminal()

def mostrar_producto():
    pass

def agregar_producto_al_carrito():
    pass

def mostrar_carrito ():
    pass

def calcular_carrito():
    pass

def calcular_producto():
    pass

def vaciar_carrito():
    pass

def procesar_compra():
    pass

def eliminar_un_producto_del_carrito():
    pass


def cliente(nombre):

    def carrito():

        def agregar():
            pass
        
        def eliminar():
            pass

        def actualizar():
            pass

        def vaciar():
            pass
def administrador(elemento, peticion): 
    
    def saludar():
        print("hola")

    def productos():

        def agregar():
            pass

        def eliminar ():
            pass
    
        def actualizar():
            pass

    def cupones():
        def agregar():
            pass

        def eliminar():
            pass

        def actualizar ():
            pass

    if (elemento == "cupones" & peticion== "crear"):
        print("crear cupones")





def main():

    limpiar_terminal()
    while True:
        print("........ E-comerce.......")
        print("1. usuario")
        print("2. Administrador")
        print("3. salir")
        opcion =int (input("Elija un usuario para iniciar el app"))

        if opcion == 1:
            pass

        elif opcion == 2:
            limpiar_terminal() #limpiar terminal
            print("......Administrador............")
            sesion= False
            usuario = input("Nombre de usuario:")
            contrasena = input("contrasena:")

            for administrador in administradores : #recorremos la lissta de administradores 
                if (usuario in administrador["usuariuo"] ) & (contrasena in administrador ["contrasena"]):
                    sesion = True 
                    limpiar_terminal()

                if sesion:
                    
                    print(f".................Administrador {usuario}................")
                    print("1. productos")
                    print("2. cupones")
                    opcion= int(input(f"Elija una opcion para trabajar"))

                    if opcion == 1:
                        pass
                    elif opcion == 2:
                        print(f".................Administrador {usuario}................")
                        print("1. crear un cupon ")
                        print("2. actualizar ")
                        print("3.eliminar")
                        opcion= int(input(f"Elija una opcion para trabajar"))
                        if opcion == 1: 
                            administrador("cupones","crear")


                    elif opcion == 3:
                        print("saliendo")
                        break

                    else: opcion_no_valida()
                        
            
            if sesion == False: print("Nombre o contraseña no validos...")


        elif opcion ==3: 
            print("saliendo......")
            break

        else: opcion_no_valida()


main()
