def mostrar_menu () : 
    print ("1. añadir un contacto")
    print ("2. eliminar un contacto")
    print ("3. buscar un contacto")
    print ("4. mostar un contacto")
    print ("5. salir")


def anadir_contactos (contactos):
    nombre= input("ingrese nombre del contacto")
    telefono= input("ingrese numero de telefono")
    email= input("ingrese un email")
    contactos =[nombre]= {"telefono": telefono, "email": email}
    print("usuario guardado con exito")


def eliminar_contactos(contactos):
    nombre = input("nombre del contacto que desea eliminare")
    if nombre in  contactos:
        del contactos [nombre] 
        print ("contacto eliminado")
    else:
        print ("contacto no encontrado")


def buscar_contactos(contactos):
    nombre = input("nombre del contacto que desea buscar")
    if nombre in contactos :
        contacto=  contactos [nombre]
        print("nombre: {nombre}")
        print(f"telefono: {contacto ["telefono"]}")
        print(f"email: {contacto ["telefono"]}")




def mostrar_contactos ():
    pass


def main ():
    contactos =[]
    while True:
        mostrar_menu ()
        opcion= input ("seleccione una opción")
        if opcion == "i":
            anadir_contactos(contactos)

        elif opcion == "2":
            eliminar_contactos(contactos)
        elif opcion =="3": 
            buscar_contactos(contactos)
        elif opcion == "4":
            pass
        elif opcion == "5":
            break
        else:
            print("opcion no valida, por favor elija una opcion")
