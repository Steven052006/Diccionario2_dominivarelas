import os 
pedidos = {}

def registrar_pedido():
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    direccion = input("Ingrese la dirección del cliente: ")
    contacto = input("Ingrese el contacto del cliente: ")
    sexo = input("Ingrese el sexo del cliente: ")
    descripcion_lugar = input("Ingrese la descripción del lugar para guiar al personal de entrega: ")

    nombre_producto = input("Ingrese el nombre del producto: ")
    referencia = input("Ingrese la referencia del producto: ")
    cantidad = int(input("Ingrese la cantidad del producto: "))

    pedido = {
        "cliente": {
            "nombre": nombre_cliente,
            "direccion": direccion,
            "contacto": contacto,
            "sexo": sexo,
            "descripcion_lugar": descripcion_lugar
        },
        "producto": {
            "nombre": nombre_producto,
            "referencia": referencia,
            "cantidad": cantidad
        }
    }

    id_pedido = len(pedidos) + 1

    pedidos[id_pedido] = pedido

    print(f"El pedido {id_pedido} ha sido registrado exitosamente.")

def ver_pedidos():
    for id_pedido, pedido in pedidos.items():
        print(f"\nPedido {id_pedido}:")
        print(f"Cliente: {pedido['cliente']['nombre']}")
        print(f"Dirección: {pedido['cliente']['direccion']}")
        print(f"Contacto: {pedido['cliente']['contacto']}")
        print(f"Sexo: {pedido['cliente']['sexo']}")
        print(f"Descripción del lugar: {pedido['cliente']['descripcion_lugar']}")
        print(f"Producto: {pedido['producto']['nombre']}")
        print(f"Referencia: {pedido['producto']['referencia']}")
        print(f"Cantidad: {pedido['producto']['cantidad']}")

while True:
    print("\nMenú principal:")
    print("1. Registrar pedido")
    print("2. Ver pedidos")
    print("3. Salir")

    opcion = int(input("Ingrese la opción deseada: "))

    if opcion == 1:
        registrar_pedido()
    elif opcion == 2:
        ver_pedidos()
    elif opcion == 3:
        print("Gracias por usar el aplicativo. Hasta luego.")
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")