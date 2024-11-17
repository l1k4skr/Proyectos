# readme.md

# Sistema de Gestión de Tours de Viñas

Este proyecto es una aplicación que permite gestionar y consultar información relacionada con tours en viñedos, ventas de productos, reservas y clientes. La aplicación está desarrollada en Python y utiliza una base de datos PostgreSQL para almacenar y consultar los datos.

## Descripción General

La aplicación proporciona una interfaz de línea de comandos que presenta un menú interactivo al usuario. A través de este menú, el usuario puede acceder a diversas opciones para consultar información detallada sobre los tours realizados, reservas, ventas, informes de ganancias y estadísticas de clientes que visitaron las diferentes viñas.

## Menú de Opciones

Al ejecutar la aplicación, se muestra el siguiente menú:

```
1. Tour y valoraciones del día
2. Reservas de tours anuales
3. Ventas en viñas
4. Informe de ganancias (último año)
5. Informe comparativo de ganancias (dos años)
6. Gráfico de sectores
7. Salir

```

A continuación, se detalla cada una de las opciones disponibles en el menú:

### 1. Tour y Valoraciones del Día

**Descripción:**

Esta opción permite al usuario consultar los tours realizados en una fecha específica, junto con los clientes que asistieron y el detalle de sus valoraciones. Es útil para obtener información detallada sobre un día particular y conocer la experiencia de los clientes.

**Funcionalidad:**

- El usuario ingresa una fecha específica (año, mes y día).
- La aplicación ejecuta una consulta SQL que obtiene los tours programados para esa fecha, los clientes que asistieron y sus valoraciones.
- Se muestran los detalles de cada tour, incluyendo el horario, los clientes asistentes y las reseñas realizadas.

**Consulta SQL Utilizada:**

```sql
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
