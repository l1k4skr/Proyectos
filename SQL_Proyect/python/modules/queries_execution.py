from modules import user_interface
import seaborn as sns
import matplotlib.pyplot as plt

# seaborn settings
sns.set_theme(style="whitegrid")
sns.set_context("paper", font_scale=1.5)


def consulta_opcion_1(cursor):
    """Esta función ejecuta la consulta para obtener los datos de los clientes que asistieron al viñedo en una fecha específica.

    Args:
        consulta (str): Consulta SQL.
        cursor (psycopg2.extensions.cursor): Cursor de la conexión a la base de datos.

    Returns:
        list: Lista con los datos de los clientes.
    """
    ano = int(input("Ingrese el año: "))
    mes = int(input("Ingrese el mes: "))
    dia = int(input("Ingrese el dia: "))
    
    fecha = f"{ano}-{mes}-{dia}"
    consulta = f"""
        SELECT
    tp.ID_tour_programado,
    t.ID_tour,
    t.Horario AS Horario_Tour,
    tp.Fecha,
    tp.Hora AS Hora_Tour_Programado,
    c.Rut,
    c.Nombre AS Nombre_Cliente,
    COALESCE(r.Valoracion, 5) AS Valoracion,
    COALESCE(r.Descripcion, 'Sin descripción') AS Descripcion_Resena
FROM
    Tour_Programado tp
    JOIN Tour t ON tp.ID_tour = t.ID_tour
    JOIN Reserva_Tour_Programado rtp ON tp.ID_tour_programado = rtp.ID_tour_programado
    JOIN Reserva res ON rtp.N_operacion = res.N_operacion
    JOIN Cliente c ON res.Rut = c.Rut
    LEFT JOIN Resena r ON tp.ID_tour_programado = r.ID_tour_programado AND c.Rut = r.Rut
WHERE
    tp.Fecha = '{fecha}'
ORDER BY
    tp.Hora, c.Nombre;
    """
    
    cursor.execute(consulta)
    tour_por_dia = cursor.fetchall()
    
    # Recuperar nombres de las columnas
    columnas = [desc[0] for desc in cursor.description]

    # Convertir a lista de diccionarios
    datos_dict = [dict(zip(columnas, fila)) for fila in tour_por_dia]

    # Imprimir los detalles
    user_interface.imprimir_detalles_opcion_1(datos_dict)
    
def consulta_opcion_2(cursor):
    """Esta función ejecuta la consulta para obtener los datos de los clientes que asistieron al viñedo en un año específico.

    Args:
        consulta (str): Consulta SQL.
        cursor (psycopg2.extensions.cursor): Cursor de la conexión a la base de datos.

    Returns:
        list: Lista con los datos de los clientes.
    """
    anio = int(input("Ingrese el año: "))
    consulta = f"""
        SELECT
    tp.ID_tour_programado,
    t.ID_tour,
    t.Horario AS Horario_Tour,
    tp.Fecha,
    tp.Hora AS Hora_Tour_Programado,
    res.N_operacion,
    c.Rut,
    c.Nombre AS Nombre_Cliente,
    res.Tipo_pago,
    res.Numero_acompanantes,
    res.Lista_de_acompanantes
FROM
    Tour_Programado tp
    JOIN Tour t ON tp.ID_tour = t.ID_tour
    JOIN Reserva_Tour_Programado rtp ON tp.ID_tour_programado = rtp.ID_tour_programado
    JOIN Reserva res ON rtp.N_operacion = res.N_operacion
    JOIN Cliente c ON res.Rut = c.Rut
WHERE
    EXTRACT(YEAR FROM tp.Fecha) = {anio}
ORDER BY
    tp.Fecha, tp.Hora, c.Nombre;
"""
    cursor.execute(consulta)
    tour_anual = cursor.fetchall()
    
    # Recuperar nombres de las columnas
    columnas = [desc[0] for desc in cursor.description]
    
    # Convertir a lista de diccionarios
    datos_dict = [dict(zip(columnas, fila)) for fila in tour_anual]
    
    # Convertir a lista de listas para tabular
    user_interface.imprimir_detalles_opcion_2(datos_dict)
    
