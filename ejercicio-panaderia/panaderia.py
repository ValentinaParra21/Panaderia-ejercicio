# panaderia.py

# Inventario inicial de productos
inventario = {
    "pan": {"precio": 1200, "stock": 40},
    "leche": {"precio": 4200, "stock": 25},
    "huevo": {"precio": 500, "stock": 180}
}



def mostrar_menu():
    print("""
1) Consultar precio y stock
2) Registrar venta
3) Agregar nuevo producto
4) Mostrar inventario completo
0) Salir
""")

def consultar_precio_y_stock():
    producto = input("Ingrese el nombre del producto: ").lower()
    datos = inventario.get(producto)

    if datos:
        print(f"Precio: ${datos['precio']}, Stock: {datos['stock']}")
    else:
        print("Producto no disponible.")

def registrar_venta():
    producto = input("Ingrese el producto: ").lower()
    datos = inventario.get(producto)

    if not datos:
        print("Producto no disponible.")
        return

    try:
        cantidad = int(input("Ingrese la cantidad: "))
    except ValueError:
        print("La cantidad debe ser un número entero.")
        return

    if cantidad <= 0:
        print("La cantidad debe ser mayor que cero.")
    elif cantidad > datos["stock"]:
        print("No hay stock disponible.")
    else:
        total = cantidad * datos["precio"]
        inventario[producto]["stock"] -= cantidad
        print(f"Venta registrada. Total a pagar: ${total}")

def agregar_producto():
    producto = input("Nombre del producto: ").lower()
    
    try:
        precio = int(input("Precio: "))
        stock = int(input("Stock inicial: "))
    except ValueError:
        print("Precio y stock deben ser números enteros.")
        return

    if producto in inventario:
        print("Producto ya existe. Actualizando datos...")
    else:
        print("Producto agregado correctamente.")

    inventario[producto] = {"precio": precio, "stock": stock}

def mostrar_inventario():
    print("\n--- Inventario completo ---")
    for producto, datos in inventario.items():
        print(f"{producto.capitalize()}: Precio ${datos['precio']} | Stock {datos['stock']}")
    print("-----\n")

def ejecutar_menu():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            consultar_precio_y_stock()
        elif opcion == "2":
            registrar_venta()
        elif opcion == "3":
            agregar_producto()
        elif opcion == "4":
            mostrar_inventario()
        elif opcion == "0":
            print("Programa finalizado.")
            break
        else:
            print(" Intente nuevamente.")


ejecutar_menu()
