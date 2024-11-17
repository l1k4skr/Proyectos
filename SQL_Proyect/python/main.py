"""
1. El programa debe mostrar un menu con las siguientes opciones:
    1. Tour y valoraciones del dia: Tour realizado con los clientes que asistieron en un día específico, con todo el detalle de sus valoraciones
    2. Reservas de tours anuales: Reserva de los distintos tours en todo el año
    3. Ventas en viñas : Ventas de productos en las distintas viñas
    4. Informe de ganancias (último año): Informe de ganancias del último año que incluya las ventas de productos y de tours mayor al promedio.
    5. Informe Comparativo de ganancias (dos años) : Informe de ganancias entre 2 años ingresados por el usuario que incluya las ventas de productos y de tours.
    6. Gráfico de Sectores: Gráfico de sectores que permita visualizar el número de clientes que visitaron lasdiferentes viñas en un año ingresado por el usuario.
"""
from modules import db_connection
from modules import queries_execution
from modules import user_interface
        


# Crear un cursor para ejecutar consultas
conexion = db_connection.conectar_base_datos()
cursor = conexion.cursor()

# Prueba: obtener versión de PostgreSQL
# cursor.execute("SELECT version();")
# version = cursor.fetchone()
# print(f"Versión de PostgreSQL: {version}")


if '__main__' == __name__:
    
    
    opcion = user_interface.menu()
    if opcion == 1:
        """
        Fecha (año, mes, día) para mostrar los tours realizados en esa fecha.
        salida:
        - ID Tour Programado
        - ID Tour
        - Horario del Tour
        - Fecha
        - Hora del Tour Programado
        - Rut
        - Nombre Cliente
        """
        queries_execution.consulta_opcion_1(cursor)
    
    elif opcion == 2:
        queries_execution.consulta_opcion_2(cursor)
                
    elif opcion == 3:
        queries_execution.consulta_opcion_3(cursor)
        
    elif opcion == 4:
        queries_execution.consulta_opcion_4(cursor)
        
    elif opcion == 5:
        queries_execution.consulta_opcion_5(cursor)
        
    elif opcion == 6:
        queries_execution.consulta_opcion_6(cursor)
        
    elif opcion == 7:
        # Cierra el cursor y la conexión
        cursor.close()
        conexion.close()
        print("Hasta luego")
        exit()
    else:
        print("Opción inválida.")
        exit()