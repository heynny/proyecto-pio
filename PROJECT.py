def addProduct_Cart(name, cant):
    try:
        product = next((p for p in productos if p["nombre"].lower() == name.lower()), None)
        
        if not product:
            print("Producto no encontrado. Verifica el nombre del producto.")
            return

        if product["stock"] < cant:
            print("No hay suficiente stock.")
            return

        confirm = input(f"¿Desea agregar {cant} unidades de {product['nombre']} al carrito? (s/n): ").lower()
        if confirm != "s":
            print("Operación cancelada.")
            return

        itemCart = next((cart for cart in carrito if cart["nombre"].lower() == name.lower()), None)
        
        if itemCart:
            itemCart["cantidad"] += cant
            itemCart["precio"] = product["precio"] * itemCart["cantidad"]
        else:
            carrito.append({
                "nombre": product["nombre"],
                "cantidad": cant,
                "precio": product["precio"] * cant
            })
        
        product["stock"] -= cant
        print(f"Se ha agregado {cant} unidades de {product['nombre']} al carrito.")
        
    except Exception as e:
        print("Se ha presentado un error al añadir al carrito:", e)
