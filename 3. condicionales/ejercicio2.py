Distancia= float(input("ingresar la distancia recorrieda en kilometros"))
if Distancia <= 1:
    tarifa=5 
elif Distancia <= 5:
    tarifa=5 + ( Distancia-1) *2
else:
    tarifa= 13+ (Distancia-5)*1.5
print("la tarifa del taxi es", tarifa)
