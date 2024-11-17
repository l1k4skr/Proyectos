--- Opcion 1

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

--- Opcion 2

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

--- Opcion 3
SELECT
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
    Total_Ventas DESC;

--- Opcion 4

--- Identifica todas las ventas de productos y tours de un año específico.
--- Calcula el promedio de todas las ganancias.
--- Filtra y devuelve solo aquellas operaciones (de productos o tours) que generaron ingresos superiores al promedio.
--- Clasifica las operaciones como Producto o Tour para diferenciarlas en el resultado.

WITH Ventas_Productos AS (
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

--- Opcion 4.1
WITH Ventas_Productos AS (
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

--- Opcion 5
WITH Ventas_Productos AS (
    SELECT
        EXTRACT(YEAR FROM c.Fecha) AS Anio,
        SUM(d.Cantidad * v.Precio) AS Total_Productos
    FROM
        Compra c
        JOIN Detalle d ON c.ID_compra = d.ID_compra
        JOIN Vino v ON d.ID_vino = v.ID_vino
    WHERE
        EXTRACT(YEAR FROM c.Fecha) IN (2022, 2026)
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
        EXTRACT(YEAR FROM r.Fecha) IN (2022, 2026)
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
    Anio IN (2022, 2026)
ORDER BY
    Anio;

--- Opcion 6

SELECT
        
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