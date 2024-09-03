def burbuja(lista): #se empieza con formulas
    n= len(lista)#tamaño de nuestra lista
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j],lista[j+1]  = lista[j+1], lista[j] 


#ejemplo lista
lista =[5,8,2,6,7,4,1,3]
burbuja(lista)
print(f"Lista Ordenada con el metodo burbuja: {lista}")
