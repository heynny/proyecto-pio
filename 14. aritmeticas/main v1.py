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





def main():

    limpiar_terminal
    while True:
        print("........ E-comerce.......")
        print("1. usuario")
        print("2. Administrador")
        print("3. salir")
        opcion =int (input("Elija un usuario para iniciar el app"))

        if opcion == 1:
            pass

        elif opcion == 2:
            print("------------Administrador------------")
            usuario = input("Nombre de usuario: ")
            contrasena = input("Contraseña: ")
            print(type(administradores))
            for administrador in administradores:
                if usuario in administrador["usuario"]:
                    if contrasena in administrador["contrasena"]:
                        print("Inicio sesion exitoso...")
                    else:
                        print("Contraseña incorrecto......")
                else:
                    print("Usuario incorrecto....")





        elif opcion ==3: 
            print("saliendo......")
            break

        else:
            print("opcion no valida..... enter para continmuar")
            limpiar_terminal()
            


main()
