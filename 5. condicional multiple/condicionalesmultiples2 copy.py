
ingreso = float(input("ingrese su salario"))
if ingreso >=0:

    if  ingreso < 100000:
     impuestos= ingreso * 0.05
    elif 100000 <= ingreso < 200000:
     impuestos= ingreso *0.15
    elif 200000<= ingreso <= 350000:
     impuestos= ingreso *0.20
    elif 350000<= ingreso < 600000:
     impuesto = ingreso * 0.30
    else:
     impuestos = ingreso * 0.45 
    print(f"el impuiesto que debe pagar es:{impuestos}")

else:
    print("Ingresos no validos")



