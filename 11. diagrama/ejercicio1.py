A = 0
B = 0

while True:

    a= float(input("Ingrese primer número"))
    b= float(input("Ingrese segundo número"))

    if (a == b):
        print("Numeros no validos, los Números tiene que ser diferentes")

    else: 
        if a > b:
            print(" A es mayor")
        else:
            print("B es mayor")

        break