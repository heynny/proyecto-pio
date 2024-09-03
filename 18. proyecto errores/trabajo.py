#programa de ventas de joyas y reloj
productos=[
    {"nombre":"anillo(s) de oro","precio": 300, "cantidad": 20},
    {"nombre":"anillo(s) de plata","precio": 180, "cantidad": 15},  
    {"nombre":"reloj(es) de oro","precio": 1000, "cantidad": 10},  
    {"nombre":"rolex","precio": 4000, "cantidad": 15}                                                         
]
carrito= []

def mostrar_productos():
        print(" -----------------------Menú de productos-----------------------------------")
        for i, producto in enumerate (productos):
            print(f"{i+1}. {producto["nombre"]} - precio ${producto["precio"]} - cantidad {producto["cantidad"]}")


def agregar_producto_al_carrito():
    mostrar_productos()
    try:
        opcion = int(input("introduce el producto que desees agregar al carrito "))
        if 1 <= opcion <= len (productos):
            cantidad = int(input("Ingrese la cantidad de productos que desees comprar: "))
            producto = productos[opcion - 1]

        if cantidad > producto ["cantidad"]:
            print("No hay suficientes existencias en stock")
        else:
            productos[opcion - 1]['cantidad'] -= cantidad
            carrito.append({"nombre": producto["nombre"], "precio": producto['precio'], "cantidad": cantidad})
            print(f"Felicidades, haz añadido {cantidad} {producto["nombre"]} exitosamente")

    except Exception as e:
        print("Se ha presentado un error", e)

def mostrar_carrito():
    if carrito:
        print("Carrito de compras.")
    for i, item in enumerate(carrito,1):
        print(f"{i}. Producto: {item['nombre']} - ${item['precio']} - cantidad: {item['cantidad']}")
    else:
        print("El carrito esta vacio")


def calcular_carrito():
    total = sum(item["precio"]* item ["cantidad"]for item in carrito)
    print(f"el total de pagar es {total}")

def finalizar_compra():
    mostrar_carrito()
    if carrito:
        calcular_carrito()
        confirmar = ("Desea finalizar la compra ya")


def main():
    
    while True:
        print("--------------------- Menu joyeria ---------------------")
        print("1-Mostrar productos disponibles")
        print("2- Añadir productos al carrito")
        print("3- Mostrar carrito")
        print("4- Finalizar compra, (pagar)")
        print("5- Salir de la compra")

        
        try:
            
            opcion = int(input("Elije una opcion: ")) 
            

            if opcion == 1:
                mostrar_productos()

            elif opcion == 2:
                agregar_producto_al_carrito()

            elif opcion == 3:
                mostrar_carrito()

            elif opcion == 4:
                finalizar_compra()

            elif opcion ==5:
                break 

            else:
                print("opcion no vali por favor selecionar del 1 al 5")
        except ValueError: print("dato no valido, ingresa un numero")
        except Exception:
            print("se ha presentado un error")

            
            

main()