"""desafio: crear un programa que determine si un número ingresado por el usuario primo"""

numero= int(input("ingrese el numero"))
primo= True
for i in range(2,numero):
    if numero% numero == 0 and numero % i ==0:
        primo = False
        print(f"el numero {numero} no es un numero primo debido a que al dividirse entre {i}su residuo es 0")
        break

if primo : 
    print(f"el numero {numero} es un numero primo")