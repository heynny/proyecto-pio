# Lista de libros en la biblioteca (predefinidos)
libros = [
    {
        "titulo": "Cien Años de Soledad",
        "autor": "Gabriel García Márquez",
        "isbn": "978-3-16-148410-0",
        "genero": "Ficción",
        "cantidad": 5
    },
    {
        "titulo": "Don Quijote de la Mancha",
        "autor": "Miguel de Cervantes",
        "isbn": "978-1-23-456789-7",
        "genero": "Clásico",
        "cantidad": 3
    },
    {
        "titulo": "La Odisea",
        "autor": "Homero",
        "isbn": "978-0-12-345678-9",
        "genero": "Épico",
        "cantidad": 4
    }
]


#lista usuario
usuarios = []


#función para a gregar un libro al inventario

def agregar_libro ():
    print("......Agregar libro........")
    titulo= input("Ingresa el titulo del libro")
    autor = input("Ingresa el Autor del libro")
    isbn = input("Ingresa el ISBN del libro")
    genero= input("Ingresa el Genero del libro")
    cantidad = int(input("Ingresa el Cantidad de ñibros disponibles"))

    
    nuevo_libro= {
        "titulo": titulo,
        "autor" :autor,
        "isbn" : isbn,
        "genero":  genero,
        "cantidad":cantidad
    }

    libros.append(nuevo_libro)
    print(f"libro{titulo} agregar al inventario")

#función para editar un libro del inventario
def editar_libro ():
    print(".......Editar libro......")
    mostrar_libros ()
    isbn = input("Ingrese el ISBN del libro que dea editar: ")
    for libro in libro :
        if libro ["isbn"]== isbn:
            libro ["titulo"]= input (f"Ingrese el nuevo titulo del libro({libro["titulo"]}):")
            libro ["autor"]= input (f"Ingrese el nuevo titulo del libro({libro["autor"]}):")
            libro ["genero"]= input (f"Ingrese el nuevo titulo del libro({libro["genero"]}):")
            libro ["cantidad"]= input (f"Ingrese el nuevo titulo del libro({libro["cantidad"]}):")

            print(f"El libro con ISBN: {isbn} ha sido actualizado")




#función para eliminar libro del inventario
def eliminar_libro ():
    print(".......Eliminar libro.......")
    mostrar_libros()
    isbn= input ("Ingrese el ISBN del que desea eliminar: ")
    global libros
    libros = [libro for libro in libros if libro['isbn'] != isbn]
    print(f"El libro con el ISBN: {isbn} ha sido eliminado")

#funcion para mostrar todos los libros del inventario
def mostrar_libros ():
    if libros: 
        print("lista de libros en la biblioteca")
        for libro in libros:
            print(f"{libro["titulo"]} - {libro["autor"]}- ISBN: {libro["isbn"]}- {libro["genero"]}-{libro["cantidad"]}")
    else:
        print("No hay libros en el inventario")



#función para a gregar un usuario 

def agregar_usuario ():
    print("......Agregar usuario........")
    nombre= input("Ingresa el nombre del usuario")
    usuario_id = input("Ingresa el id del usuario")
    

    nuevo_usuario= {
        "nombre": nombre,
        "usuario_id" : usuario_id,
        "prestamo": []}
    
    usuarios.append(nuevo_usuario)
    print(f"Usuario {nombre} fue afregado con exito")


#función para editar un usuario
def editar_usuario ():
    print("---------- Editar usuario ----------")
    mostrar_usuario()
    usuario_id = input("Ingrese el id del usuario que desea editar: ")
    for usuario in usuarios:
        if usuario["usuario_id"] == usuario_id:
            usuario['nombre'] = input(f"Ingrese el nuevo nombre dle usuario({usuario['nombre']}): ")
            print(f"Usuaruio {usuario_id} editado con exito")



#función para eliminar  usuario 
def eliminar_usuario():
    pass

#funcion para mostrar todos los  usuarios
def mostrar_usuario ():
    if usuarios:
        print("lista de usuariois")
        for usuario in usuarios:
            print(f"{ usuario [ "usuario_id"]}- {usuario ["nombre"]}  ")
    else: 
        print("no hay usuarios registrados")




#funcion para registrar el prestamo del libro
def registrar_prestamo():
    mostrar_libros()
    isbn = input ("ingrese el ISBN del libro que desea prestar")
    libro= next((libro for libro in libros if libro ["isbn"]== isbn), None) 


    if libro and libro ["cantidad"]> 0:
        mostrar_usuario()
        usuario_id= input("ingrese el ID del usuario")
        usuario= next((usuario for usuario in usuarios if usuario ["usuario_id"]== usuario_id), None) 


        if usuario:
            libro["cantidad"]-= 1
            usuario ["prestamo"].append(libro["titulo"])
            print(f"prestamo registrado {libro["titulo"]}al usuario {usuario["nombre"]}con el id {usuario["usuario_id"]}")
        else: 
            print("usuario no encontrado")
    else: 
        print (" libro no disponible o encontrado")

#funcion para registrar la devolucion del libro
def registrar_devolucion():
    pass


# funcion para infoprmes de libros prestados
def informe_prestamos():
    pass


#funcion principal de menu
def menu():
    while True :
        print(".......menu.....")
        print("1. agregar libro")
        print("3. Eliminar libro")
        print("4. Mostar libros")
        print("5. Agregar usuario")
        print("6. Editar usuario")
        print("7. Eliminar usuario")
        print("8. Mostar usuarios")
        print("9. Registar prestamo de libro")
        print("10. Devolver libro")

        print("0. Finalizar")


        opcion = int(input("Selecciona una opcion: "))

        if opcion == 1:
            agregar_libro()
        elif opcion == 2:
            editar_libro()
        elif opcion == 3:
            eliminar_libro()
        elif opcion == 4:
            mostrar_libros()
        elif opcion == 5:
            agregar_usuario()
        elif opcion == 6:
            editar_usuario()
        elif opcion == 7:
            eliminar_usuario()
        elif opcion == 8:
            mostrar_usuario()
        elif opcion == 9:
            registrar_prestamo()
        elif opcion == 10:
            registrar_devolucion()
            

        elif opcion == 0:
            break


