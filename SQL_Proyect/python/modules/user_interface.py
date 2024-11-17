def menu():
    print("""
        1. Tour y valoraciones del dia
        2. Reservas de tours anuales
        3. Ventas en viñas
        4. Informe de ganancias (último año)
        5. Informe Comparativo de ganancias (dos años) 
        6. Gráfico de Sectores
        7. Salir
        """)
    while True:
        opcion = input("Ingrese una opción: ")
        if opcion.isnumeric():
            opcion = int(opcion)
            if opcion >= 1 and opcion <= 7:
                return opcion
            else:
                print("Opción inválida.")
        else:
            print("Opción inválida.")
    

# Función para formatear los datos
def imprimir_detalles_opcion_1(datos):
    """Esta función imprime los detalles de los clientes que asistieron al viñedo en una fecha específica.

    Args:
        datos (dict): Diccionario con los datos de los clientes.
    """
    print("Clientes que asistieron al viñedo en esa fecha:\n")
    for cliente in datos:
        print(f"ID Tour Programado: {cliente['id_tour_programado']}")
        print(f"ID Tour: {cliente['id_tour']}")
        print(f"Nombre Cliente: {cliente['nombre_cliente']}")
        print(f"RUT: {cliente['rut'].strip()}")
        print(f"Fecha: {cliente['fecha']}")
        print(f"Hora Tour: {cliente['hora_tour_programado']}")
        print(f"Valoración: {cliente['valoracion']}")
        print(f"Descripción Reseña: {cliente['descripcion_resena']}")
        print("-" * 50)

# Función para formatear los datos
def imprimir_detalles_opcion_2(datos):
    """Esta función imprime los detalles de los clientes que asistieron al viñedo en una fecha específica.

    Args:
        datos (dict): Diccionario con los datos de los clientes.
    """
    for cliente in datos:
        print(f"ID Tour Programado: {cliente['id_tour_programado']}")
        print(f"ID Tour: {cliente['id_tour']}")
        print(f"Horario del Tour: {cliente['horario_tour']}")
        print(f"Fecha: {cliente['fecha']}")
        print(f"Hora del Tour Programado: {cliente['hora_tour_programado']}")
        print(f"N° de Operación: {cliente['n_operacion']}")
        print(f"Nombre Cliente: {cliente['nombre_cliente']}")
        print(f"RUT: {cliente['rut'].strip()}")
        print(f"Tipo de Pago: {cliente['tipo_pago']}")
        print(f"Número de Acompañantes: {cliente['numero_acompanantes']}")
        if cliente['lista_de_acompanantes']:
            print(f"Lista de Acompañantes: {cliente['lista_de_acompanantes']}")
        else:
            print(f"Lista de Acompañantes: Ninguno")
        print("-" * 50)
