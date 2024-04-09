import os 
despachos = {}

def registrar_despacho(placa, descripcion_vehiculo, nombre_propietario, contacto_propietario, ruta, descripcion_carga):
    id_despacho = len(despachos) + 1
    despachos[id_despacho] = {
        'placa': placa,
        'descripcion_vehiculo': descripcion_vehiculo,
        'nombre_propietario': nombre_propietario,
        'contacto_propietario': contacto_propietario,
        'ruta': ruta,
        'descripcion_carga': descripcion_carga
    }
    print(f'Despacho {id_despacho} registrado con éxito.')

def mostrar_despacho(id_despacho):
    if id_despacho in despachos:
        despacho = despachos[id_despacho]
        print(f'Despacho {id_despacho}:')
        print(f'Placa: {despacho["placa"]}')
        print(f'Descripción del vehículo: {despacho["descripcion_vehiculo"]}')
        print(f'Nombre del propietario: {despacho["nombre_propietario"]}')
        print(f'Contacto del propietario: {despacho["contacto_propietario"]}')
        print(f'Ruta: {despacho["ruta"]}')
        print(f'Descripción de la carga: {despacho["descripcion_carga"]}')
    else:
        print(f'Despacho {id_despacho} no encontrado.')

while True:
    print('\n<<<<< MENÚ PRINCIPAL >>>>>')
    print('1. Registrar despacho')
    print('2. Mostrar despacho')
    opcion = input('-> ')
    if opcion == '1':
        placa = input('Placa: ')
        descripcion_vehiculo = input('Descripción del vehículo: ')
        nombre_propietario = input('Nombre del propietario: ')
        contacto_propietario = input('Contacto del propietario: ')
        ruta = input('Ruta: ')
        descripcion_carga = input('Descripción de la carga: ')
        registrar_despacho(placa, descripcion_vehiculo, nombre_propietario, contacto_propietario, ruta, descripcion_carga)
    elif opcion == '2':
        id_despacho = input('ID de despacho: ')
        mostrar_despacho(int(id_despacho))
    else:
        print('Opción inválida. Por favor, inténtalo de nuevo.')