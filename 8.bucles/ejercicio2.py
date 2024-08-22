"""Crear un programa que pida un número al usuario y los sume.
el rpograma termina cuando el usuarion ingrece un 0"""

suma = 0 
num = int(input("ingrese un número (ingrese 0 para salir)"))
# el signo ! e = queremos decir que es diferente 
while num != 0 :  #while busca la verdad
    suma += num
    num = int(input("Ingrese otro número"))

print(f"la suma de los números ingresados es {suma}")
