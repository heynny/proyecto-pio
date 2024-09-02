def comparador (a,b):
    if(a ==b):

        print("Error números iguales, tienes que cambiar el número")
        return False 

    else:
        if a > b:
            print ("A es mayor")
            return True 
        else:
            print("B es mayor")
            return("B es mayor")

def main ():
    while True:
        a = float(input("Ingrese primer número"))
        b = float(input("Ingrese segundo número"))

        if comparador (a, b) : break


main()