#ejercisio sobre condicional edad y licencia de conducir


edad= int(input("Ingrese su edad"))

if edad >= 18:
    
    tiene_licencia = int(input("¿Tiene licencia de conducir?(1 para si, 2 para no): "))

    if tiene_licencia ==1:
        print("Puede conducir")
    else:
        print("No puede conducir sin licencia")
else:
    print("Eres menor de edad, no puedes conducir")
