def solicitud_datos():
    """Función que solicitara los datos al usuario

    Returns:
        _tuple: Una tuple con los datos ingresados por el usuario
    """
    genero = input("Ingrese su genero (M/H): ").lower()
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = int(input("Ingrese su edad: "))
    ad1 = input("Ingrese primer adjetivo: ")
    ad2 = input("Ingrese segundo adjetivo: ")
    objeto = input("Define un objeto: ")
    rP = input("Dime una relación personal (Padre, amig@, prim@, etc): ")
    
    return (nombre, apellido, edad, genero, ad1, ad2, objeto, rP)

def definidorDeGemerito(genero):
    """Función que definirá el genero del usuario
    Args:
        genero (str): El genero ingresado por el usuario
    Returns:
        str: El genero del usuario
    """
    if genero == "m":
        return 'una'
    else:
        return "un"
if '__main__' == __name__:        
        print('Bienvenido a Historias Locas')
        print('Te solicitaremos que ingreses algunos datos')
        datos = solicitud_datos()
        conjugar = definidorDeGemerito(datos[3])
        nombre = datos[0]
        ad1 = datos[4]
        ad2 = datos[5]
        objeto = datos[6]
        rP = datos[7]
        print(f"Había una vez una persona que se llamaba {nombre}. {nombre} tenia muy {ad1} su(s) {objeto}. Un dia, {nombre} le dijo a su {ad2} {rP}: \"Hola, {rP}, como estás?, a lo que {rP} respondió: \"Muy bien, y tu, {nombre}?\", a lo que {nombre} respondió: \"Muy bien también, gracias\". Y así fue como {nombre} y su {rP} se fueron a jugar a la playa.")