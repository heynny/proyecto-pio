def busqueda_lineal(lista,x):
    for i in range (len(lista)):
        if lista [i]== x:
            return -1
    return "dato no encontrado"



#ejemplo lista
lista = [5,8,2,1,4,7,3,6,9]
x=4
resultado = busqueda_lineal(lista,x)
print(f"Elemento encontrado en el indice{resultado}")

#entre menos datos haya es mas funcional 