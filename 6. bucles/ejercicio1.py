"""crear un programa que imprima todos los numeros inpares del 1 al 10"""
for i in range(1,11,2):
    print(f"la tabla de multiplicar del {i}")
    for j in range(1,11):
        print(f"{i} * {j} = {i*j}")
    print () #separacion