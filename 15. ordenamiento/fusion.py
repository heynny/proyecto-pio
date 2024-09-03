def merge_sort(liasta):
    if len(lista)>1:
        mitad = len(lista)// 2

        izquierda = (lista)[:mitad]
        derecha = lista [lista:]

        print("generacion")
        print(izquierda)
        print(derecha)

        merge_sort(izquierda)
        merge_sort(derecha)

        i=j=k=0 
        while i < len(izquierda)and j< len(derecha):
            if izquierda[i]< derecha[j]:
                lista[k]= izquierda[i]
                i+= 1
            else:
                lista[k]= derecha [j]
                j+= 1
            k+= 1 

        while i < len(izquierda):
            lista[k]= izquierda[i]
            i+=1
            k+= 1

        while j < len(derecha):
            lista[k]= izquierda[j]
            j+=1
            k+= 1
            





#Ejemplo lista
lista = [5,8,2,1,4,7,3,6,9]
merge_sort(lista)
print(f"Lista Ordenada con el metodo merge sort: {lista}")