def consulta_opcion_3(cursor):
    
    consulta = """SELECT
    v.Nombre AS Nombre_Vinedo,
    SUM(d.Cantidad * vi.Precio) AS Total_Ventas
FROM
    Vinedo v
    JOIN Sala_de_Venta sv ON v.ID_vinedo = sv.ID_vinedo
    JOIN Compra c ON sv.Codigo = c.Codigo
    JOIN Detalle d ON c.ID_compra = d.ID_compra
    JOIN Vino vi ON d.ID_vino = vi.ID_vino
GROUP BY
    v.Nombre
ORDER BY
    Total_Ventas DESC;"""
    cursor.execute(consulta)
    ventas_vinedos = cursor.fetchall()
    print("Ventas en viñas:\n")
    for venta in ventas_vinedos:
        print(f"Vinedo: {venta[0]}")
        print(f"Total de ventas: {venta[1]}")
        print("-" * 50)

def consulta_opcion_4(cursor):
    anio = int(input("Ingrese el año: "))
    consulta = f"""WITH Ventas_Productos AS (
SELECT
    c.ID_compra,
    SUM(d.Cantidad * v.Precio) AS Total_Compra
FROM
    Compra c
    JOIN Detalle d ON c.ID_compra = d.ID_compra
    JOIN Vino v ON d.ID_vino = v.ID_vino
WHERE
    EXTRACT(YEAR FROM c.Fecha) = {anio}
GROUP BY
    c.ID_compra
),
Ventas_Tours AS (
SELECT
    r.N_operacion,
    (1 + r.Numero_acompanantes) * t.Precio AS Total_Reserva
FROM
    Reserva r
    JOIN Reserva_Tour_Programado rtp ON r.N_operacion = rtp.N_operacion
    JOIN Tour_Programado tp ON rtp.ID_tour_programado = tp.ID_tour_programado
    JOIN Tour t ON tp.ID_tour = t.ID_tour
WHERE
    EXTRACT(YEAR FROM r.Fecha) = {anio}
),
Total_Ganancias AS (
SELECT Total_Compra AS Total FROM Ventas_Productos
UNION ALL
SELECT Total_Reserva AS Total FROM Ventas_Tours
),
Promedio_Ganancias AS (
SELECT AVG(Total) AS Promedio FROM Total_Ganancias
)
SELECT
'Producto' AS Tipo,
vp.ID_compra AS ID_Operacion,
vp.Total_Compra AS Total_Venta
FROM
Ventas_Productos vp
CROSS JOIN Promedio_Ganancias pg
WHERE
vp.Total_Compra > pg.Promedio
UNION ALL
SELECT
'Tour' AS Tipo,
vt.N_operacion AS ID_Operacion,
vt.Total_Reserva AS Total_Venta
FROM
Ventas_Tours vt
CROSS JOIN Promedio_Ganancias pg
WHERE
vt.Total_Reserva > pg.Promedio;
""" 
    cursor.execute(consulta)
    ganancias_ultimo_anio = cursor.fetchall()
    consulta2 = f"""WITH Ventas_Productos AS (
SELECT
    c.ID_compra,
    SUM(d.Cantidad * v.Precio) AS Total_Compra
FROM
    Compra c
    JOIN Detalle d ON c.ID_compra = d.ID_compra
    JOIN Vino v ON d.ID_vino = v.ID_vino
WHERE
    EXTRACT(YEAR FROM c.Fecha) = {anio}
GROUP BY
    c.ID_compra
),
Ventas_Tours AS (
SELECT
    r.N_operacion,
    (1 + r.Numero_acompanantes) * t.Precio AS Total_Reserva
FROM
    Reserva r
    JOIN Reserva_Tour_Programado rtp ON r.N_operacion = rtp.N_operacion
    JOIN Tour_Programado tp ON rtp.ID_tour_programado = tp.ID_tour_programado
    JOIN Tour t ON tp.ID_tour = t.ID_tour
WHERE
    EXTRACT(YEAR FROM r.Fecha) = {anio}
)
SELECT
AVG(Total) AS Promedio_Ganancias_Anual
FROM (
SELECT Total_Compra AS Total FROM Ventas_Productos
UNION ALL
SELECT Total_Reserva AS Total FROM Ventas_Tours
) AS Total_Ganancias;
"""
    cursor.execute(consulta2)
    promedio_ganancias = cursor.fetchone()
    
    print(f"Promedio de ganancias anual: {round(promedio_ganancias[0], 2)}")
    print(f"Ganancias superiores al promedio del último año ({anio}):\n")
    for ganancia in ganancias_ultimo_anio:
        print(f"Tipo: {ganancia[0]}")
        print(f"ID de Operación: {ganancia[1]}")
        print(f"Total de Venta: {ganancia[2]}")
        print("-" * 50)

