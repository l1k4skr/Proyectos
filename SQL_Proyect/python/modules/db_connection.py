import psycopg2
def conectar_base_datos():
    usuario = input("Ingrese el usuario de la base de datos: ")
    # Datos de conexión
    host = "localhost"  # Cambia por el host de tu base de datos
    port = 5432         # Puerto por defecto de PostgreSQL
    database = "sistema_de_tours_de_vinas"  # Nombre de tu base de datos
    user = usuario  # Usuario de la base de datos
    password = ""  # Contraseña del usuario

    try:
        # Establecer la conexión
        connection = psycopg2.connect(
            host=host,
            port=port,
            database=database,
            user=user,
            password=password
        )
        print("Conexión exitosa a la base de datos.")
        return connection
    except Exception as e:
        print("Error al conectarse a la base de datos: ", e)
        return None
