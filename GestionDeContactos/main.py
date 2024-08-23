'''
Proyecto: Gestión de Contactos

Descripción
El proyecto consiste en un sistema de gestión de contactos donde cada contacto tiene un nombre, un número de teléfono y una lista de etiquetas (por ejemplo, "amigo", "trabajo", "familia"). El sistema debería permitirte agregar, eliminar, y buscar contactos, así como listar todos los contactos agrupados por etiquetas.

Estructuras de Datos a Utilizar
Lista: Para almacenar todos los contactos. #!
Tupla: Para representar un contacto individual (nombre y teléfono). #!
Diccionario: Para almacenar detalles adicionales de los contactos, como las etiquetas. #!
Set: Para almacenar y gestionar las etiquetas, asegurando que no haya duplicados. #!

Funcionalidades
Agregar Contacto: Permite al usuario agregar un nuevo contacto a la lista. Cada contacto es una tupla que contiene un nombre y un número de teléfono, y se asocia a un diccionario que contiene las etiquetas como un set.#!
Eliminar Contacto: Permite al usuario eliminar un contacto existente por nombre.#!
Buscar Contacto: Permite al usuario buscar un contacto por nombre y mostrar la información del contacto.#!
Listar Contactos por Etiquetas: Muestra todos los contactos organizados por etiquetas, usando sets para evitar etiquetas duplicadas.#!

Ejemplo de Uso
Agregar contacto: Juan Pérez, 123456789, etiquetas: ['amigo', 'trabajo']
Buscar contacto: Juan Pérez
Eliminar contacto: Juan Pérez
Listar contactos por etiquetas: amigo: Juan Pérez, María López

Requisitos
Implementar funciones para cada una de las funcionalidades mencionadas.
Asegurarte de manejar adecuadamente los casos en los que no existan contactos, o cuando se busque uno que no esté en la lista.

'''
# ERROR HANDLERS 
def error_name_handler():
    print('Error debes ingresar un nombre')

def error_not_founds():
    print('No se han encontrado usuarios')

#Functions 
def agregar_contacto(contacto):
    contactos.append(contacto)

def crear_contacto(nombre, telefono, etiquetas):
    return (nombre, telefono, {'Etiquetas':etiquetas})

def eliminar_contacto(nombre):
    if nombre == '':
        error_name_handler()
        return
    for index, contacto in enumerate(contactos):
        if contacto[0] == nombre:
            contactos.pop(index)
        else:
            error_not_founds()

def buscar_contacto(nombre):
    if nombre == '':
        error_name_handler()
        return
    for contacto in contactos:
        if contacto[0] == nombre:
            print(contacto)
            return
        else:
            error_not_founds()

def listar_por_etiqueta(etiqueta):
    found = False
    for contacto in contactos:
        if etiqueta in contacto[2]['Etiquetas']:
            print(contacto)
            found = not found
        else:
            pass
    if not found:
        error_not_founds()


if '__main__' == __name__:
    while True:
        print('Bienvenido a la gestion de contactos')
        print('1. Agregar contacto')
        print('2. Eliminar contacto')
        print('3. Buscar contacto')
        print('4. Listar contactos por etiqueta')
        print('5. Salir')
        opcion = int(input('Ingrese una opcion: '))

contactos = []

contacto1 = crear_contacto('Andres', '999999999', {'Familia', 'Trabajo', 'Estudiante', 'Amigo'}) 
contacto2 = crear_contacto('Camila', '999999999', {'Trabajo', 'Estudiante', 'Amigo'}) 
contacto3 = crear_contacto('Arturo', '999999999', {'Estudiante'}) 


agregar_contacto(contacto1)
agregar_contacto(contacto2)
agregar_contacto(contacto3)


# print(contactos)
# buscar_contacto('Andres')
# eliminar_contacto('')
listar_por_etiqueta('Estudiante')
# print(contactos)