def consulta_opcion_5(cursor):
    anio1 = int(input("Ingrese el primer año a comparar: "))
    anio2 = int(input("Ingrese el segundo año a comparar: "))
    consulta = f"""WITH Ventas_Productos AS (
SELECT
    EXTRACT(YEAR FROM c.Fecha) AS Anio,
    SUM(d.Cantidad * v.Precio) AS Total_Productos
FROM
    Compra c
    JOIN Detalle d ON c.ID_compra = d.ID_compra
    JOIN Vino v ON d.ID_vino = v.ID_vino
WHERE
    EXTRACT(YEAR FROM c.Fecha) IN ({anio1}, {anio2})
GROUP BY
    EXTRACT(YEAR FROM c.Fecha)
),
Ventas_Tours AS (
SELECT
    EXTRACT(YEAR FROM r.Fecha) AS Anio,
    SUM((1 + r.Numero_acompanantes) * t.Precio) AS Total_Tours
FROM
    Reserva r
    JOIN Reserva_Tour_Programado rtp ON r.N_operacion = rtp.N_operacion
    JOIN Tour_Programado tp ON rtp.ID_tour_programado = tp.ID_tour_programado
    JOIN Tour t ON tp.ID_tour = t.ID_tour
WHERE
    EXTRACT(YEAR FROM r.Fecha) IN ({anio1}, {anio2})
GROUP BY
    EXTRACT(YEAR FROM r.Fecha)
),
Ganancias_Anuales AS (
SELECT
    COALESCE(vp.Anio, vt.Anio) AS Anio,
    COALESCE(vp.Total_Productos, 0) AS Total_Productos,
    COALESCE(vt.Total_Tours, 0) AS Total_Tours,
    COALESCE(vp.Total_Productos, 0) + COALESCE(vt.Total_Tours, 0) AS Total_Ganancias
FROM
    Ventas_Productos vp
    FULL OUTER JOIN Ventas_Tours vt ON vp.Anio = vt.Anio
)
SELECT
Anio,
Total_Productos,
Total_Tours,
Total_Ganancias
FROM
Ganancias_Anuales
WHERE
Anio IN ({anio1}, {anio2})
ORDER BY
Anio;"""
    cursor.execute(consulta)
    ganancias_dos_anios = cursor.fetchall()
    for dato in ganancias_dos_anios:
        print(f"Año: {dato[0]}")
        print(f"Total de Productos: {dato[1]}")
        print(f"Total de Tours: {dato[2]}")
        print(f"Total de Ganancias: {dato[3]}")
        print("-" * 50)
def consulta_opcion_6(cursor):
    anio = int(input("Ingrese el año: "))
    consulta = f"""SELECT
    
v.Nombre AS Nombre_Vinedo,
COUNT(DISTINCT r.Rut) AS Numero_Clientes
FROM
Vinedo v
JOIN Tour t ON v.ID_vinedo = t.ID_vinedo
JOIN Tour_Programado tp ON t.ID_tour = tp.ID_tour
JOIN Reserva_Tour_Programado rtp ON tp.ID_tour_programado = rtp.ID_tour_programado
JOIN Reserva r ON rtp.N_operacion = r.N_operacion
WHERE
EXTRACT(YEAR FROM tp.Fecha) = {anio}
GROUP BY
v.Nombre
ORDER BY
Numero_Clientes DESC;

    """ 
    cursor.execute(consulta)
    grafico_sectores = cursor.fetchall()
    print("Gráfico de sectores:\n")
    for vinedo in grafico_sectores:
        print(f"Vinedo: {vinedo[0]}")
        print(f"Número de Clientes: {vinedo[1]}")
        print("-" * 50)
    # Crear el gráfico
    plt.figure(figsize=(10, 6))
    plt.pie([vinedo[1] for vinedo in grafico_sectores], labels=[vinedo[0] for vinedo in grafico_sectores], autopct='%1.1f%%')
    plt.title(f"Número de Clientes que visitaron las viñas en el año {anio}")
    plt.show()